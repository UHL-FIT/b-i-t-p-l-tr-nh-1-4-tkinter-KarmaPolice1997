import tkinter as tk

root = tk.Tk()
root.config(bg="#f8f9fa")
root.title("Thẻ sinh viên số - Đào Đức Phúc")
root.geometry("400x300")

# Tieu de di cung voi phong chu va mau
nhan_truong = tk.Label(
    root,
    text="TRƯỜNG ĐẠI HỌC HẠ LONG",
    font="white",
    bg="#0056b3"
)
nhan_truong.pack(fill="x", pady=10)

nhan_khoa = tk.Label(
    root,
    text="Khoa: Khoa học máy tính",
    font="Arial",
    fg="#008000"
)
nhan_khoa.pack(pady=5)

# Hien thi ho ten
nhan_ten = tk.Label(root, text="Họ tên: Đào Đức Phúc", font=("Arial", 12))
nhan_ten.pack(pady=5)

# Hien thi MSSV cung voi mau do
nhan_msv = tk.Label(root, text="MSSV: 24DH080018", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)

# Tao nut bam de thoat 
nut_thoat = tk.Button(
    root,
    text="Đóng ứng dụng",
    command=root.destroy,
    bg="#dc3545",
    fg="white",
    width=200,
    height=200,
)
nut_thoat.pack(pady=20)

# nhan_chao = tk.Label(root, text="Chào mừng sinh viên Đại học Hạ Long!")
# nhan_chao.pack(pady=50)

root.mainloop()