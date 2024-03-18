#sürücü.find_element(By.CSS_SELECTOR, '[aria-controls="react-autowhatever-1"]').send_keys(gidilecekadres)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import pyautogui

def selenium():
    gidilecekadres = input("İlgilendiğiniz Hisseyi giriniz:")
    alısfiyati = float(input("Alış fiyatınız:"))
    kacadetalis = int(input("Kac adet Lot Mevcut:"))
    kullaniciadi = input("Lütfen Fintables E-Mailinizi Giriniz")
    sifre = input("Lütfen Fintables Sifrenizi Giriniz")

    kar = None
    mesaj = f"Kar durumunuz{kar}"

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
    sürücü.find_element(By.CSS_SELECTOR, '[class="whitespace-nowrap font-bold text-foreground-02 hover:text-foreground-01"]').click()
    time.sleep(1)
    sürücü.find_element(By.CSS_SELECTOR, '[class="focus:ring-shared-brand-solid-01 focus:border-shared-brand-solid-01 text-foreground-01 border-stroke-02 block w-full sm:text-sm rounded-md bg-background-adaptive-01 h-10 w-full"]').send_keys(kullaniciadi)
    sürücü.find_element(By.CSS_SELECTOR,'[tabindex="2"]').send_keys(sifre)
    time.sleep(1)
    sürücü.find_element(By.CSS_SELECTOR, '[tabindex="3"]').click()
    #pyautogui.press('enter')
    time.sleep(2)
    sürücü.find_element(By.CSS_SELECTOR, '[class="hidden lg:inline-flex lg:flex-shrink-0 items-center rounded-lg py-1.5 px-3 bg-background-adaptive-02 text-foreground-03 hover:border-stroke-02 mt-1"]').click()
    time.sleep(1)
    #sürücü.find_element(By.CSS_SELECTOR, '[class="font-medium"]').send_keys(sifre)
    sürücü.find_element(By.CSS_SELECTOR, '[class ="h-16 w-full border-0 bg:background-solid-01 dark:bg-background-adaptive-01 pl-11 pr-4 text-foreground-01 focus:ring-0 sm:text-xl"]').send_keys(gidilecekadres)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    #Hesaplama
    while True:
        time.sleep(2)
        anlıkfiyat = sürücü.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/span').text
        dönanlıkfiyat = anlıkfiyat.replace(',','.')
        sonanlıkfiyat = float(dönanlıkfiyat)
        #anlık fiyatı alır ve karsılastırır ardından lot sayısıyla çarpar
        yüzde = sürücü.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span/span[2]').text
        time.sleep(2)
        favök = sürücü.find_element(By.XPATH, './/*[contains(@class, "text-right py-3.5 pr-3")]').text
        saat = sürücü.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]').text
        print(favök)
        print(saat)
        print((sonanlıkfiyat - alısfiyati) * kacadetalis)
        print("Günlük Yüzdesel Değişim "," %" + yüzde)





def mail(mesaj):
    try:
        baslik = "Borsa Bilgilendirme Mesajınız"
        mesaj = None

        if mesaj is not None:
            mailiniz = "***@gmail.com"
            sifreniz = "****"
            gidecek = "**********"
            content = "Subject:{0}\n\n{1}".format(baslik, mesaj)
            outlook = SMTP("smtp-mail.outlook.com", 587)
            outlook.starttls()
            outlook.login(mailiniz, sifreniz)
            outlook.sendmail(mailiniz, gidecek, content.encode("utf-8"))
            print("Mail Gönderme İşlemi Başarılı")
    except Exception as e:
        print(e)

selenium()




