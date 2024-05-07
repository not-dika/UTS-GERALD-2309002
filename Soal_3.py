jb = int(input("Masukan Jumlah Barang : "))
tb = 0
for i in range(jb):
    tb += int(input(f"Masukan Harga Barang Ke-{i+1} : "))
print(f"Total Belanjaan : Rp.{tb:,.2f}")