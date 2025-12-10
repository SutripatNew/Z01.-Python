import tkinter as tk
from tkinter import ttk
import json

# ---------------- Dictionary ----------------

# โหลดไฟล์ dictionary 
with open(r"d:\My Documents\sutripat.ng\OneDrive - Thainamthip\2. Knowledge\2. Computer\Z01.-Python\02_GUI\1.1_Dictionary.json",
          "r", encoding="utf-8") as f:
    eng_to_th = json.load(f)
    

# สร้าง dict reverse อัตโนมัติ (ไทย -> อังกฤษ)
th_to_eng = {v: k for k, v in eng_to_th.items()}


# ---------------- Function ----------------
def translate():
    word = entry.get().strip()

    if word in eng_to_th:
        output_label.config(text=eng_to_th[word], foreground="#2b6cb0")  # ฟ้า
    elif word in th_to_eng:
        output_label.config(text=th_to_eng[word], foreground="#2f855a")  # เขียว
    else:
        output_label.config(text="ไม่พบคำแปลใน Dictionary", foreground="#e53e3e")  # แดง




# ---------------- GUI ----------------
root = tk.Tk()
root.title("Mini Dictionary (EN ↔ TH)")
root.geometry("450x300")
root.configure(bg="#f2f2f7")  # สีพื้นหลังแนว iOS


# ---- Style ----
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#ffffff",
                font=("Segoe UI", 12))

style.configure("Title.TLabel",
                background="#ffffff",
                font=("Segoe UI", 16, "bold"))

style.configure("TEntry",
                padding=8,
                font=("Segoe UI", 14))

style.configure("TButton",
                padding=8,
                font=("Segoe UI", 12),
                relief="flat")

style.map("TButton",
          background=[("active", "#4299e1")],
          foreground=[("active", "white")])


# ---- Main Frame (เหมือน card) ----
frame = tk.Frame(root, bg="#ffffff", bd=0, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=230)

title = ttk.Label(frame, text="EN ↔ TH Dictionary", style="Title.TLabel")
title.pack(pady=(15, 10))

entry = ttk.Entry(frame, width=25)
entry.pack(pady=10)
entry.bind('<Return>', lambda event: translate())

btn = ttk.Button(frame, text="Translate", command=translate)
btn.pack(pady=5)

output_label = ttk.Label(frame, text="", font=("Segoe UI", 14, "bold"))
output_label.pack(pady=10)


root.mainloop()