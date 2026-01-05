import tkinter as tk
from tkinter import messagebox

# ================= DATA MENU =================
menu = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Ayam Geprek": 18000,
    "Es Teh": 5000
}

# ================= FUNGSI =================
def update_menu_list():
    listbox_menu.delete(0, tk.END)
    for nama, harga in menu.items():
        listbox_menu.insert(tk.END, f"{nama} - Rp{harga}")

def tambah_menu():
    nama = entry_nama.get()
    harga = entry_harga.get()

    if nama == "" or harga == "":
        messagebox.showwarning("Peringatan", "Data tidak boleh kosong!")
        return

    try:
        harga = int(harga)
    except ValueError:
        messagebox.showwarning("Peringatan", "Harga harus angka!")
        return

    menu[nama] = harga
    update_menu_list()
    entry_nama.delete(0, tk.END)
    entry_harga.delete(0, tk.END)

def hapus_menu():
    selected = listbox_menu.curselection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih menu terlebih dahulu!")
        return

    for i in reversed(selected):
        item = listbox_menu.get(i)
        nama = item.split(" - ")[0]
        del menu[nama]

    update_menu_list()

def hitung_total():
    selected = listbox_menu.curselection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih menu!")
        return

    if entry_jumlah.get() == "":
        messagebox.showwarning("Peringatan", "Masukan jumlah")
        return

    try:
        jumlah = int(entry_jumlah.get())
    except ValueError:
        messagebox.showwarning("Peringatan", "Jumlah harus angka!")
        return

    total = 0
    for i in selected:
        item = listbox_menu.get(i)
        nama = item.split(" - ")[0]
        total += menu[nama] * jumlah

    label_total.config(text=f"Total: Rp{total}")

# ================= ROOT =================
root = tk.Tk()
root.title("Aplikasi Menu Makanan")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0") # Memberikan warna abu-abu muda sebagai background

# ================= JUDUL =================
judul = tk.Label(
    root,
    text="DAFTAR MENU MAKANAN",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333",
    pady=20
)
judul.pack()

# ================= LIST MENU =================
listbox_menu = tk.Listbox(
    root,
    width=40,
    height=10,
    selectmode=tk.MULTIPLE,
    font=("Arial", 10)
)
listbox_menu.pack(pady=10)

update_menu_list()

# ================= INPUT MENU =================
frame_input = tk.LabelFrame(root, text="Tambah Menu Baru", bg="#f0f0f0", padx=10, pady=10)
frame_input.pack(pady=10, padx=20, fill="x")

tk.Label(frame_input, text="Nama Menu", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
tk.Label(frame_input, text="Harga", bg="#f0f0f0").grid(row=1, column=0, sticky="w")

entry_nama = tk.Entry(frame_input)
entry_harga = tk.Entry(frame_input)

entry_nama.grid(row=0, column=1, padx=10, pady=2)
entry_harga.grid(row=1, column=1, padx=10, pady=2)

tk.Button(
    frame_input,
    text="Tambah Menu",
    command=tambah_menu,
    bg="#4CAF50",
    fg="white",
    width=15
).grid(row=2, columnspan=2, pady=10)

# ================= HAPUS MENU =================
btn_hapus = tk.Button(
    root,
    text="Hapus Menu Terpilih",
    command=hapus_menu,
    bg="#f44336",
    fg="white"
)
btn_hapus.pack(pady=5)

# ================= PESANAN =================
frame_pesan = tk.Frame(root, bg="#f0f0f0")
frame_pesan.pack(pady=15)

tk.Label(frame_pesan, text="Jumlah Beli:", bg="#f0f0f0", font=("Arial", 10, "bold")).grid(row=0, column=0)
entry_jumlah = tk.Entry(frame_pesan, width=10)
entry_jumlah.grid(row=0, column=1, padx=5)

tk.Button(
    frame_pesan,
    text="Hitung Total",
    command=hitung_total,
    bg="#2196F3",
    fg="white",
    width=20
).grid(row=1, columnspan=2, pady=10)

label_total = tk.Label(
    root,
    text="Total: Rp0",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
label_total.pack(pady=10)

root.mainloop()