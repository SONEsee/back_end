# credit_score_service.py
"""
Credit Score Service
====================
Service สำหรับคำนวณคะแนนเครดิตของลูกค้า โดยดึงข้อมูลจาก:
- IndividualBankIbk: ข้อมูลลูกค้า
- B1: ข้อมูลสินเชื่อ
- C1: ข้อมูลหลักประกันหลัก
- C2.x: ข้อมูลหลักประกันแต่ละประเภท
- scr_attribute_table & scr_atttype_desc: ตารางคะแนน
- request_charge: ประวัติการตรวจสอบเครดิต
- memberInfo: ข้อมูลธนาคาร
"""

from decimal import Decimal
from datetime import date, datetime
from django.db.models import Sum, Max, Count, Q, F, Case, When, DecimalField
from .models import (
    IndividualBankIbk, B1, C1,
    col_real_estates, col_money_mia, col_equipment_eqi,
    col_project_prj, col_vechicle_veh, col_guarantor_gua,
    col_goldsilver_gold, col_guarantor_com,
    scr_atttype_desc, scr_attribute_table,
    request_charge,
    memberInfo  # ⭐ เพิ่มบรรทัดนี้
)


class CreditScoreService:
    """
    Class หลักสำหรับคำนวณคะแนนเครดิต
    
    Attributes:
        lcic_id (str): รหัส LCIC ของลูกค้า
        customer (dict): ข้อมูลลูกค้า
        loans (QuerySet): ข้อมูลสินเชื่อ
        collaterals (dict): ข้อมูลหลักประกัน
    """
    
    # อัตราแลกเปลี่ยนเงินตรา (คงที่)
    EXCHANGE_RATES = {
        'USD': Decimal('9593'),  # 1 USD = 9,593 LAK
        'THB': Decimal('345'),   # 1 THB = 345 LAK
        'LAK': Decimal('1')      # 1 LAK = 1 LAK
    }
    
    def __init__(self, lcic_id):
        """
        Initialize service with lcic_id
        
        Args:
            lcic_id (str): รหัส LCIC ของลูกค้าที่ต้องการคำนวณคะแนน
        """
        self.lcic_id = lcic_id
        self.customer = None
        self.loans = None
        self.collaterals = None
    
    # =====================================================
    # HELPER FUNCTIONS
    # =====================================================
    # ⭐ get name collateral นี้
    def get_collateral_type_name(self, col_type):
        """
        Map col_type to collateral type names
        
        Args:
            col_type: รหัสประเภทหลักประกัน (เช่น 'C2.1', 'C2.2')
        
        Returns:
            dict: ชื่อหลักประกันภาษาอังกฤษและลาว
        """
        collateral_mapping = {
            'C2.1': {
                'code': 'C2.1',
                'name_eng': 'BUILDING / BUILDING+LAND / HOME / HOME+LAND / LAND',
                'name_lao': 'ອາຄານ/ ອາຄານ + ທີ່ດິນ/ ເຮືອນ/ເຮືອນ+ທີ່ດິນ/ ທີ່ດິນ'
            },
            'C2.2': {
                'code': 'C2.2',
                'name_eng': 'MONEY IN ACCOUNT',
                'name_lao': 'ເງິນໃນບັນຊີ'
            },
            'C2.3': {
                'code': 'C2.3',
                'name_eng': 'MACHINERY AND EQUIPMENTS',
                'name_lao': 'ເຄື່ອງຈັກ ແລະ ອຸປະກອນຕ່າງໆ'
            },
            'C2.4': {
                'code': 'C2.4',
                'name_eng': 'PROJECT',
                'name_lao': 'ໂຄງການ'
            },
            'C2.5': {
                'code': 'C2.5',
                'name_eng': 'VEHICLE',
                'name_lao': 'ຍານພາຫະນະ'
            },
            'C2.6': {
                'code': 'C2.6',
                'name_eng': 'GUARANTOR_IND',
                'name_lao': 'ຜູ້ຄຳ້ປະກັນບຸກຄົນ'
            },
            'C2.7': {
                'code': 'C2.7',
                'name_eng': 'GOLD AND SILVER',
                'name_lao': 'ເງິນ ແລະ ຄຳ'
            },
            'C2.8': {
                'code': 'C2.8',
                'name_eng': 'GUARANTOR_COM',
                'name_lao': 'ຜູ້ຄຳ້ປະກັນວິສາຫະກິດ'
            }
        }
        
        return collateral_mapping.get(col_type, {
            'code': col_type,
            'name_eng': f'Unknown Type ({col_type})',
            'name_lao': f'ບໍ່ຮູ້ຈັກ ({col_type})'
        })
        
    def get_bank_info(self, bnk_code):
        """
        Map bnk_code to bank information from memberInfo
        
        Args:
            bnk_code: รหัสธนาคาร (เช่น '01', '02')
        
        Returns:
            dict: ข้อมูลธนาคาร
        """
        try:
            if not bnk_code:
                return {
                    'bnk_code': None,
                    'code': None,
                    'display_code': None,
                    'name': None,
                    'name_lao': None
                }
            
            # หาธนาคารจาก bnk_code
            bank = memberInfo.objects.filter(bnk_code=bnk_code).first()
            
            if bank:
                return {
                    'bnk_code': bank.bnk_code,
                    'code': bank.code,
                    'display_code': f"{bank.code}-{bank.bnk_code}",  # เช่น "LC-01"
                    'name': bank.nameE,
                    'name_lao': bank.nameL
                }
            else:
                # ถ้าไม่เจอ return ค่าเดิม
                return {
                    'bnk_code': bnk_code,
                    'code': None,
                    'display_code': bnk_code,
                    'name': f"Unknown Bank ({bnk_code})",
                    'name_lao': f"ບໍ່ຮູ້ຈັກ ({bnk_code})"
                }
        except Exception as e:
            return {
                'bnk_code': bnk_code,
                'code': None,
                'display_code': bnk_code,
                'name': f"Error: {str(e)}",
                'name_lao': None
            }
    
    def convert_to_lak(self, value, currency):
        """
        แปลงค่าเงินเป็น LAK
        
        Args:
            value: จำนวนเงิน
            currency: สกุลเงิน (USD, THB, LAK)
        
        Returns:
            Decimal: มูลค่าใน LAK
        """
        try:
            if not value:
                return Decimal('0')
            
            value = Decimal(str(value))
            rate = self.EXCHANGE_RATES.get(currency, Decimal('1'))
            return value * rate
        except:
            return Decimal('0')
    
    # =====================================================
    # MAIN FUNCTION - เริ่มต้นการคำนวณคะแนน
    # =====================================================
    
    def calculate_final_score(self, breakdown):
        """
        คำนวณคะแนนรวมสุดท้าย
        
        สูตร: (((total_weighted_score) × 13) ÷ 100) + 350
        
        Args:
            breakdown: คะแนนแต่ละด้าน
        
        Returns:
            dict: คะแนนรวมพร้อมรายละเอียดการคำนวณ
        """
        try:
            # รวมคะแนนทุกด้าน
            scores = {}
            total_weighted_score = 0
            
            for key, value in breakdown.items():
                score = value.get('score', 0)
                scores[key] = score
                total_weighted_score += score
            
            # สูตรคำนวณคะแนนรวม
            final_score = ((total_weighted_score * 13) / 100) + 350
            
            return {
                'final_score': round(final_score, 2),
                'calculation_details': {
                    'total_weighted_score': round(total_weighted_score, 2),
                    'formula': '((total_weighted_score × 13) ÷ 100) + 350',
                    'calculation': f"(({round(total_weighted_score, 2)} × 13) ÷ 100) + 350 = {round(final_score, 2)}",
                    'individual_scores': scores
                }
            }
        except Exception as e:
            raise Exception(f"Error calculating final score: {str(e)}")
    
    def get_credit_rating(self, score):
        """
        ประเมินระดับเครดิตจากคะแนน
        """
        if score >= 700:
            return "Excellent"
        elif score >= 650:
            return "Good"
        elif score >= 600:
            return "Fair"
        elif score >= 550:
            return "Poor"
        else:
            return "Very Poor"
    
    def calculate_credit_score(self):
        """Main function to calculate credit score"""
        try:
            # 1. Get customer information
            self.customer = self.get_customer_info()
            if not self.customer:
                return None
            
            # 2. Get loan information
            loan_summary = self.get_loan_summary()
            
            # 3. Get collateral information
            collateral_summary = self.get_collateral_summary()
            
            # 4. Calculate score breakdown
            score_breakdown = self.calculate_score_breakdown(
                self.customer, 
                loan_summary, 
                collateral_summary
            )
            
            # 5. Calculate final score
            final_score_data = self.calculate_final_score(score_breakdown)
            
            # ⭐ แก้ไขตรงนี้ - เพิ่ม validation
            if isinstance(final_score_data, dict):
                final_score = final_score_data.get('final_score', 0)
            else:
                # ถ้าเป็น float โดยตรง
                final_score = final_score_data
                final_score_data = {
                    'final_score': final_score,
                    'calculation_details': {}
                }
            
            # 6. Get credit rating
            credit_rating = self.get_credit_rating(final_score)
            
            return {
                'customer_info': self.customer,
                'loan_summary': loan_summary,
                'collateral_summary': collateral_summary,
                'score_breakdown': score_breakdown,
                'final_score_calculation': final_score_data,
                'final_credit_score': final_score,
                'credit_rating': credit_rating
            }
        except Exception as e:
            import traceback
            error_detail = traceback.format_exc()
            raise Exception(f"Error calculating credit score: {str(e)}\n{error_detail}")
    
    # =====================================================
    # SECTION 1: ข้อมูลลูกค้า (Customer Information)
    # =====================================================
    
    def get_customer_info(self):
        """Get customer information from IndividualBankIbk"""
        try:
            customer = IndividualBankIbk.objects.filter(
                lcic_id=self.lcic_id
            ).first()
            
            if not customer:
                return None
            
            # Calculate age
            age = None
            if customer.ind_birth_date:
                today = date.today()
                age = today.year - customer.ind_birth_date.year - (
                    (today.month, today.day) < 
                    (customer.ind_birth_date.month, customer.ind_birth_date.day)
                )
            
            # ⭐ เพิ่ม bank info
            bank_info = self.get_bank_info(customer.bnk_code)
            
            return {
                'lcic_id': customer.lcic_id,
                'customer_id': customer.customerid,
                'bnk_code': customer.bnk_code,
                'bank_info': bank_info,  # ⭐ เพิ่มบรรทัดนี้
                'branch_code': customer.branchcode,
                'national_id': customer.ind_national_id,
                'passport': customer.ind_passport,
                'familybook': customer.ind_familybook,
                'familybook_prov_code': customer.ind_familybook_prov_code,
                'name': customer.ind_name,
                'surname': customer.ind_surname,
                'lao_name': customer.ind_lao_name,
                'lao_surname': customer.ind_lao_surname,
                'birth_date': customer.ind_birth_date,
                'age': age,
                'gender': customer.ind_gender,
                'nationality': customer.ind_nationality,
                'civil_status': customer.ind_civil_status,
            }
        except Exception as e:
            raise Exception(f"Error getting customer info: {str(e)}")
    
    # =====================================================
    # SECTION 2: ข้อมูลสินเชื่อ (Loan Information)
    # =====================================================
    
    def get_loan_summary(self):
        """
        ดึงข้อมูลสินเชื่อทั้งหมดของลูกค้าจาก B1
        
        Features:
        - แสดงสินเชื่อทั้งหมด (ทั้ง Active และ Inactive)
        - แยกคำนวณยอดรวมสำหรับ Active และ All
        - ดึงหลักประกันของแต่ละสินเชื่อ
        - หา max credit line, max days slow
        
        Returns:
            dict: สรุปข้อมูลสินเชื่อทั้งหมด
        """
        try:
            # ดึงสินเชื่อทั้งหมด (ไม่กรอง status)
            all_loans = B1.objects.filter(
                LCIC_code=self.lcic_id
            ).order_by('-lon_credit_line')
            
            # ถ้าไม่มีสินเชื่อเลย return ค่าว่าง
            if not all_loans.exists():
                return {
                    'total_loans': 0,
                    'active_loans': 0,
                    'inactive_loans': 0,
                    'loans_detail': [],
                    'total_credit_line': 0,
                    'total_outstanding_balance': 0,
                    'total_credit_line_active': 0,
                    'total_outstanding_balance_active': 0,
                    'max_credit_line': 0,
                    'max_days_slow': 0,
                    'loan_purpose': None,
                    'loan_term': None,
                    'loan_open_year': None,
                }
            
            loans_detail = []
            active_loans_count = 0
            inactive_loans_count = 0
            
            # กรองเฉพาะสินเชื่อ Active (สำหรับคำนวณคะแนน)
            active_loans = all_loans.filter(lon_status='ACTIVE')
            
            # Loop ผ่านสินเชื่อทั้งหมด
            for loan in all_loans:
                # คำนวณอายุสินเชื่อ (loan open year)
                loan_open_year = None
                if loan.lon_open_date:
                    today = date.today()
                    loan_open_year = today.year - loan.lon_open_date.year
                
                # คำนวณระยะเวลาสินเชื่อ (loan term year)
                loan_term_year = None
                if loan.lon_open_date and loan.lon_exp_date:
                    term_years = loan.lon_exp_date.year - loan.lon_open_date.year
                    loan_term_year = term_years
                
                # ดึงหลักประกันของสินเชื่อนี้
                loan_collaterals = self.get_loan_collaterals(
                    loan.loan_id,
                    loan.bnk_code,
                    loan.branch_id,
                    loan.customer_id
                )
                
                # ⭐ เพิ่ม bank info
                bank_info = self.get_bank_info(loan.bnk_code)
                
                # สร้าง dict ข้อมูลสินเชื่อ
                loan_info = {
                    'loan_id': loan.loan_id,
                    'bnk_code': loan.bnk_code,
                    'bank_info': bank_info,  # ⭐ เพิ่มบรรทัดนี้
                    'branch_id': loan.branch_id,
                    'customer_id': loan.customer_id,
                    'loan_status': loan.lon_status,
                    'product_type': loan.product_type,
                    'loan_open_date': loan.lon_open_date,
                    'loan_exp_date': loan.lon_exp_date,
                    'loan_open_year': loan_open_year,
                    'loan_term': loan.lon_term,
                    'loan_term_year': loan_term_year,
                    'loan_purpose': loan.lon_purpose_code,
                    'credit_line': float(loan.lon_credit_line) if loan.lon_credit_line else 0,
                    'outstanding_balance': float(loan.lon_outstanding_balance) if loan.lon_outstanding_balance else 0,
                    'currency': loan.lon_currency_code,
                    'interest_rate': float(loan.lon_int_rate) if loan.lon_int_rate else 0,
                    'days_slow': loan.lon_no_days_slow if loan.lon_no_days_slow else 0,
                    'loan_class': loan.lon_class,
                    'loan_type': loan.lon_type,
                    'account_no': loan.lon_account_no,
                    'collaterals': loan_collaterals['details'],
                    'total_collateral_value': loan_collaterals['total_value'],
                    'collateral_count': loan_collaterals['count'],
                }
                
                loans_detail.append(loan_info)
                
                # นับจำนวน active/inactive
                if loan.lon_status == 'ACTIVE':
                    active_loans_count += 1
                else:
                    inactive_loans_count += 1
            
            # คำนวณยอดรวมของสินเชื่อทั้งหมด
            total_credit_line = all_loans.aggregate(
                total=Sum('lon_credit_line')
            )['total'] or 0
            
            total_outstanding = all_loans.aggregate(
                total=Sum('lon_outstanding_balance')
            )['total'] or 0
            
            # คำนวณยอดรวมของสินเชื่อ Active เท่านั้น (ใช้สำหรับคำนวณคะแนน)
            total_credit_line_active = active_loans.aggregate(
                total=Sum('lon_credit_line')
            )['total'] or 0
            
            total_outstanding_active = active_loans.aggregate(
                total=Sum('lon_outstanding_balance')
            )['total'] or 0
            
            # หาสินเชื่อที่มี credit line สูงสุด (ใช้จาก active loans)
            max_credit_loan = active_loans.first() if active_loans.exists() else all_loans.first()
            
            # หาจำนวนวันค้างชำระสูงสุด (จาก active loans)
            max_days_slow = active_loans.aggregate(
                max_slow=Max('lon_no_days_slow')
            )['max_slow'] or 0
            
            # คำนวณอายุสินเชื่อ (จากสินเชื่อที่มี credit line สูงสุด)
            loan_open_year = None
            if max_credit_loan and max_credit_loan.lon_open_date:
                today = date.today()
                loan_open_year = today.year - max_credit_loan.lon_open_date.year
            
            # ดึง loan term
            loan_term = max_credit_loan.lon_term if max_credit_loan else None
            
            return {
                'total_loans': all_loans.count(),
                'active_loans': active_loans_count,
                'inactive_loans': inactive_loans_count,
                'loans_detail': loans_detail,
                
                # ยอดรวมของสินเชื่อทั้งหมด
                'total_credit_line': float(total_credit_line),
                'total_outstanding_balance': float(total_outstanding),
                
                # ยอดรวมของสินเชื่อ Active เท่านั้น (ใช้คำนวณคะแนน)
                'total_credit_line_active': float(total_credit_line_active),
                'total_outstanding_balance_active': float(total_outstanding_active),
                
                'max_credit_line': float(max_credit_loan.lon_credit_line) if max_credit_loan else 0,
                'max_days_slow': int(max_days_slow),
                'loan_purpose': max_credit_loan.lon_purpose_code if max_credit_loan else None,
                'loan_term': loan_term,
                'loan_open_year': loan_open_year,
                'loan_currency': max_credit_loan.lon_currency_code if max_credit_loan else None,
            }
        except Exception as e:
            raise Exception(f"Error getting loan summary: {str(e)}")
    
    def get_loan_collaterals(self, loan_id, bnk_code, branch_id, customer_id):
        """
        Get collaterals for a specific loan
        """
        try:
            collateral_data = []
            total_value_lak = Decimal('0')
            
            c1_records = C1.objects.filter(
                loan_id=loan_id,
                bnk_code=bnk_code,
                branch_id_code=branch_id,
                bank_customer_ID=customer_id,
                LCIC_code=self.lcic_id
            )
            
            for c1 in c1_records:
                col_type = c1.col_type
                col_id = c1.col_id
                
                # ⭐ เพิ่มบรรทัดนี้ - ดึงชื่อ collateral type
                col_type_info = self.get_collateral_type_name(col_type)
                
                # C2.1 - Real Estate
                if col_type == 'C2.1':
                    items = col_real_estates.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.1',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"Land No: {item.land_no}",
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.rel_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.2 - Money/MIA
                elif col_type == 'C2.2':
                    items = col_money_mia.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.2',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"Account: {item.account_no}",
                            'account_type': item.account_type,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.mia_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.3 - Equipment
                elif col_type == 'C2.3':
                    items = col_equipment_eqi.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.3',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"{item.machine_type} - {item.machine_no}",
                            'machine_type': item.machine_type,
                            'machine_no': item.machine_no,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.machine_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.4 - Project
                elif col_type == 'C2.4':
                    items = col_project_prj.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.4',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"{item.project_name_en}",
                            'project_name': item.project_name_en,
                            'project_name_lao': item.project_name_la,
                            'project_number': item.project_number,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.project_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.5 - Vehicle
                elif col_type == 'C2.5':
                    items = col_vechicle_veh.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.5',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"{item.model} - {item.plate_number}",
                            'model': item.model,
                            'plate_number': item.plate_number,
                            'engine_number': item.engine_number,
                            'body_number': item.body_number,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.vehicle_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.6 - Guarantor Individual
                elif col_type == 'C2.6':
                    items = col_guarantor_gua.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.6',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"{item.gua_name} {item.gua_surname}",
                            'guarantor_name': f"{item.gua_name} {item.gua_surname}",
                            'guarantor_lao_name': f"{item.gua_lao_name} {item.gua_lao_surname}",
                            'national_id': item.gua_national_id,
                            'passport': item.gua_passport,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.gua_ind_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.7 - Gold/Silver
                elif col_type == 'C2.7':
                    items = col_goldsilver_gold.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.7',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"Weight: {item.weight} {item.unit}",
                            'weight': item.weight,
                            'unit': item.unit,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.gld_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
                
                # C2.8 - Guarantor Company
                elif col_type == 'C2.8':
                    items = col_guarantor_com.objects.filter(
                        loan_id=loan_id,
                        col_id=col_id
                    )
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.8',
                            'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มบรรทัดนี้
                            'col_id': item.col_id,
                            'LCIC_code': item.LCIC_code,
                            'loan_id': item.loan_id,
                            'description': f"{item.company_name}",
                            'company_name': item.company_name,
                            'company_lao_name': item.company_lao_name,
                            'enterprise_code': item.gua_enterprise_code,
                            'value': float(value_lak),
                            'value_unit': item.value_unit,
                            'original_value': float(item.value) if item.value else 0,
                            'owner': item.owner_name,
                            'status': item.gua_com_status,
                            'is_own_loan': item.loan_id == loan_id
                        })
                        total_value_lak += value_lak
            
            return {
                'details': collateral_data,
                'count': len(collateral_data),
                'total_value': float(total_value_lak)
            }
        except Exception as e:
            return {
                'details': [],
                'count': 0,
                'total_value': 0
            }
    
    # =====================================================
    # SECTION 3: ข้อมูลหลักประกัน (Collateral Summary)
    # =====================================================
    
    def get_collateral_summary(self):
        """Get collateral summary from all C2.x tables - รวมทั้งหมดของ customer"""
        try:
            collateral_data = {}
            total_value_lak = Decimal('0')
            collateral_types = []
            
            # Get collateral types from C1 (ทั้งหมดของ customer)
            c1_records = C1.objects.filter(LCIC_code=self.lcic_id)
            c1_col_types = list(c1_records.values_list('col_type', flat=True).distinct())
            
            # C2.1 - Real Estate
            if 'C2.1' in c1_col_types or col_real_estates.objects.filter(LCIC_code=self.lcic_id).exists():
                real_estates = col_real_estates.objects.filter(LCIC_code=self.lcic_id)
                total_rel = Decimal('0')
                items = []
                
                for item in real_estates:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_rel += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'land_no': item.land_no,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.1'] = {
                        'type': 'Real Estate',
                        'count': real_estates.count(),
                        'total_value_lak': float(total_rel),
                        'items': items
                    }
                    total_value_lak += total_rel
                    collateral_types.append('C2.1')
            
            # C2.2 - Money/MIA
            if 'C2.2' in c1_col_types or col_money_mia.objects.filter(LCIC_code=self.lcic_id).exists():
                mia_records = col_money_mia.objects.filter(LCIC_code=self.lcic_id)
                total_mia = Decimal('0')
                items = []
                
                for item in mia_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_mia += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'account_no': item.account_no,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.2'] = {
                        'type': 'Money/MIA',
                        'count': mia_records.count(),
                        'total_value_lak': float(total_mia),
                        'items': items
                    }
                    total_value_lak += total_mia
                    collateral_types.append('C2.2')
            
            # C2.3 - Equipment
            if 'C2.3' in c1_col_types or col_equipment_eqi.objects.filter(LCIC_code=self.lcic_id).exists():
                equipment_records = col_equipment_eqi.objects.filter(LCIC_code=self.lcic_id)
                total_eqi = Decimal('0')
                items = []
                
                for item in equipment_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_eqi += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'machine_type': item.machine_type,
                        'machine_no': item.machine_no,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.3'] = {
                        'type': 'Equipment',
                        'count': equipment_records.count(),
                        'total_value_lak': float(total_eqi),
                        'items': items
                    }
                    total_value_lak += total_eqi
                    collateral_types.append('C2.3')
            
            # C2.4 - Project
            if 'C2.4' in c1_col_types or col_project_prj.objects.filter(LCIC_code=self.lcic_id).exists():
                project_records = col_project_prj.objects.filter(LCIC_code=self.lcic_id)
                total_prj = Decimal('0')
                items = []
                
                for item in project_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_prj += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'project_name': item.project_name_en,
                        'project_number': item.project_number,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.4'] = {
                        'type': 'Project',
                        'count': project_records.count(),
                        'total_value_lak': float(total_prj),
                        'items': items
                    }
                    total_value_lak += total_prj
                    collateral_types.append('C2.4')
            
            # C2.5 - Vehicle
            if 'C2.5' in c1_col_types or col_vechicle_veh.objects.filter(LCIC_code=self.lcic_id).exists():
                vehicle_records = col_vechicle_veh.objects.filter(LCIC_code=self.lcic_id)
                total_veh = Decimal('0')
                items = []
                
                for item in vehicle_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_veh += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'plate_number': item.plate_number,
                        'model': item.model,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.5'] = {
                        'type': 'Vehicle',
                        'count': vehicle_records.count(),
                        'total_value_lak': float(total_veh),
                        'items': items
                    }
                    total_value_lak += total_veh
                    collateral_types.append('C2.5')
            
            # C2.6 - Guarantor Individual
            if 'C2.6' in c1_col_types or col_guarantor_gua.objects.filter(LCIC_code=self.lcic_id).exists():
                guarantor_records = col_guarantor_gua.objects.filter(LCIC_code=self.lcic_id)
                total_gua = Decimal('0')
                items = []
                
                for item in guarantor_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_gua += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'guarantor_name': item.gua_name,
                        'national_id': item.gua_national_id,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.6'] = {
                        'type': 'Guarantor Individual',
                        'count': guarantor_records.count(),
                        'total_value_lak': float(total_gua),
                        'items': items
                    }
                    total_value_lak += total_gua
                    collateral_types.append('C2.6')
            
            # C2.7 - Gold/Silver
            if 'C2.7' in c1_col_types or col_goldsilver_gold.objects.filter(LCIC_code=self.lcic_id).exists():
                gold_records = col_goldsilver_gold.objects.filter(LCIC_code=self.lcic_id)
                total_gld = Decimal('0')
                items = []
                
                for item in gold_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_gld += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'weight': item.weight,
                        'unit': item.unit,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.7'] = {
                        'type': 'Gold/Silver',
                        'count': gold_records.count(),
                        'total_value_lak': float(total_gld),
                        'items': items
                    }
                    total_value_lak += total_gld
                    collateral_types.append('C2.7')
            
            # C2.8 - Guarantor Company
            if 'C2.8' in c1_col_types or col_guarantor_com.objects.filter(LCIC_code=self.lcic_id).exists():
                guarantor_com_records = col_guarantor_com.objects.filter(LCIC_code=self.lcic_id)
                total_gua_com = Decimal('0')
                items = []
                
                for item in guarantor_com_records:
                    value_lak = self.convert_to_lak(item.value, item.value_unit)
                    total_gua_com += value_lak
                    items.append({
                        'col_id': item.col_id,
                        'loan_id': item.loan_id,
                        'company_name': item.company_name,
                        'enterprise_code': item.gua_enterprise_code,
                        'value': float(value_lak),
                        'owner': item.owner_name
                    })
                
                if len(items) > 0:
                    collateral_data['C2.8'] = {
                        'type': 'Guarantor Company',
                        'count': guarantor_com_records.count(),
                        'total_value_lak': float(total_gua_com),
                        'items': items
                    }
                    total_value_lak += total_gua_com
                    collateral_types.append('C2.8')
            
            return {
                'total_collateral_value_lak': float(total_value_lak),
                'collateral_types': collateral_types,
                'collateral_count': len(collateral_types),
                'details': collateral_data
            }
        except Exception as e:
            raise Exception(f"Error getting collateral summary: {str(e)}")
    
    # =====================================================
    # SECTION 4: Inquiries (ประวัติการตรวจสอบเครดิต)
    # =====================================================
    
    def get_inquiries_count(self):
        """
        นับจำนวนครั้งที่ถูกตรวจสอบเครดิต (ยกเว้นธนาคารตัวเอง)
        
        เงื่อนไข:
        - ดึงเฉพาะ chg_code = 'FCR' หรือ 'FCRF'
        - ยกเว้นธนาคารของลูกค้าเอง
        
        หมวดหมู่:
        - 0 = ไม่มีการตรวจสอบ
        - 1 = ตรวจสอบ 1 ครั้ง
        - 2 = ตรวจสอบมากกว่า 1 ครั้ง
        """
        try:
            # 1. ดึงรหัสธนาคารของลูกค้า
            customer_bnk_code = None
            if self.customer:
                customer_bnk_code = self.customer.get('bnk_code')
            
            # 2. นับจำนวนการตรวจสอบจาก request_charge
            inquiries = request_charge.objects.filter(
                LCIC_code=self.lcic_id,
                chg_code__in=['FCR', 'FCRF']
            )
            
            # 3. ยกเว้นการตรวจสอบจากธนาคารของลูกค้าเอง
            if customer_bnk_code:
                inquiries = inquiries.exclude(bnk_code=customer_bnk_code)
            
            # 4. นับจำนวน
            inquiry_count = inquiries.count()
            
            # 5. จัดหมวดหมู่
            if inquiry_count == 0:
                category = 0
            elif inquiry_count == 1:
                category = 1
            else:
                category = 2
            
            return {
                'count': inquiry_count,
                'category': category,
                'inquiries': list(inquiries.values(
                    'rec_charge_ID',
                    'bnk_code',
                    'bnk_type',
                    'chg_code',
                    'insert_date',
                    'cusType',
                    'lon_purpose'
                ))
            }
        except Exception as e:
            return {
                'count': 0,
                'category': 0,
                'inquiries': [],
                'error': str(e)
            }
    
    # =====================================================
    # SECTION 5: คำนวณคะแนน (Scoring)
    # =====================================================
    
    def get_weighted_score(self, att_type, att_code):
        """
        คำนวณคะแนนแบบง่าย (ไม่มี range)
        
        สูตร: att_value × att_weight
        """
        try:
            result = scr_attribute_table.objects.filter(
                att_type=att_type,
                att_code=att_code
            ).first()
            
            if result:
                att_desc = scr_atttype_desc.objects.filter(att_type=att_type).first()
                if att_desc:
                    return result.att_value * att_desc.att_weight
            return 0
        except:
            return 0
    
    def get_weighted_score_range(self, att_type, value):
        """
        คำนวณคะแนนแบบ range (เช่น อายุ 30-40 ปี)
        """
        try:
            attributes = scr_attribute_table.objects.filter(att_type=att_type)
            
            for attr in attributes:
                if '|' in attr.att_code:
                    parts = attr.att_code.split('|')
                    min_val = Decimal(parts[0]) if parts[0] else Decimal('0')
                    max_val = Decimal(parts[1]) if parts[1] else Decimal('999999999')
                    
                    if min_val <= Decimal(str(value)) <= max_val:
                        att_desc = scr_atttype_desc.objects.filter(att_type=att_type).first()
                        if att_desc:
                            return attr.att_value * att_desc.att_weight
            return 0
        except:
            return 0
    
    def get_weighted_score_detail(self, att_type, att_code):
        """
        คำนวณคะแนนพร้อมรายละเอียด (แบบไม่มี range)
        """
        try:
            result = scr_attribute_table.objects.filter(
                att_type=att_type,
                att_code=att_code
            ).first()
            
            if result:
                att_desc = scr_atttype_desc.objects.filter(att_type=att_type).first()
                if att_desc:
                    weighted_score = result.att_value * att_desc.att_weight
                    return {
                        'score': float(weighted_score),
                        'att_type': att_type,
                        'att_type_desc': att_desc.att_type_desc,
                        'att_type_lao_desc': att_desc.att_type_lao_desc,
                        'att_code': att_code,
                        'att_name': result.att_name,
                        'att_value': result.att_value,
                        'att_weight': att_desc.att_weight,
                        'formula': f"{result.att_value} × {att_desc.att_weight} = {float(weighted_score)}"
                    }
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': att_code,
                'message': 'Not found in scoring table'
            }
        except Exception as e:
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': att_code,
                'error': str(e)
            }
    
    def get_weighted_score_range_detail(self, att_type, value):
        """
        Get weighted score for range-based attributes with details
        
        รองรับทั้ง:
        - แบบไม่มี range: att_code = "0" 
        - แบบมี range: att_code = "1|29", "30|60"
        """
        try:
            attributes = scr_attribute_table.objects.filter(att_type=att_type)
        
            for attr in attributes:
                # กรณีที่ 1: att_code ไม่มี | (เช่น "0")
                if '|' not in attr.att_code:
                    if str(value) == str(attr.att_code):
                        att_desc = scr_atttype_desc.objects.filter(att_type=att_type).first()
                        if att_desc:
                            weighted_score = attr.att_value * att_desc.att_weight
                            return {
                                'score': float(weighted_score),
                                'att_type': att_type,
                                'att_type_desc': att_desc.att_type_desc,
                                'att_type_lao_desc': att_desc.att_type_lao_desc,
                                'att_code': attr.att_code,
                                'att_name': attr.att_name,
                                'att_value': attr.att_value,
                                'att_weight': att_desc.att_weight,
                                'input_value': float(value),
                                'range': f"Exact match: {attr.att_code}",
                                'formula': f"{attr.att_value} × {att_desc.att_weight} = {float(weighted_score)}"
                            }
            
                # กรณีที่ 2: att_code มี | (เช่น "1|29", "30|60")
                else:
                    parts = attr.att_code.split('|')
                    try:
                        min_val = Decimal(parts[0]) if parts[0] else Decimal('0')
                        max_val = Decimal(parts[1]) if parts[1] else Decimal('999999999')
                    
                        if min_val <= Decimal(str(value)) <= max_val:
                            att_desc = scr_atttype_desc.objects.filter(att_type=att_type).first()
                            if att_desc:
                                weighted_score = attr.att_value * att_desc.att_weight
                                return {
                                    'score': float(weighted_score),
                                    'att_type': att_type,
                                    'att_type_desc': att_desc.att_type_desc,
                                    'att_type_lao_desc': att_desc.att_type_lao_desc,
                                    'att_code': attr.att_code,
                                    'att_name': attr.att_name,
                                    'att_value': attr.att_value,
                                    'att_weight': att_desc.att_weight,
                                    'input_value': float(value),
                                    'range': f"{float(min_val)} - {float(max_val)}",
                                    'formula': f"{attr.att_value} × {att_desc.att_weight} = {float(weighted_score)}"
                                }
                    except (ValueError, IndexError):
                        continue
        
            return {
                'score': 0,
                'att_type': att_type,
                'input_value': float(value) if value else None,
                'message': 'Value not in any range'
            }
        except Exception as e:
            return {
                'score': 0,
                'att_type': att_type,
                'input_value': float(value) if value else None,
                'error': str(e)
            }
    
    def calculate_score_breakdown(self, customer, loan_summary, collateral_summary):
        """Calculate score breakdown for each attribute with detailed information"""
        try:
            breakdown = {}
            
            # 1. Gender Score
            gender_detail = self.get_weighted_score_detail('gdID', customer.get('gender', ''))
            breakdown['gender'] = {
                'score': gender_detail['score'],
                'input_value': customer.get('gender'),
                'details': gender_detail
            }
            
            # 2. Province Score
            province_code = customer.get('familybook_prov_code', '')
            
            if province_code:
                province_detail = self.get_weighted_score_detail('cpID', province_code)
                breakdown['province'] = {
                    'score': province_detail['score'],
                    'input_value': province_code,
                    'details': province_detail
                }
            else:
                breakdown['province'] = {
                    'score': 0,
                    'input_value': None,
                    'details': {
                        'att_type': 'cpID',
                        'message': 'No province code found'
                    }
                }
            
            # 3. Marital Status Score
            marital_detail = self.get_weighted_score_detail('mstatusID', customer.get('civil_status', ''))
            breakdown['marital_status'] = {
                'score': marital_detail['score'],
                'input_value': customer.get('civil_status'),
                'details': marital_detail
            }
            
            # 4. Age Score
            age_detail = self.get_weighted_score_range_detail('AgeID', customer.get('age', 0))
            breakdown['age'] = {
                'score': age_detail['score'],
                'input_value': customer.get('age'),
                'details': age_detail
            }
            
            # 5. Loan Purpose Score
            loan_purpose_detail = self.get_weighted_score_detail('lpID', loan_summary.get('loan_purpose', ''))
            breakdown['loan_purpose'] = {
                'score': loan_purpose_detail['score'],
                'input_value': loan_summary.get('loan_purpose'),
                'details': loan_purpose_detail
            }
            
            # 6. Loan Term Score
            loan_term_detail = self.get_weighted_score_detail('ltID', loan_summary.get('loan_term', ''))
            breakdown['loan_term'] = {
                'score': loan_term_detail['score'],
                'input_value': loan_summary.get('loan_term'),
                'details': loan_term_detail
            }
            
            # 7. Credit Line Score
            credit_line_detail = self.get_weighted_score_range_detail(
                'CLID', 
                loan_summary.get('total_credit_line_active', 0)
            )
            breakdown['credit_line'] = {
                'score': credit_line_detail['score'],
                'input_value': loan_summary.get('total_credit_line_active'),
                'details': credit_line_detail
            }
            
            # 8. Overdue Days Score
            overdue_detail = self.get_weighted_score_range_detail(
                'ovdID', 
                loan_summary.get('max_days_slow', 0)
            )
            breakdown['overdue_days'] = {
                'score': overdue_detail['score'],
                'input_value': loan_summary.get('max_days_slow'),
                'details': overdue_detail
            }
            
            # 9. Outstanding Balance Score
            outstanding_detail = self.get_weighted_score_range_detail(
                'totaloustBalance', 
                loan_summary.get('total_outstanding_balance_active', 0)
            )
            breakdown['outstanding_balance'] = {
                'score': outstanding_detail['score'],
                'input_value': loan_summary.get('total_outstanding_balance_active'),
                'details': outstanding_detail
            }
            
            # 10. Registration Year Score
            reg_year_detail = self.get_weighted_score_range_detail(
                'regID', 
                loan_summary.get('loan_open_year', 0)
            )
            breakdown['registration_year'] = {
                'score': reg_year_detail['score'],
                'input_value': loan_summary.get('loan_open_year'),
                'details': reg_year_detail
            }
            
            # 11. Inquiries Score
            inquiries_data = self.get_inquiries_count()
            inquiry_category = str(inquiries_data['category'])
            
            inquiries_detail = self.get_weighted_score_detail('inqueriesID', inquiry_category)
            breakdown['inquiries'] = {
                'score': inquiries_detail['score'],
                'input_value': {
                    'inquiry_count': inquiries_data['count'],
                    'category': inquiries_data['category'],
                    'category_description': 'No inquiries' if inquiries_data['category'] == 0 else (
                        'One inquiry' if inquiries_data['category'] == 1 else 'Multiple inquiries'
                    )
                },
                'details': {
                    **inquiries_detail,
                    'inquiries_list': inquiries_data['inquiries']
                }
            }
            
            # 12. Collateral Type Score
            col_types = collateral_summary.get('collateral_types', [])
            
            if not col_types or len(col_types) == 0:
                no_col_detail = self.get_weighted_score_detail('colTypeID', '0')
                breakdown['collateral_type'] = {
                    'score': no_col_detail['score'],
                    'input_value': [],
                    'details': no_col_detail
                }
            else:
                col_type_details = []
                total_col_type_score = Decimal('0')
                
                att_desc = scr_atttype_desc.objects.filter(att_type='colTypeID').first()
                attributes = scr_attribute_table.objects.filter(att_type='colTypeID')
                
                for col_type in col_types:
                    for attr in attributes:
                        if '|' in attr.att_code:
                            parts = attr.att_code.split('|')
                            col_code = parts[0]
                            
                            if col_code == col_type:
                                if att_desc:
                                    score = Decimal(str(attr.att_value)) * Decimal(str(att_desc.att_weight))
                                    total_col_type_score += score
                                    
                                    col_type_details.append({
                                        'col_type': col_type,
                                        'att_code': attr.att_code,
                                        'att_name': attr.att_name,
                                        'att_value': float(attr.att_value),
                                        'att_weight': float(att_desc.att_weight),
                                        'score': float(score),
                                        'formula': f"{attr.att_value} × {att_desc.att_weight} = {float(score)}"
                                    })
                                    break
                
                breakdown['collateral_type'] = {
                    'score': float(total_col_type_score),
                    'input_value': col_types,
                    'details': {
                        'att_type': 'colTypeID',
                        'att_type_desc': att_desc.att_type_desc if att_desc else None,
                        'att_type_lao_desc': att_desc.att_type_lao_desc if att_desc else None,
                        'collateral_types': col_type_details,
                        'total_score': float(total_col_type_score)
                    }
                }
            
            # 13. Collateral Value Score
            col_value = collateral_summary.get('total_collateral_value_lak', 0)
            outstanding = loan_summary.get('total_outstanding_balance_active', 0)
            
            if col_value < outstanding:
                col_value_code = 'col_val_min'
                comparison = 'Collateral value < outstanding loan'
            elif col_value == outstanding:
                col_value_code = 'col_val_equal'
                comparison = 'Equal outstanding loan'
            elif col_value > outstanding:
                col_value_code = 'col_val_max'
                comparison = 'Collateral value > outstanding loan'
            else:
                col_value_code = 'col_val_min'
                comparison = 'Unknown comparison'
            
            col_value_detail = self.get_weighted_score_detail('colValueID', col_value_code)
            breakdown['collateral_value'] = {
                'score': col_value_detail['score'],
                'input_value': {
                    'collateral_value': col_value,
                    'outstanding_balance': outstanding,
                    'comparison': comparison,
                    'code': col_value_code
                },
                'details': col_value_detail
            }
            
            return breakdown
        except Exception as e:
            raise Exception(f"Error calculating score breakdown: {str(e)}")
        
        