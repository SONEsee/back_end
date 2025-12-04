# # credit_score_ind.py
# """
# Credit Score Service
# ====================
# Service สำหรับคำนวณคะแนนเครดิตของลูกค้า โดยดึงข้อมูลจาก:
# - IndividualBankIbk: ข้อมูลลูกค้า
# - B1: ข้อมูลสินเชื่อ
# - C1: ข้อมูลหลักประกันหลัก
# - C2.x: ข้อมูลหลักประกันแต่ละประเภท
# - scr_attribute_table_new & scr_atttype_desc_new: ตารางคะแนน (NEW)
# - request_charge: ประวัติการตรวจสอบเครดิต
# - memberInfo: ข้อมูลธนาคาร
# """

from decimal import Decimal
from datetime import date, datetime
from django.db.models import Sum, Max, Count, Q, F, Case, When, DecimalField
from .models import (
    IndividualBankIbk, B1, C1,
    col_real_estates, col_money_mia, col_equipment_eqi,
    col_project_prj, col_vechicle_veh, col_guarantor_gua,
    col_goldsilver_gold, col_guarantor_com,
    scr_atttype_desc_new, scr_attribute_table_new,  # ⭐ เปลี่ยนเป็น _new
    request_charge,
    memberInfo,Main_catalog_cat
)


