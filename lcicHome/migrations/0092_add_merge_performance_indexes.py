from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies = [
        ('lcicHome', '0091_lciccodemaping'),  # Update this
    ]
    
    operations = [
        # Index for National ID queries
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_national_id_segment ON individual_bank_ibk(ind_national_id, segment) WHERE ind_national_id IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_national_id_segment;"
        ),
        
        # Index for Passport queries
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_passport_segment ON individual_bank_ibk(ind_passport, segment) WHERE ind_passport IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_passport_segment;"
        ),
        
        # Composite index for Family Book + Province
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_familybook_prov ON individual_bank_ibk(ind_familybook, ind_familybook_prov_code, segment) WHERE ind_familybook IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_familybook_prov;"
        ),
        
        # Index for English names (surname first for blocking)
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_surname_name ON individual_bank_ibk(ind_surname, ind_name, segment) WHERE ind_surname IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_surname_name;"
        ),
        
        # Index for Lao names  
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_lao_surname_name ON individual_bank_ibk(ind_lao_surname, ind_lao_name, segment) WHERE ind_lao_surname IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_lao_surname_name;"
        ),
        
        # Index for mm_ind_sys_id
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_mm_sys_id ON individual_bank_ibk(mm_ind_sys_id, segment) WHERE mm_ind_sys_id IS NOT NULL AND segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_mm_sys_id;"
        ),
        
        # Index for LCIC ID (for grouping)
        migrations.RunSQL(
            "CREATE INDEX IF NOT EXISTS idx_ibk_lcic_segment ON individual_bank_ibk(lcic_id, segment) WHERE segment = 'A1';",
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_lcic_segment;"
        ),
        
        # Functional index for normalized national ID (PostgreSQL)
        migrations.RunSQL(
            """
            CREATE INDEX IF NOT EXISTS idx_ibk_national_id_normalized 
            ON individual_bank_ibk(LOWER(REPLACE(REPLACE(ind_national_id, '-', ''), ' ', ''))) 
            WHERE ind_national_id IS NOT NULL AND segment = 'A1';
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_ibk_national_id_normalized;",
            state_operations=[]
        ),
    ]