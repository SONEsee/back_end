from decimal import Decimal
from django.forms.models import model_to_dict
from datetime import date, datetime
from django.forms.models import model_to_dict
from django.db.models import Sum, Max, Count, Q, F, Case, When, DecimalField
from .models import (
    IndividualBankIbk, B1, C1,
    col_real_estates, col_money_mia, col_equipment_eqi,
    col_project_prj, col_vechicle_veh, col_guarantor_gua,
    col_goldsilver_gold, col_guarantor_com,
    scr_atttype_desc, scr_attribute_table,
    request_charge,
    memberInfo 
)

class CreditScoreCalculator:
        
    def get_individual_data(self, lcic_id=None, ind_sys_id=None):
        """
        Logic ดึงข้อมูลอยู่ทั้งหมดที่นี่
        """
        customer = IndividualBankIbk.objects.all()
        if ind_sys_id:
            customer = customer.filter(ind_sys_id=ind_sys_id).first()
            return self.format_output(customer)
        if lcic_id:
            customer = customer.filter(lcic_id=lcic_id).first()
            return self.format_output(customer)
        return self.format_output(customer)
    
    def get_attribute(self, att_type, code):
        """
        ດຶງຂໍ້ມູນ attribute ຈາກ scr_attribute_table ໂດຍກຳນົດ att_type ແລະ code
        """
        attr = scr_attribute_table.objects.filter(
            att_type=att_type,
            att_code=code
        ).first()

        if attr is None:
            return None
        return attr.att_name   # Return text only ("Female", "Married", ...)
        # return {
        #     "id": attr.att_id,
        #     "field": attr.att_type,
        #     "text": attr.att_name,
        #     "score": attr.att_value,
        # }
    def get_age(self, birth_date):
        if birth_date is None:
            return None
        # birth_date อาจเป็น string ต้องแปลงก่อน
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = date.today()
        # คิดอายุแบบสากล
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        return age
    
    def get_loans(self, customer):
        """
        ດຶງຂໍ້ມູນສິນເຊື່ອ B1 ທັງໝົດ ທຸກ column ໂດຍ filter ດ້ວຍ customer_id
        """
        if customer is None:
            return []
        loans = B1.objects.filter(LCIC_code=customer.lcic_id)
        return [model_to_dict(loan) for loan in loans]
    
    def get_collateral_all(self, model, customer):
        """
        ฟังก์ชันกลาง: ดึงหลักประกันจาก model ตาม LCIC_code
        """
        if customer is None:
            return []
        items = model.objects.filter(loan_id=customer.lcic_id)
        return [model_to_dict(item) for item in items]
    def get_collateral(self, customer):
        return self.get_collateral_all(C1, customer)
    def get_real_estates(self, customer):
        return self.get_collateral_all(col_real_estates, customer)
    def get_money_mia(self, customer):
        return self.get_collateral_all(col_money_mia, customer)
    def get_equipment_eqi(self, customer):
        return self.get_collateral_all(col_equipment_eqi, customer)
    def get_project_prj(self, customer):
        return self.get_collateral_all(col_project_prj, customer)
    def get_vechicle_veh(self, customer):
        return self.get_collateral_all(col_vechicle_veh, customer)
    def get_guarantor_gua(self, customer):
        return self.get_collateral_all(col_guarantor_gua, customer)
    def get_goldsilver_gold(self, customer):
        return self.get_collateral_all(col_goldsilver_gold, customer)
    def get_guarantor_com(self, customer):
        return self.get_collateral_all(col_guarantor_com, customer)

    def format_output(self, customer):
        if customer is None:
            return None
        if hasattr(customer, "__iter__") and not isinstance(customer, dict):
            return [self.format_output(obj) for obj in customer]
        if customer.ind_familybook or customer.ind_familybook_prov_code:
            familybook = f"{customer.ind_familybook or ''}-{customer.ind_familybook_prov_code or ''}".strip("-")
        else:
            familybook = None
        gender = self.get_attribute("gdID", customer.ind_gender)
        address = self.get_attribute("cpID", customer.ind_familybook_prov_code)
        marital = self.get_attribute("mstatusID", customer.ind_civil_status)
        age = self.get_age(customer.ind_birth_date)
        loans = self.get_loans(customer)
        collateral = self.get_collateral(customer)
        real_estates = self.get_real_estates(customer)
        money_mia = self.get_money_mia(customer)
        equipment_eqi = self.get_equipment_eqi(customer)    
        project_prj = self.get_project_prj(customer)
        vechicle_veh = self.get_vechicle_veh(customer)
        guarantor_gua = self.get_guarantor_gua(customer)
        goldsilver_gold = self.get_goldsilver_gold(customer)
        guarantor_com = self.get_guarantor_com(customer)

        return {
            "lcic_id": customer.lcic_id,
            "ind_lao_name": customer.ind_lao_name,
            "customer_id": customer.customerid,
            "ind_lao_surname": customer.ind_lao_surname,
            "ind_name": customer.ind_name,
            "ind_surname": customer.ind_surname,
            "ind_birth_date": customer.ind_birth_date,
            "ind_nationality": customer.ind_nationality,
            "ind_national_id": customer.ind_national_id,
            "familybook": familybook,
            "address": address,
            "ind_passport": customer.ind_passport,
            "ind_gender": gender,
            "marital_status": marital,
            "age": age,
            "loans": loans,
            "collateral": collateral,
            "real_estates": real_estates,
            "money_mia": money_mia,
            "equipment_eqi": equipment_eqi,
            "project_prj": project_prj,
            "vechicle_veh": vechicle_veh,
            "guarantor_gua": guarantor_gua,
            "goldsilver_gold": goldsilver_gold,
            "guarantor_com": guarantor_com,
        }
