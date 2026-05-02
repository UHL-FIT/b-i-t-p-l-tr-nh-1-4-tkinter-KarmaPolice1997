import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def xu_li_du_lieu():
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    thoi_gian = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

    print(f"[{thoi_gian}] | Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")
    
    if not mssv.isdigit():
        messagebox.showerror("Lỗi", "Mã sinh viên phải là số")
        return 0

    if ho_ten != "":
        nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    else:
        messagebox.showerror("Lỗi", "Vui lòng không để trống thông tin!")
        return 0


def xoa_input():
    o_nhap_ho_ten.delete(0, tk.END)
    o_nhap_ma_sv.delete(0, tk.END)

root = tk.Tk()
root.title("Quản lí sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

nhap_ma_sv = tk.Label(
    root,
    text="Mã sinh viên: "
)
o_nhap_ma_sv = tk.Entry(root)

nhap_ho_ten = tk.Label(
    root,
    text="Họ và tên: "
)
o_nhap_ho_ten = tk.Entry(root)

nhap_ma_sv.grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
    )
o_nhap_ma_sv.grid(
    row=0, column=1, padx=10, pady=10, sticky="ew"
    )

nhap_ho_ten.grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
    )
o_nhap_ho_ten.grid(
    row=1, column=1, padx=10, pady=10, sticky="ew"
    )

nut_xac_nhan = tk.Button(
    root, 
    text="Xác nhận điểm danh", 
    command=lambda: (xu_li_du_lieu(), xoa_input())
    )
nut_xac_nhan.grid(
    row=2, 
    column=0, 
    columnspan=2, 
    pady=10
    )

nhan_ket_qua = tk.Label(
    root,
    text="Xác nhận điểm danh",
    font=("Arial", 10, "italic")
)

nhan_ket_qua.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)

root.mainloop()