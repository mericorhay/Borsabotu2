import pymsgbox
from pymsgbox import password,prompt
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from smtplib import SMTP
import pyautogui

try:
    gidilecekadres = prompt("İlgilendiğiniz Hisseyi giriniz: ")
    alısfiyati = float(prompt("Alış fiyatınız: "))
    kacadetalis = int(prompt("Kaç adet Lot Mevcut: "))
    kullaniciadi = prompt("Lütfen Fintables E-Mailinizi Giriniz: ")
    sifre = password("Lütfen Fintables Sifrenizi Giriniz: ")
    Outlookkullaniciadi = prompt("Lütfen Outlook E-Mailinizi Giriniz: ")
    Outlooksifre = password("Lütfen Outlook Sifrenizi Giriniz: ")
    gidecekmailadres = prompt("Lütfen Karşı Mail Adresinizi Giriniz: ")

    def selenium():
        try:
            ayarlar = webdriver.ChromeOptions()
            ayarlar.add_argument("--incognito")
            ayarlar.add_argument("--no-sandbox")
            ayarlar.add_argument("--disable-gpu")
            ayarlar.add_argument("--disable-extensions")
            ayarlar.add_experimental_option("detach", True)

            sürücü = webdriver.Chrome(options=ayarlar)
            sürücü.maximize_window()
            sürücü.get("https://fintables.com/")
            time.sleep(1)

            # Fintables girişi
            sürücü.find_element(By.CSS_SELECTOR, '[class="whitespace-nowrap font-bold text-foreground-02 hover:text-foreground-01"]').click()
            time.sleep(1)
            sürücü.find_element(By.CSS_SELECTOR, '[class="focus:ring-shared-brand-solid-01 focus:border-shared-brand-solid-01 text-foreground-01 border-stroke-02 block w-full sm:text-sm rounded-md bg-background-adaptive-01 h-10 w-full"]').send_keys(kullaniciadi)
            sürücü.find_element(By.CSS_SELECTOR, '[tabindex="2"]').send_keys(sifre)
            time.sleep(4)
            sürücü.find_element(By.CSS_SELECTOR, '[tabindex="3"]').click()
            time.sleep(4)

            # Hisse arama ve seçim
            sürücü.find_element(By.CSS_SELECTOR, '[class="hidden lg:inline-flex lg:flex-shrink-0 items-center rounded-lg py-1.5 px-3 bg-background-adaptive-02 text-foreground-03 hover:border-stroke-02 mt-1"]').click()
            time.sleep(4)
            sürücü.find_element(By.CSS_SELECTOR, '[class="h-16 w-full border-0 bg:background-solid-01 dark:bg-background-adaptive-01 pl-11 pr-4 text-foreground-01 focus:ring-0 sm:text-xl"]').send_keys(gidilecekadres)
            time.sleep(4)
            pyautogui.press('enter')
            time.sleep(10)
            pymsgbox.alert("Sistem Arkaplanda Çalışacaktır. Sistemin Çalışmaya Başlaması İçin Tamam Tuşuna Basabilirsiniz.",
                             "Pencere Gizleniyor")
            time.sleep(2)
            #pyautogui.press('enter')
            sürücü.set_window_position(-2000, 0)


            while True:
                mesajs = ""
                mesaj = ""
                anlıkfiyat = sürücü.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/span').text
                time.sleep(4)
                dönanlıkfiyat = anlıkfiyat.replace(',', '.')
                sonanlıkfiyat = float(dönanlıkfiyat)
                yüzde = sürücü.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span/span[2]').text
                time.sleep(4)
                favök = sürücü.find_element(By.XPATH, './/*[contains(@class, "text-right py-3.5 pr-3")]').text
                time.sleep(4)
                saat = sürücü.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]').text
                funcsaat = int(saat[:-6])
                hesap = (sonanlıkfiyat - alısfiyati) * kacadetalis

                if (funcsaat > 10 and funcsaat <= 12):
                    mesajs = "Günaydın"
                    mesaj = f"{mesajs}\nKar/Zarar durumunuz: {hesap},\n Anlık Fiyat: {sonanlıkfiyat},\n FAVÖK Oranı: {favök},\n Ölçülen Saat: {saat},\n Günlük Yüzdesel Değişim: % {yüzde}"
                    mail(mesaj)
                elif (funcsaat > 12 and funcsaat <= 15):
                    mesajs = "İyi Günler"
                    mesaj = f"{mesajs}\nKar/Zarar durumunuz: {hesap},\n Anlık Fiyat: {sonanlıkfiyat},\n FAVÖK Oranı: {favök},\n Ölçülen Saat: {saat},\n Günlük Yüzdesel Değişim: % {yüzde}"
                    mail(mesaj)
                elif (funcsaat > 15 and funcsaat < 18):
                    mesajs = "İyi Akşamlar"
                    mesaj = f"{mesajs}\nKar/Zarar durumunuz: {hesap},\n Anlık Fiyat: {sonanlıkfiyat},\n FAVÖK Oranı: {favök},\n Ölçülen Saat: {saat},\n Günlük Yüzdesel Değişim: % {yüzde}"
                    mail(mesaj)
                elif (funcsaat == 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8,9):
                    print("Sistem kendini Uykuya alıyor Yarın Görüşmek Üzere İyi Akşamlar")
                    mesajs = "Sistem kendini Uykuya alıyor Yarın Görüşmek Üzere İyi Akşamlar"
                    mesaj = f"{mesajs}"
                    mail(mesaj)
                    time.sleep(57900)

                print("Anlık Fiyat", sonanlıkfiyat)
                print("FAVÖK Oranı", favök)
                print("Ölçülen Saat", saat)
                print("Kar/Zarar Durumunuz", hesap)
                print("Günlük Yüzdesel Değişim ", "%" + yüzde)
                print("*" * 50)
                time.sleep(3600)

        except Exception as e:
            print("Hata oluştu:", e)

    def mail(mesaj):
        try:
            baslik = "Borsa Bilgilendirme Mesajınız"
            if mesaj is not None:
                content = "Subject:{0}\n\n{1}".format(baslik, mesaj)
                outlook = SMTP("smtp-mail.outlook.com", 587)
                outlook.starttls()
                outlook.login(Outlookkullaniciadi, Outlooksifre)
                outlook.sendmail(Outlookkullaniciadi, gidecekmailadres, content.encode("utf-8"))
                print("Mail Gönderme İşlemi Başarılı")
        except Exception as e:
            print("Mail gönderme hatası:", e)

    selenium()

except KeyboardInterrupt:
    print("Klavye İnterrupt'i aldınız. Programdan çıkılıyor...")
