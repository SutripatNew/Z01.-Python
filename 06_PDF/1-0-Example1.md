# Example 1

<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> ตัวอย่างที่ 1 - Basic & Detail Code </summary>

``` python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=12)

pdf.set_font('Arial', size=16, style='B')
pdf.cell(200,10, txt="My First PDF in Python", ln=True, align="C")

pdf.set_font('Arial', size=12)
pdf.multi_cell(0,10, txt="This is created using Python")

pdf.output(r'01_DataScience\ExportFile\clcoding.pdf')
print('PDF created successfully')
```

**คำอธิบาย**

<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 1. from fpdf import FPDF </summary>

- นำเข้า (import) คลาส `FPDF` จากไลบรารี `fpdf` (หรือ `fpdf2` — ทั้งสองเวอร์ชันมี API คล้ายกัน) เพื่อใช้สร้างไฟล์ PDF ใน Python
- **ข้อควรระวัง**: หากยังไม่ได้ติดตั้ง ให้ติดตั้งด้วย `pip install fpdf2` หรือ `pip install fpdf` ขึ้นกับเวอร์ชันที่ต้องการ
</details>


<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 2. pdf = FPDF() </summary>

- สร้างออบเจ็กต์ `FPDF` ใหม่ ซึ่งเป็นตัวแทนเอกสาร PDF ที่เราจะใช้งาน
- พารามิเตอร์ที่มักให้ได้เมื่อสร้าง: `orientation='P'` (แนวตั้ง), `unit='mm'` (หน่วยมิลลิเมตร), `format='A4'` (หรือ `'Letter'`) — ถ้าไม่ระบุจะใช้ค่าเริ่มต้น (แนวตั้ง, mm, A4)
</details>


<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 3. pdf.add_page()  </summary>

- เพิ่มหน้าเปล่า (new page) ให้กับเอกสาร PDF — ต้องเรียกก่อนวาดอะไรลงในหน้าถัดไป
- ถ้าต้องการระบุ orientation หรือ format ของหน้านั้น ๆ สามารถใส่พารามิเตอร์ได้ เช่น `pdf.add_page(orientation='L')`
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 4. pdf.set_font('Arial', size=12) </summary>

- เลือกฟอนต์ที่จะใช้ในข้อความถัดไป: `'Arial'` เป็นชื่อฟอนต์, `size=12` คือขนาดฟอนต์ (หน่วยเป็น point)
- ฟอนต์ที่มีให้ใช้งานแบบ built-in ส่วนใหญ่เป็นฟอนต์ Latin เท่านั้น (ไม่รองรับ Unicode/ภาษาไทยโดยตรง) — หากต้องการพิมพ์ภาษาไทยต้องฝังฟอนต์ TTF (ดูส่วนตัวอย่างเพิ่มฟอนต์ด้านล่าง)
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 5. (ซ้ำ) pdf.set_font('Arial', size=16, style='B') </summary>

- เปลี่ยนขนาดฟอนต์เป็น 16 และใส่ `style='B'` เพื่อให้ตัวหนา (Bold)
- `style` รับค่า `'B'` (bold), `'I'` (italic), `'U'` (underline) หรือรวมกันได้เช่น `'BI'`
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 6. pdf.cell(200,10, txt="My First PDF in Python", ln=True, align="C") </summary>

- วาด **cell** เดียว (เหมือนกล่องข้อความแนวนอน) ขนาดความกว้าง = `200` (หน่วยเป็น mm หรือ unit ที่ตั้งไว้), ความสูง = `10`
- `txt` คือข้อความที่จะใส่ลงใน cell
- `ln=True` หมายถึงหลังจากวาด cell นี้จะทำการขึ้นบรรทัดใหม่ (cursor ย้ายไปบรรทัดถัดไป) — ถ้า `ln=False` จะวาดต่อด้านขวาได้
- `align="C"` จัดกึ่งกลางภายใน cell (`"L"`, `"C"`, `"R"` เป็นตัวเลือก)
- **หมายเหตุ**: ถ้ากำหนดความกว้าง `w=0` จะให้ auto-fill ไปจนขอบขวาของหน้า

</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 7. pdf.set_font('Arial', size=12) </summary>

- กลับไปใช้ขนาดฟอนต์ 12 สำหรับข้อความถัดไป
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 8. pdf.multi_cell(0,10, txt="This is created using Python")  </summary>

- `multi_cell` ทำหน้าที่คล้าย `cell` แต่รองรับการขึ้นบรรทัดอัตโนมัติเมื่อข้อความยาวเกินความกว้างที่กำหนด
- พารามิเตอร์แรก `0` หมายถึงใช้ความกว้างเต็มแถว (auto width -> เท่ากับ margin ขวา)
- ความสูงของแต่ละบรรทัดที่วาด = `10`
- เหมาะสำหรับย่อหน้าหลายบรรทัดหรือข้อความยาว
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 9. pdf.output(r'01_DataScience\ExportFile\clcoding.pdf')  </summary>

- บันทึกไฟล์ PDF ลงที่พาธที่ระบุ (ที่นี่ใช้ raw string `r'...'` เพื่อหลีกเลี่ยงการตีความ backslash)
- ถ้าโฟลเดอร์ `01_DataScience\ExportFile` ไม่มีจริง จะเกิด error ดังนั้นควรตรวจสอบ/สร้างโฟลเดอร์ก่อน
</details>



<details style="background-color: #bbf8b336; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> 10. print('PDF created successfully') </summary>

- พิมพ์ข้อความในคอนโซลว่าเรียบร้อยแล้ว เป็นการยืนยันเท่านั้น
</details>

</details>




