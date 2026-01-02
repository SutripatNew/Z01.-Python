# 1. Extract Data from SQL [library : ```pyodbc```]
``` python
# -------------- Step 1 : Query MsSQL and DELETE Historical data 3 months --------------

import pyodbc
import pandas as pd
# import urllib

# ตั้งค่า connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=TDWPOWERBI;"   # หรือใส่ IP
    "DATABASE=TNTL_PUR;"
    "UID=tntlbiadmin;"
    "PWD=admin@123;"
)

# ----------- คำสั่ง SQL ลบข้อมูล 3 เดือนย้อนหลัง -----------
delete_query = """
    DELETE FROM dbo.STG_Sugar 
    WHERE DATEFROMPARTS([YEAR], [MONTH], 1) >= DATEADD(MONTH, -3, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
    """
# รันคำสั่ง
cursor = conn.cursor()
cursor.execute(delete_query)
# ยืนยันการลบ (commit)
conn.commit()
# ----------------------- END -------------------------


# เขียน SQL Query
sql_query = """
    SELECT * 
    FROM dbo.STG_Sugar
    """

# แสดงผลลัพธ์
df_ORG = pd.read_sql(sql_query, conn)
```


# 2. Export Data to SQL [library : ```pyodbc```]


# 3. Extract Data from SQL [library : sqlalchemy]
``` python
# -------------- Step 1 : Query MsSQL and DELETE Historical data 3 months --------------

from sqlalchemy import create_engine, text, DECIMAL
import urllib
import pandas as pd

# ตั้งค่า connection
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=TDWPOWERBI;"   
    "DATABASE=TNTL_PUR;"
    "UID=tntlbiadmin;"             # SQL Login user
    "PWD=admin@123;"  # รหัสผ่าน
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


# ----------- คำสั่ง SQL ลบข้อมูล 3 เดือนย้อนหลัง -----------
delete_query = """
    DELETE FROM dbo.STG_Sugar 
    WHERE DATEFROMPARTS([YEAR], [MONTH], 1) >= DATEADD(MONTH, -3, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
    """
# รันคำสั่ง
with engine.begin() as conn:
    conn.execute(text(delete_query))
# ----------------------- END -------------------------


# เขียน SQL Query
sql_query = """
    SELECT * 
    FROM dbo.STG_Sugar
    """

# แสดงผลลัพธ์
df_ORG = pd.read_sql(sql_query, engine)
```


# 4. Export Data to SQL [library : ```sqlalchemy```]
``` python
df_all.to_sql('STG_Brent_Oil', 
              engine, 
              if_exists='replace', # append 
              index=False, 
              dtype={"PRICE": DECIMAL(18, 2)} # กำหนัดหรือไม่ก็ได้ (กำหนดเพราะข้อมูลเราได้ text)
            )	
```