import re


class Müşteri:
    def __init__(self):
        self.m_adı = None
        self.m_soyadı = None
        self.m_yas = None
        self.m_mail = None
        self.m_id = None

    def bilgi_alma(self):
        self.m_adı = input("Müşterinin adını giriniz: ")
        self.m_soyadı = input("Müşterinin soyadını giriniz: ")

        while True:
            try:
                self.m_yas = int(input("Müşterinin yaşını giriniz: "))
                if self.m_yas < 0:
                    print("Yaş negatif olamaz. Tekrar deneyin.")
                    continue
                break
            except ValueError:
                print("Lütfen geçerli bir yaş giriniz.")

        while True:
            self.m_mail = input("Müşterinin mail adresini giriniz: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", self.m_mail):
                break
            else:
                print("Geçersiz e-posta adresi. Lütfen doğru formatta giriniz.")

        while True:
            try:
                self.m_id = int(input("Müşterinin id'sini giriniz: "))
                break
            except ValueError:
                print("Lütfen geçerli bir id giriniz.")

        print(
            f"Müşterinin adı: {self.m_adı}, soyadı: {self.m_soyadı}, yaşı: {self.m_yas}, mail adresi: {self.m_mail}, id: {self.m_id}")


class Ürün:
    def __init__(self):
        self.ürün_adı = None
        self.stok_kodu = None
        self.stok_adedi = None
        self.fiyat = None
        self.alınan_adet = None
        self.toplam_fiyat = None

    def bilgi_alma(self):
        self.ürün_adı = input("Ürün adını giriniz: ")
        self.stok_kodu = input("Ürünün stok kodunu giriniz: ")

        while True:
            try:
                self.stok_adedi = int(input("Ürünün stok adedini giriniz: "))
                if self.stok_adedi < 0:
                    print("Stok adedi negatif olamaz.")
                    continue
                break
            except ValueError:
                print("Lütfen geçerli bir stok adedi giriniz.")

        while True:
            try:
                self.alınan_adet = int(input("Kaç adet alındığını giriniz: "))
                if self.alınan_adet > self.stok_adedi:
                    print("Alınan adet, stok adetinden fazla olamaz.")
                    continue
                break
            except ValueError:
                print("Lütfen geçerli bir adet giriniz.")

        while True:
            try:
                self.fiyat = float(input("Ürünün fiyatını giriniz: "))
                if self.fiyat < 0:
                    print("Fiyat negatif olamaz.")
                    continue
                break
            except ValueError:
                print("Lütfen geçerli bir fiyat giriniz.")

        self.toplam_fiyat = self.alınan_adet * self.fiyat
        print(f"Ürünün adı: {self.ürün_adı}, stok kodu: {self.stok_kodu}, stok adedi: {self.stok_adedi}, "
              f"alınan adet: {self.alınan_adet}, kalan adet: {self.stok_adedi - self.alınan_adet}, "
              f"fiyatı: {self.fiyat} TL, toplam fiyat: {self.toplam_fiyat} TL.")


class Personel:
    def __init__(self):
        self.p_adı = None
        self.p_soyadı = None
        self.p_maas = None
        self.p_departman = None

    def bilgi_alma(self):
        self.p_adı = input("Personelin adını giriniz: ")
        self.p_soyadı = input("Personelin soyadını giriniz: ")
        self.p_departman = input("Personelin departmanının adını giriniz: ")

        while True:
            try:
                self.p_maas = float(input("Personelin maaşını giriniz: "))
                if self.p_maas < 0:
                    print("Maaş negatif olamaz.")
                    continue
                break
            except ValueError:
                print("Lütfen geçerli bir maaş giriniz.")

        print(
            f"Personelin adı: {self.p_adı}, soyadı: {self.p_soyadı}, departmanı: {self.p_departman}, maaşı: {self.p_maas} TL.")


# Kullanıcıdan bilgi al
x = Müşteri()
x.bilgi_alma()

y = Ürün()
y.bilgi_alma()

z = Personel()
z.bilgi_alma()
