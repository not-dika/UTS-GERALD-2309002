tahun = int(input("Masukan Tahun : "))
if tahun % 400 == 0 or ((tahun % 4 == 0) and (tahun % 100!= 0)):
    print(f"Tahun {tahun} merupakan TAHUN KABISAT")
else:
    print(f"Tahun {tahun} BUKAN tahun kabisat")