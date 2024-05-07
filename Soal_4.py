import Modul_Soal_4 as bmi

bb = int(input("Masukan Berat Badan (Kg) : "))
tb = float(input("Masukan Tinggi Badan (M) : "))
print(f"Berat Badan (Kg) : {bb}")
print(f"Tinggi Badan (Cm) : {tb*100}")
print(f"Nilai BMI Anda : {bmi.hitung_bmi(bb,tb)}")
print(f"Kategori BMI : {bmi.kategori_bmi(bmi.hitung_bmi(bb,tb))}")