class CreditScoreServiceIND:
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
    
    def get_collateral_type_name(self, col_type):
        """
        Map col_type to collateral type names from Main_catalog_cat
        
        Args:
            col_type: รหัสประเภทหลักประกัน (เช่น 'C2.1', 'C2.2')
        
        Returns:
            dict: ชื่อหลักประกันภาษาอังกฤษและลาว
        """
        try:
            if not col_type:
                return {
                    'code': None,
                    'name_eng': 'Unknown',
                    'name_lao': 'ບໍ່ຮູ້ຈັກ'
                }
            
            # ⭐ ดึงข้อมูลจาก Main_catalog_cat
            catalog = Main_catalog_cat.objects.filter(
                ct_type='C1',
                cat_value=col_type,
                cat_status=1  # สมมติว่า 1 = active
            ).first()
            
            if catalog:
                return {
                    'code': col_type,
                    'name_eng': catalog.cat_name if catalog.cat_name else f'Unknown Type ({col_type})',
                    'name_lao': catalog.cat_lao_name if catalog.cat_lao_name else f'ບໍ່ຮູ້ຈັກ ({col_type})'
                }
            else:
                # ⭐ กรณีไม่เจอในฐานข้อมูล ใช้ค่า default
                return {
                    'code': col_type,
                    'name_eng': f'Unknown Type ({col_type})',
                    'name_lao': f'ບໍ່ຮູ້ຈັກ ({col_type})'
                }
        except Exception as e:
            return {
                'code': col_type,
                'name_eng': f'Error: {str(e)}',
                'name_lao': f'ບໍ່ຮູ້ຈັກ ({col_type})'
            }
        
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
                    'display_code': f"{bank.code}-{bank.bnk_code}",
                    'name': bank.nameE,
                    'name_lao': bank.nameL
                }
            else:
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
        ⭐ NEW: คำนวณคะแนนรวมสุดท้าย
        
        สูตร: FinalScore = 300 + (Raw/1000) * 600
        - Raw = รวมคะแนนทั้งหมดจาก breakdown
        - 1000 = คะแนนเต็ม
        - 300 = คะแนนฐาน (Base Score)
        - 600 = คะแนนสูงสุดที่เพิ่มได้ (Maximum Additional Score)
        
        Args:
            breakdown: คะแนนแต่ละด้าน
        
        Returns:
            dict: คะแนนรวมพร้อมรายละเอียดการคำนวณ
        """
        try:
            # ค่าคงที่ในสูตร
            BASE_SCORE = 300
            MAX_ADDITIONAL_SCORE = 600
            FULL_SCORE = 1000
            
            # รวมคะแนนทุกด้าน (Raw Score)
            scores = {}
            score_values = []
            raw_score = 0
            
            for key, value in breakdown.items():
                score = value.get('score', 0)
                scores[key] = score
                score_values.append(str(int(score)))  # แปลงเป็น int เพื่อไม่ให้มีทศนิยม
                raw_score += score
            
            # สร้างสูตรการบวก Raw Score พร้อมผลลัพธ์
            raw_formula = " + ".join(score_values)
            calculation = f"{raw_formula} = {int(raw_score)}"
            
            # คำนวณ Final Score ตามสูตร
            # FinalScore = 300 + (Raw/1000) * 600
            final_score = BASE_SCORE + (raw_score / FULL_SCORE) * MAX_ADDITIONAL_SCORE
            
            # สร้างสูตรการคำนวณ Final Score
            final_calculation = f"{BASE_SCORE} + ({round(raw_score, 2)}/{FULL_SCORE}) * {MAX_ADDITIONAL_SCORE} = {round(final_score, 2)}"
            
            return {
                'final_score': round(final_score, 2),
                'calculation_details': {
                    'base_score': BASE_SCORE,
                    'max_additional_score': MAX_ADDITIONAL_SCORE,
                    'full_score': FULL_SCORE,
                    'raw_score': int(raw_score),
                    'calculation': calculation,
                    'final_calculation': final_calculation,
                    'individual_scores': scores
                }
            }
        except Exception as e:
            raise Exception(f"Error calculating final score: {str(e)}")
    
    def get_credit_rating(self, score):
        """
        ประเมินระดับเครดิตจากคะแนน
        """
        if score >= 800:
            return "Excellent"
        elif score >= 740:
            return "Good"
        elif score >= 670:
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
            
            if isinstance(final_score_data, dict):
                final_score = final_score_data.get('final_score', 0)
            else:
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
            
            # ⭐ NEW: Calculate registration year from ind_insert_date
            registration_year = None
            if customer.ind_insert_date:
                today = date.today()
                registration_year = today.year - customer.ind_insert_date.year
            
            bank_info = self.get_bank_info(customer.bnk_code)
            
            return {
                'lcic_id': customer.lcic_id,
                'customer_id': customer.customerid,
                'bnk_code': customer.bnk_code,
                'bank_info': bank_info,
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
                'ind_insert_date': customer.ind_insert_date,  # ⭐ เพิ่มบรรทัดนี้
                'registration_year': registration_year,  # ⭐ เพิ่มบรรทัดนี้
            }
        except Exception as e:
            raise Exception(f"Error getting customer info: {str(e)}")
    
    # =====================================================
    # SECTION 2: ข้อมูลสินเชื่อ (Loan Information)
    # =====================================================
    
    def get_loan_summary(self):
        """
        ดึงข้อมูลสินเชื่อทั้งหมดของลูกค้าจาก B1
        
        NEW LOGIC:
        - แยก ACTIVE/WRITE-OFF และ INACTIVE
        - คำนวณ total สำหรับทั้ง 2 กลุ่ม
        
        Returns:
            dict: สรุปข้อมูลสินเชื่อทั้งหมด
        """
        try:
            # ดึงสินเชื่อทั้งหมด
            all_loans = B1.objects.filter(
                LCIC_code=self.lcic_id
            ).order_by('-lon_credit_line')
            
            if not all_loans.exists():
                return {
                    'total_loans': 0,
                    'active_loans': 0,
                    'inactive_loans': 0,
                    'loans_detail': [],
                    'has_active_or_writeoff': False,
                    'scoring_loans': [],
                    'total_credit_line_lak': 0,
                    'total_outstanding_balance_lak': 0,
                }
            
            # ⭐ NEW: แยก ACTIVE/WRITE-OFF และ INACTIVE
            active_writeoff_loans = all_loans.filter(
                lon_status__in=['ACTIVE', 'WRITE-OFF']
            )
            inactive_loans = all_loans.filter(lon_status='INACTIVE')
            
            has_active = active_writeoff_loans.exists()
            
            # เลือกกลุ่มสินเชื่อสำหรับคำนวณคะแนน
            if has_active:
                scoring_loans = active_writeoff_loans
                loan_status_used = 'ACTIVE/WRITE-OFF'
            else:
                scoring_loans = inactive_loans
                loan_status_used = 'INACTIVE'
            
            # Loop ผ่านสินเชื่อทั้งหมด
            loans_detail = []
            for loan in all_loans:
                # คำนวณอายุสินเชื่อ
                loan_open_year = None
                if loan.lon_open_date:
                    today = date.today()
                    loan_open_year = today.year - loan.lon_open_date.year
                
                # คำนวณระยะเวลาสินเชื่อ
                loan_term_year = None
                if loan.lon_open_date and loan.lon_exp_date:
                    term_years = loan.lon_exp_date.year - loan.lon_open_date.year
                    loan_term_year = term_years
                
                # แปลงเป็น LAK
                credit_line_lak = self.convert_to_lak(
                    loan.lon_credit_line,
                    loan.lon_currency_code
                )
                outstanding_lak = self.convert_to_lak(
                    loan.lon_outstanding_balance,
                    loan.lon_currency_code
                )
                
                # ดึงหลักประกัน
                loan_collaterals = self.get_loan_collaterals(
                    loan.loan_id,
                    loan.bnk_code,
                    loan.branch_id,
                    loan.customer_id
                )
                
                bank_info = self.get_bank_info(loan.bnk_code)
                
                loan_info = {
                    'loan_id': loan.loan_id,
                    'bnk_code': loan.bnk_code,
                    'bank_info': bank_info,
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
                    'credit_line_lak': float(credit_line_lak),
                    'outstanding_balance_lak': float(outstanding_lak),
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
            
            # ⭐ คำนวณ Total ในหน่วย LAK สำหรับกลุ่มที่ใช้คำนวณคะแนน
            total_credit_line_lak = Decimal('0')
            total_outstanding_lak = Decimal('0')
            
            for loan in scoring_loans:
                credit_lak = self.convert_to_lak(loan.lon_credit_line, loan.lon_currency_code)
                outstanding_lak = self.convert_to_lak(loan.lon_outstanding_balance, loan.lon_currency_code)
                total_credit_line_lak += credit_lak
                total_outstanding_lak += outstanding_lak
            
            # หาสินเชื่อที่มี credit line สูงสุด (สำหรับ regID)
            max_credit_loan = scoring_loans.first() if scoring_loans.exists() else None
            
            loan_open_year = None
            if max_credit_loan and max_credit_loan.lon_open_date:
                today = date.today()
                loan_open_year = today.year - max_credit_loan.lon_open_date.year
            
            return {
                'total_loans': all_loans.count(),
                'active_loans': active_writeoff_loans.count(),
                'inactive_loans': inactive_loans.count(),
                'loans_detail': loans_detail,
                'has_active_or_writeoff': has_active,
                'loan_status_used': loan_status_used,
                'scoring_loans': list(scoring_loans.values(
                    'loan_id', 'lon_purpose_code', 'lon_term', 'lon_class',
                    'lon_credit_line', 'lon_outstanding_balance', 'lon_currency_code',
                    'lon_open_date', 'lon_exp_date'
                )),
                'total_credit_line_lak': float(total_credit_line_lak),
                'total_outstanding_balance_lak': float(total_outstanding_lak),
                'loan_open_year': loan_open_year,
            }
        except Exception as e:
            raise Exception(f"Error getting loan summary: {str(e)}")
    
    def get_loan_collaterals(self, loan_id, bnk_code, branch_id, customer_id):
        """Get collaterals for a specific loan"""
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
                
                col_type_info = self.get_collateral_type_name(col_type)
                
                # C2.1 - Real Estate
                if col_type == 'C2.1':
                    items = col_real_estates.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.1',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_money_mia.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.2',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_equipment_eqi.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.3',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_project_prj.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.4',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_vechicle_veh.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.5',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_guarantor_gua.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.6',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_goldsilver_gold.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.7',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
                    items = col_guarantor_com.objects.filter(loan_id=loan_id, col_id=col_id)
                    for item in items:
                        value_lak = self.convert_to_lak(item.value, item.value_unit)
                        collateral_data.append({
                            'col_type': 'C2.8',
                            'col_type_name_eng': col_type_info['name_eng'],
                            'col_type_name_lao': col_type_info['name_lao'],
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
            
            c1_records = C1.objects.filter(LCIC_code=self.lcic_id)
            c1_col_types = list(c1_records.values_list('col_type', flat=True).distinct())
            
            # C2.1 - Real Estate
            if 'C2.1' in c1_col_types or col_real_estates.objects.filter(LCIC_code=self.lcic_id).exists():
                real_estates = col_real_estates.objects.filter(LCIC_code=self.lcic_id)
                total_rel = Decimal('0')
                items = []
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.1')
                
                for item in real_estates:
                    value_lak = self.convert_to_lak(item.col_value, item.value_unit)
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.2')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.3')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.4')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.5')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.6')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.7')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
                
                # ⭐ ดึงชื่อจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name('C2.8')
                
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
                        'type': col_type_info['name_eng'],  # ⭐ ใช้ชื่อจาก catalog
                        'type_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
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
        นับจำนวนครั้งที่ถูกตรวจสอบเครดิต (ยกเว้น bnk_code = '01')
        """
        try:
            inquiries = request_charge.objects.filter(
                LCIC_code=self.lcic_id,
                chg_code__in=['FCR', 'FCRF']
            ).exclude(bnk_code='01')  # ✅ ไม่นับ bnk_code = '01'
            
            inquiry_count = inquiries.count()
            
            return {
                'count': inquiry_count
            }
        except Exception as e:
            return {
                'count': 0,
                'error': str(e)
            }
    
    # =====================================================
    # SECTION 5: คำนวณคะแนน (Scoring) - NEW LOGIC
    # =====================================================
    
    def get_score_simple(self, att_type, att_code):
        """
        ⭐ NEW: คำนวณคะแนนแบบง่าย (ไม่มี range)
        + แสดง att_weight เสมอ แม้ไม่มีข้อมูล
        """
        try:
            # ⭐ ดึง att_weight ก่อนเสมอ
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            result = scr_attribute_table_new.objects.filter(
                att_type=att_type,
                att_code=att_code
            ).first()
            
            if result:
                return {
                    'score': result.att_value,
                    'att_type': att_type,
                    'att_code': att_code,
                    'att_name': result.att_name,
                    'att_value': result.att_value,
                    'att_group_id': result.att_group_id,
                    'att_desc': result.att_desc,
                    'att_weight': att_weight,
                }
            
            # ⭐ แม้ไม่มีข้อมูล ก็ return att_weight
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': att_code,
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'message': 'Not found in scoring table'
            }
        except Exception as e:
            # ⭐ กรณี error ก็ยังต้อง return att_weight
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': att_code,
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'error': str(e)
            }


    def get_score_range(self, att_type, value):
        """
        ⭐ NEW: คำนวณคะแนนแบบ range
        + แสดง att_weight เสมอ
        """
        try:
            # ⭐ ดึง att_weight ก่อนเสมอ
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            attributes = scr_attribute_table_new.objects.filter(att_type=att_type)
            
            for attr in attributes:
                if '|' not in attr.att_code:
                    if str(value) == str(attr.att_code):
                        return {
                            'score': attr.att_value,
                            'att_type': att_type,
                            'att_code': attr.att_code,
                            'att_name': attr.att_name,
                            'att_value': attr.att_value,
                            'att_group_id': attr.att_group_id,
                            'att_desc': attr.att_desc,
                            'att_weight': att_weight,
                            'input_value': value,
                            'range': f"Exact match: {attr.att_code}",
                        }
                else:
                    parts = attr.att_code.split('|')
                    try:
                        min_val = Decimal(parts[0]) if parts[0] else Decimal('0')
                        max_val = Decimal(parts[1]) if parts[1] else Decimal('999999999999')
                        
                        if min_val <= Decimal(str(value)) <= max_val:
                            return {
                                'score': attr.att_value,
                                'att_type': att_type,
                                'att_code': attr.att_code,
                                'att_name': attr.att_name,
                                'att_value': attr.att_value,
                                'att_group_id': attr.att_group_id,
                                'att_desc': attr.att_desc,
                                'att_weight': att_weight,
                                'input_value': value,
                                'range': f"{float(min_val)} - {float(max_val)}",
                            }
                    except (ValueError, IndexError):
                        continue
            
            # ⭐ ไม่เจอใน range ก็ return att_weight
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': None,
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'input_value': value,
                'message': 'Value not in any range'
            }
        except Exception as e:
            # ⭐ กรณี error
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            return {
                'score': 0,
                'att_type': att_type,
                'att_code': None,
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'input_value': value,
                'error': str(e)
            }


    def get_score_min_max(self, att_type, loans, is_active):
        """
        ⭐ NEW: คำนวณคะแนนแบบ MIN/MAX
        + แสดง att_weight เสมอ
        + แสดงเฉพาะ selected item (ไม่แสดง all_scores)
        """
        try:
            # ⭐ ดึง att_weight ก่อนเสมอ
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            scores = []
            
            for loan in loans:
                # เลือก field ตาม att_type
                if att_type == 'lpID':
                    code = loan.lon_purpose_code
                elif att_type == 'ltID':
                    code = loan.lon_term
                elif att_type == 'ovdID':
                    code = loan.lon_class
                else:
                    continue
                
                if not code:
                    continue
                
                # หาคะแนน
                score_data = self.get_score_simple(att_type, code)
                if score_data.get('score', 0) > 0:
                    scores.append({
                        'loan_id': loan.loan_id,
                        'code': code,
                        'score': score_data['score'],
                        'att_value': score_data['att_value'],
                        'att_group_id': score_data.get('att_group_id'),
                        'att_name': score_data.get('att_name'),
                        'att_weight': att_weight,
                    })
            
            if not scores:
                return {
                    'score': 0,
                    'att_type': att_type,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': att_weight,
                    'strategy': 'MIN' if is_active else 'MAX',
                    'message': 'No valid scores found'
                }
            
            # ⭐ เลือก MIN หรือ MAX
            if is_active:
                selected = min(scores, key=lambda x: x['score'])
                strategy = 'MIN'
            else:
                selected = max(scores, key=lambda x: x['score'])
                strategy = 'MAX'
            
            # ✅ แสดงเฉพาะ detail ของ selected item
            return {
                'score': selected['score'],
                'att_type': att_type,
                'att_weight': att_weight,
                'strategy': strategy,
                'selected_code': selected['code'],
                'selected_loan_id': selected['loan_id'],
                'att_value': selected['att_value'],
                'att_group_id': selected.get('att_group_id'),
                'att_name': selected.get('att_name'),
            }
        except Exception as e:
            # ⭐ กรณี error
            desc = scr_atttype_desc_new.objects.filter(att_type=att_type).first()
            att_weight = desc.att_weight if desc else 0
            
            return {
                'score': 0,
                'att_type': att_type,
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'error': str(e)
            }


    def get_collateral_type_score_min_max(self, col_types, is_active):
        """
        ⭐ NEW: คำนวณคะแนน Collateral Type แบบ MIN/MAX
        + แสดง att_weight เสมอ
        + ดึงชื่อหลักประกันจาก Main_catalog_cat
        """
        try:
            # ⭐ ดึง att_weight ก่อนเสมอ
            desc = scr_atttype_desc_new.objects.filter(att_type='colTypeID').first()
            att_weight = desc.att_weight if desc else 0
            
            scores = []
            
            for col_type in col_types:
                # ⭐ ดึงชื่อหลักประกันจาก Main_catalog_cat
                col_type_info = self.get_collateral_type_name(col_type)
                
                attributes = scr_attribute_table_new.objects.filter(
                    att_type='colTypeID',
                    att_code__startswith=col_type
                )
                
                for attr in attributes:
                    scores.append({
                        'col_type': col_type,
                        'col_type_name_eng': col_type_info['name_eng'],  # ⭐ เพิ่มชื่อภาษาอังกฤษ
                        'col_type_name_lao': col_type_info['name_lao'],  # ⭐ เพิ่มชื่อภาษาลาว
                        'att_code': attr.att_code,
                        'att_name': attr.att_name,  # ⭐ เก็บไว้สำหรับ reference (ถ้าต้องการ)
                        'score': attr.att_value,
                        'att_value': attr.att_value,
                        'att_group_id': attr.att_group_id,
                        'att_weight': att_weight,
                    })
                    break
            
            if not scores:
                return {
                    'score': 0,
                    'att_type': 'colTypeID',
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': att_weight,
                    'message': f'No collateral types found for: {col_types}'
                }
            
            # เลือก MIN หรือ MAX
            if is_active:
                selected = min(scores, key=lambda x: x['score'])
                strategy = 'MIN'
            else:
                selected = max(scores, key=lambda x: x['score'])
                strategy = 'MAX'
            
            return {
                'score': selected['score'],
                'att_type': 'colTypeID',
                'att_weight': att_weight,
                'strategy': strategy,
                'selected_col_type': selected['col_type'],
                'all_scores': scores,
                'att_value': selected['att_value'],
                'att_group_id': selected.get('att_group_id'),
                'att_name': selected.get('att_name'),  # ⭐ เก็บไว้สำหรับ reference
            }
        except Exception as e:
            # ⭐ กรณี error
            desc = scr_atttype_desc_new.objects.filter(att_type='colTypeID').first()
            att_weight = desc.att_weight if desc else 0
            
            return {
                'score': 0,
                'att_type': 'colTypeID',
                'att_name': '-',
                'att_value': 0,
                'att_weight': att_weight,
                'error': str(e)
            }
    
    def calculate_score_breakdown(self, customer, loan_summary, collateral_summary):
        """
        ⭐ NEW: คำนวณคะแนนทั้งหมด 12 parameters
        + แสดง att_weight เสมอ
        """
        try:
            breakdown = {}
            
            # ดึงข้อมูลสำหรับคำนวณ
            has_active = loan_summary.get('has_active_or_writeoff', False)
            scoring_loans_data = loan_summary.get('scoring_loans', [])
            
            # แปลงเป็น QuerySet
            if scoring_loans_data:
                loan_ids = [loan['loan_id'] for loan in scoring_loans_data]
                scoring_loans = B1.objects.filter(loan_id__in=loan_ids)
            else:
                scoring_loans = B1.objects.none()
            
            # =====================================================
            # 1. cpID (Province)
            # =====================================================
            province_code = customer.get('familybook_prov_code', '')
            
            if province_code:
                province_detail = self.get_score_simple('cpID', province_code)
            else:
                # ⭐ ไม่มี province_code ก็ยังได้ att_weight
                desc = scr_atttype_desc_new.objects.filter(att_type='cpID').first()
                province_detail = {
                    'score': 0,
                    'att_type': 'cpID',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No province code found'
                }
            
            breakdown['province'] = {
                'score': province_detail['score'],
                'input_value': province_code,
                'details': province_detail
            }
            
            # =====================================================
            # 2. mstatusID (Marital Status)
            # =====================================================
            civil_status = customer.get('civil_status', '')
            if civil_status:
                marital_detail = self.get_score_simple('mstatusID', civil_status)
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='mstatusID').first()
                marital_detail = {
                    'score': 0,
                    'att_type': 'mstatusID',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No civil status found'
                }
            
            breakdown['marital_status'] = {
                'score': marital_detail['score'],
                'input_value': civil_status,
                'details': marital_detail
            }
            
            # =====================================================
            # 3. AgeID (Age)
            # =====================================================
            age = customer.get('age', 0)
            if age and age > 0:
                age_detail = self.get_score_range('AgeID', age)
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='AgeID').first()
                age_detail = {
                    'score': 0,
                    'att_type': 'AgeID',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No age found'
                }
            
            breakdown['age'] = {
                'score': age_detail['score'],
                'input_value': age,
                'details': age_detail
            }
            
            # =====================================================
            # 4. regID (Registration Year)
            # =====================================================
            registration_year = customer.get('registration_year', 0)
            
            if registration_year is not None and registration_year > 0:
                reg_year_detail = self.get_score_range('regID', registration_year)
                breakdown['registration_year'] = {
                    'score': reg_year_detail['score'],
                    'input_value': registration_year,
                    'details': {
                        **reg_year_detail,
                        'ind_insert_date': str(customer.get('ind_insert_date')),
                        'years_since_registration': registration_year
                    }
                }
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='regID').first()
                breakdown['registration_year'] = {
                    'score': 0,
                    'input_value': None,
                    'details': {
                        'att_type': 'regID',
                        'att_code': None,
                        'att_name': '-',
                        'att_value': 0,
                        'att_weight': desc.att_weight if desc else 0,
                        'message': 'No registration date found'
                    }
                }
            
            # =====================================================
            # 5. lpID (Loan Purpose) - MIN/MAX
            # =====================================================
            if scoring_loans.exists():
                lp_detail = self.get_score_min_max('lpID', scoring_loans, has_active)
                breakdown['loan_purpose'] = {
                    'score': lp_detail['score'],
                    'input_value': lp_detail.get('selected_code'),
                    'details': lp_detail
                }
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='lpID').first()
                breakdown['loan_purpose'] = {
                    'score': 0,
                    'input_value': None,
                    'details': {
                        'att_type': 'lpID',
                        'att_name': '-',
                        'att_value': 0,
                        'att_weight': desc.att_weight if desc else 0,
                        'message': 'No loans found'
                    }
                }
            
            # =====================================================
            # 6. ltID (Loan Term)
            # =====================================================
            if scoring_loans.exists():
                loan_term_scores = []
                desc = scr_atttype_desc_new.objects.filter(att_type='ltID').first()
                att_weight = desc.att_weight if desc else 0
                
                for loan in scoring_loans:
                    if loan.lon_open_date and loan.lon_exp_date:
                        term_years = loan.lon_exp_date.year - loan.lon_open_date.year
                        term_score_data = self.get_score_range('ltID', term_years)
                        
                        if 'score' in term_score_data and term_score_data['score'] > 0:
                            loan_term_scores.append({
                                'loan_id': loan.loan_id,
                                'open_date': loan.lon_open_date,
                                'exp_date': loan.lon_exp_date,
                                'term_years': term_years,
                                'score': term_score_data['score'],
                                'att_value': term_score_data.get('att_value', 0),
                                'att_group_id': term_score_data.get('att_group_id'),
                                'att_code': term_score_data.get('att_code'),
                                'att_name': term_score_data.get('att_name'),
                                'att_weight': att_weight,
                            })
                
                if loan_term_scores:
                    # ⭐ เปลี่ยนจากเลือก MIN/MAX score เป็นเลือก longest/shortest term
                    if has_active:
                        # ACTIVE: เลือก longest term (term_years มากที่สุด)
                        loan_term_scores.sort(key=lambda x: x['term_years'], reverse=True)
                        selected = loan_term_scores[0]
                        strategy = 'LONGEST'
                    else:
                        # INACTIVE: เลือก shortest term (term_years น้อยที่สุด)
                        loan_term_scores.sort(key=lambda x: x['term_years'])
                        selected = loan_term_scores[0]
                        strategy = 'SHORTEST'
                    
                    breakdown['loan_term'] = {
                        'score': selected['score'],
                        'input_value': selected['term_years'],
                        'details': {
                            'score': selected['score'],
                            'att_type': 'ltID',
                            'att_weight': att_weight,
                            'strategy': strategy,
                            'selected_loan_id': selected['loan_id'],
                            'term_years': selected['term_years'],
                            'open_date': str(selected['open_date']),
                            'exp_date': str(selected['exp_date']),
                            'att_value': selected['att_value'],
                            'att_group_id': selected.get('att_group_id'),
                            'att_code': selected.get('att_code'),
                            'att_name': selected.get('att_name'),
                        }
                    }
                else:
                    breakdown['loan_term'] = {
                        'score': 0,
                        'input_value': None,
                        'details': {
                            'att_type': 'ltID',
                            'att_name': '-',
                            'att_value': 0,
                            'att_weight': att_weight,
                            'message': 'No valid loan terms found'
                        }
                    }
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='ltID').first()
                breakdown['loan_term'] = {
                    'score': 0,
                    'input_value': None,
                    'details': {
                        'att_type': 'ltID',
                        'att_name': '-',
                        'att_value': 0,
                        'att_weight': desc.att_weight if desc else 0,
                        'message': 'No loans found'
                    }
                }
            
            # =====================================================
            # 7. CLID (Credit Line)
            # =====================================================
            total_credit_line_lak = loan_summary.get('total_credit_line_lak', 0)
            if total_credit_line_lak > 0:
                clid_detail = self.get_score_range('CLID', total_credit_line_lak)
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='CLID').first()
                clid_detail = {
                    'score': 0,
                    'att_type': 'CLID',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No credit line found'
                }
            
            breakdown['credit_line'] = {
                'score': clid_detail['score'],
                'input_value': total_credit_line_lak,
                'details': clid_detail
            }
            
            # =====================================================
            # 8. inqueriesID (Inquiries)
            # =====================================================
            inquiries_data = self.get_inquiries_count()

            # ✅ ใช้ get_score_range เพื่อหา score จาก model
            inquiries_detail = self.get_score_range('inqueriesID', inquiries_data['count'])

            breakdown['inquiries'] = {
                'score': inquiries_detail['score'],
                'input_value': inquiries_data['count'],
                'details': inquiries_detail
            }
            
            # =====================================================
            # 9. ovdID (Overdue Class)
            # =====================================================
            if scoring_loans.exists():
                ovd_detail = self.get_score_min_max('ovdID', scoring_loans, has_active)
                breakdown['overdue_class'] = {
                    'score': ovd_detail['score'],
                    'input_value': ovd_detail.get('selected_code'),
                    'details': ovd_detail
                }
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='ovdID').first()
                breakdown['overdue_class'] = {
                    'score': 0,
                    'input_value': None,
                    'details': {
                        'att_type': 'ovdID',
                        'att_name': '-',
                        'att_value': 0,
                        'att_weight': desc.att_weight if desc else 0,
                        'message': 'No loans found'
                    }
                }
            
            # =====================================================
            # 10. colTypeID (Collateral Type)
            # =====================================================
            col_types = collateral_summary.get('collateral_types', [])
            
            if col_types:
                col_type_detail = self.get_collateral_type_score_min_max(col_types, has_active)
                breakdown['collateral_type'] = {
                    'score': col_type_detail['score'],
                    'input_value': col_types,
                    'details': col_type_detail
                }
            else:
                # ⭐ ไม่มี collateral
                desc = scr_atttype_desc_new.objects.filter(att_type='colTypeID').first()
                no_col_detail = {
                    'score': 0,
                    'att_type': 'colTypeID',
                    'att_code': None,
                    'att_name': 'No Collateral',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No collateral found'
                }
                breakdown['collateral_type'] = {
                    'score': 0,
                    'input_value': [],
                    'details': no_col_detail
                }
            
            # =====================================================
            # 11. colValueID (Collateral Value)
            # =====================================================
            col_value = collateral_summary.get('total_collateral_value_lak', 0)
            outstanding = loan_summary.get('total_outstanding_balance_lak', 0)
            
            if outstanding > 0:
                col_percentage = (col_value / outstanding) * 100
                col_value_detail = self.get_score_range('colValueID', col_percentage)
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='colValueID').first()
                col_percentage = 0
                col_value_detail = {
                    'score': 0,
                    'att_type': 'colValueID',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No outstanding balance'
                }
            
            breakdown['collateral_value'] = {
                'score': col_value_detail['score'],
                'input_value': {
                    'collateral_value_lak': col_value,
                    'outstanding_balance_lak': outstanding,
                    'percentage': round(col_percentage, 2),
                    'att_code': col_value_detail.get('att_code'),
                },
                'details': col_value_detail
            }
            
            # =====================================================
            # 12. totaloustBalance (Outstanding %)
            # =====================================================
            total_outstanding = loan_summary.get('total_outstanding_balance_lak', 0)
            total_credit = loan_summary.get('total_credit_line_lak', 0)
            
            if total_credit > 0:
                percentage = (total_outstanding / total_credit) * 100
                outstanding_detail = self.get_score_range('totaloustBalance', percentage)
            else:
                desc = scr_atttype_desc_new.objects.filter(att_type='totaloustBalance').first()
                percentage = 0
                outstanding_detail = {
                    'score': 0,
                    'att_type': 'totaloustBalance',
                    'att_code': None,
                    'att_name': '-',
                    'att_value': 0,
                    'att_weight': desc.att_weight if desc else 0,
                    'message': 'No credit line found'
                }
            
            breakdown['outstanding_balance'] = {
                'score': outstanding_detail['score'],
                'input_value': {
                    'percentage': round(percentage, 2),
                    'total_outstanding_lak': total_outstanding,
                    'total_credit_line_lak': total_credit
                },
                'details': outstanding_detail
            }
            
            return breakdown
        except Exception as e:
            raise Exception(f"Error calculating score breakdown: {str(e)}")
