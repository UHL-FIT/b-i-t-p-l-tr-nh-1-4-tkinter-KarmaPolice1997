import tkinter as tk

root = tk.Tk()
root.title("Ứng dụng đầu tiên - Đào Đức Phúc")
root.geometry("500500")

nhan_chao = tk.Label(root, text="Chào mừng sinh viên Đại học Hạ Long!")
nhan_chao.pack(pady=50)

root.mainloop()
