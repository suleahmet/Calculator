def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Hata: Sıfıra bölünemez."

print("Basit Hesap Makinesi")
print("Toplama = +\nÇıkarma = -\nÇarpma = *\nBölme = /")

secim = input("Yapilacak islem: ")
x = float(input("Birinci sayıyı gir: "))
y = float(input("İkinci sayıyı gir: "))

if secim == "+":
    print("Sonuç:", add(x, y))
elif secim == "":
    print("Sonuç:", sub(x, y))
elif secim == "*":
    print("Sonuç:", mul(x, y))
elif secim == "/":
    print("Sonuç:", div(x, y))
else:
    print("Geçersiz işlem.")