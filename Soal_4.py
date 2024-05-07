def hitung_bmi(bb, tb):
    return round(bb/(tb*tb), 1)
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi and bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi and bmi < 29.9:
        return "Kelebihan berat badan"
    elif bmi >= 30:
        return "Obesitas"

bb = int(input("Masukan Berat Badan (Kg) : "))
tb = float(input("Masukan Tinggi Badan (M) : "))
print(f"Berat Badan (Kg) : {bb}")
print(f"Tinggi Badan (Cm) : {tb*100}")
print(f"Nilai BMI Anda : {hitung_bmi(bb,tb)}")
print(f"Kategori BMI : {kategori_bmi(hitung_bmi(bb,tb))}")
