import tkinter as tk
from tkinter import messagebox

# ================= DATA MENU =================
menu = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Ayam Geprek": 18000,
    "Es Teh": 5000
}

# Menyimpan pesanan aktif: {"Nama Menu": jumlah}
keranjang = {}

# ================= FUNGSI =================
def update_menu_list():
    listbox_menu.delete(0, tk.END)
    for nama, harga in menu.items():
        listbox_menu.insert(tk.END, f"{nama} - Rp{harga}")

def update_keranjang_list():
    listbox_keranjang.delete(0, tk.END)
    for nama, jumlah in keranjang.items():
        harga_satuan = menu[nama]
        subtotal = harga_satuan * jumlah
        listbox_keranjang.insert(tk.END, f"{nama} ({jumlah}x) - Rp{subtotal:,}".replace(",", "."))

def tambah_ke_keranjang():
    selected = listbox_menu.curselection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih menu dari daftar!")
        return

    try:
        jumlah = int(entry_jumlah.get())
        if jumlah <= 0: raise ValueError
    except ValueError:
        messagebox.showwarning("Peringatan", "Masukkan jumlah valid (angka positif)!")
        return

    # Ambil nama menu yang dipilih
    index = selected[0]
    item_text = listbox_menu.get(index)
    nama_menu = item_text.split(" - ")[0]

    # Tambahkan ke dictionary keranjang
    if nama_menu in keranjang:
        keranjang[nama_menu] += jumlah
    else:
        keranjang[nama_menu] = jumlah

    update_keranjang_list()
    entry_jumlah.delete(0, tk.END)
    entry_jumlah.insert(0, "1")

def hapus_keranjang():
    selected = listbox_keranjang.curselection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih item di keranjang yang ingin dihapus!")
        return
    
    index = selected[0]
    item_text = listbox_keranjang.get(index)
    nama_menu = item_text.split(" (")[0]
    
    del keranjang[nama_menu]
    update_keranjang_list()
    hitung_total() # Update total setelah hapus

def hitung_total():
    total_akhir = 0
    for nama, jumlah in keranjang.items():
        total_akhir += menu[nama] * jumlah
    
    label_total.config(text=f"Total Bayar: Rp{total_akhir:,}".replace(",", "."))

# ================= ROOT =================
root = tk.Tk()
root.title("Aplikasi Kasir Makanan")
root.geometry("450x700")
root.configure(bg="#f8f9fa")

# ================= BAGIAN ATAS: DAFTAR MENU =================
tk.Label(root, text="MENU TERSEDIA", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(pady=5)
listbox_menu = tk.Listbox(root, width=50, height=6)
listbox_menu.pack(pady=5, padx=20)
update_menu_list()

# Input Jumlah
frame_add = tk.Frame(root, bg="#f8f9fa")
frame_add.pack(pady=10)

tk.Label(frame_add, text="Jumlah:", bg="#f8f9fa").grid(row=0, column=0)
entry_jumlah = tk.Entry(frame_add, width=5)
entry_jumlah.insert(0, "1")
entry_jumlah.grid(row=0, column=1, padx=5)

btn_tambah = tk.Button(frame_add, text="Tambah ke Keranjang", command=tambah_ke_keranjang, bg="#4CAF50", fg="white")
btn_tambah.grid(row=0, column=2, padx=5)

# ================= BAGIAN TENGAH: KERANJANG =================
tk.Label(root, text="KERANJANG PESANAN", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(pady=5)
listbox_keranjang = tk.Listbox(root, width=50, height=8, fg="blue")
listbox_keranjang.pack(pady=5, padx=20)

btn_hapus_item = tk.Button(root, text="Hapus Item Keranjang", command=hapus_keranjang, bg="#f44336", fg="white", font=("Arial", 8))
btn_hapus_item.pack()

# ================= BAGIAN BAWAH: TOTAL =================
btn_hitung = tk.Button(root, text="HITUNG TOTAL BAYAR", command=hitung_total, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), height=2)
btn_hitung.pack(pady=20, fill="x", padx=50)

label_total = tk.Label(root, text="Total Bayar: Rp0", font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#2c3e50")
label_total.pack(pady=10)

root.mainloop()