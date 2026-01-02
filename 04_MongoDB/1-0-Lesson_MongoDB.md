# MongoDB

## Connect with Mongo DB

ติดตั้งด้วย MongoDB : <a href="https://www.mongodb.com/try/download/community" target="_blank">Link Download</a>

<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> Code ติดตั้งก่อนเริ่ม Run </summary>

1. ติดตั้ง library : pip ```install pymongo```

2. รัน cmd <br>
    ```
    cd "C:\Program Files\MongoDB\Server\8.0\bin"
    .\mongod
    ```
</details>



<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> Code - Create </summary>

1. สร้าง ฐานข้อมูล (database) / collection (table)
    - สร้างฐานข้อมูล : <ตัวแปร db> = client['<ฐานข้อมูล>']
    - สร้าง collection : <ตัวแปร col.> = <ตัวแปร db>['<collection>']
    ``` bash
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)

    # เลือกฐานข้อมูล (database) / collection [Table]
    # หากฐานข้อมูล / collection ยังไม่มี PyMongo จะสร้างให้โดยอัตโนมัติเมื่อมีการเพิ่มข้อมูล
    db = client['mydatabase']
    MyCollection = db['customer']
    ```

2. Create
    - - เพิ่ม 1 document : **`*<ตัวแปร col.>***.insert_one( Dictionary )`
    - เพิ่มหลาย documents : **`*<ตัวแปร col.>***.insert_many( Dictionary )`
    ``` python
    # เพิ่มข้อมูล 1 document
    data = {"name": "John Doe", "age": 30, "city": "New York"}
    result = MyCollection.insert_one(data)
    print(f"ID ของเอกสารที่เพิ่ม: {result.inserted_id}")
    ## ID ของเอกสารที่เพิ่ม: 68c8e01ab5dca5068b4d15d7
    ```
    ``` python
    # เพิ่มข้อมูล หลาย documents
    datas = [
        {"name": "Bob", "age": 35, "city": "Chiang Mai"},
        {"name": "Charlie", "age": 22, "city": "Phuket"}
    ]
    results = MyCollection.insert_many(datas)
    print(f"เพิ่มเอกสาร {len(results.inserted_ids)} รายการสำเร็จ")
    ## เพิ่มเอกสาร 2 รายการสำเร็จ
    ```

</details>



<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> Code - Read </summary>

- **`*<ตัวแปร col.>***.find()`
- **`*<ตัวแปร col.>***.find({}, {เงื่อนไข : 0หรือ1})`
    - 0 คือ ไม่เอา,  1 คือ เอา
    ``` python
    # อ่าน document แรกที่เจอ
    print(MyCollection.find_one())
    # {'_id': ObjectId('68c8e01ab5dca5068b4d15d7'), 'name': 'John Doe', 'age': 30, 'city': 'New York'}
    ```
    ``` python
    # เงื่อนไข (เหมือน WHERE)
    for doc in MyCollection.find({"city": "Chiang Mai"}):
    print(doc)
    # {'_id': ObjectId('68c8e1aab83a1ebfd677e664'), 'name': 'Bob', 'age': 35, 'city': 'Chiang Mai'}
    ```
    ``` python
    # อ่านทั้งหมด
    for doc in MyCollection.find():
        print(doc)

    # {'_id': ObjectId('68c8e01ab5dca5068b4d15d7'), 'name': 'John Doe', 'age': 30, 'city': 'New York'}
    # {'_id': ObjectId('68c8e1aab83a1ebfd677e664'), 'name': 'Bob', 'age': 35, 'city': 'Chiang Mai'}
    # {'_id': ObjectId('68c8e1aab83a1ebfd677e665'), 'name': 'Charlie', 'age': 22, 'city': 'Phuket'}
    ```
</details>



<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> Code - Update [set] + ลบColumns [unset] </summary>

- update 1 document : **`*<ตัวแปร col.>***.update_one(**{เงื่อนไข}**, **{'$set' : {สิ่งที่แก้ไข}}**)`
- update หลาย documents : **`*<ตัวแปร col.>***.update_many(**{เงื่อนไข}**, **{'$set' : {สิ่งที่แก้ไข}}**)`
- เพิ่มคอลัมน์ : **`*<ตัวแปร col.>***.update_many(**{เงื่อนไข}**, **{'$set' : {สิ่งที่แก้ไขใหม่}**)`
- ลบคอลัมน์ : **`*<ตัวแปร col.>***.update_many(**{เงื่อนไข}**, **{'$unset' : {คอลัมน์ที่ลบ : ""}**)`
``` python
# update_one
MyCollection.update_one(
    {"name": "Bob"},                   # เงื่อนไข
    {"$set": {"city": "New York"}}  # สิ่งที่แก้ไข  >> จาก Bob, city: Chiang Mai
)

for i in MyCollection.find({'name':'Bob'}):
    print(i)
    
# {'_id': ObjectId('68c8e1aab83a1ebfd677e664'), 'name': 'Bob', 'age': 35, 'city': 'New York'}
```
``` python
# update_many
MyCollection.update_many(
    {"city": "New York"},
    {"$set": {"age": "60"}}
)

for i in MyCollection.find():
    print(i)
    
'''
เดิม
{'_id': ObjectId('68c8e01ab5dca5068b4d15d7'), 'name': 'John Doe', 'age': 30, 'city': 'New York'}
{'_id': ObjectId('68c8e1aab83a1ebfd677e664'), 'name': 'Bob', 'age': 35, 'city': 'New York'}
{'_id': ObjectId('68c8e1aab83a1ebfd677e665'), 'name': 'Charlie', 'age': 22, 'city': 'Phuket'}


ใหม่
{'_id': ObjectId('68c8e01ab5dca5068b4d15d7'), 'name': 'John Doe', 'age': '60', 'city': 'New York'}
{'_id': ObjectId('68c8e1aab83a1ebfd677e664'), 'name': 'Bob', 'age': '60', 'city': 'New York'}
{'_id': ObjectId('68c8e1aab83a1ebfd677e665'), 'name': 'Charlie', 'age': 22, 'city': 'Phuket'}
'''
```
</details>



<details style="background-color: #fff8907c; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
<summary> Code - Delete </summary>

1. ลบ ข้อมูล
    - **`*<ตัวแปร col.>***.delete_one(**{เงื่อนไข}**)`
    - **`*<ตัวแปร col.>***.delete_many(**{เงื่อนไข}**)`
    ``` python
    # ลบ document เดียว
    MyCollection.delete_one({"name": "Charlie"})

    # ลบหลาย document
    MyCollection.delete_many({"city": "New York"})
    ```

2. ลบ Collection
    - **`*<ตัวแปร col.>***.drop()`
    ``` python
    MyCollection.drop()
    ```

3. ลบ database
    ``` python
    client.drop_database("db")
    ```
</details>