import time
import os
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- AYARLAR ---
UBYS_URL = "https://ubys.kastamonu.edu.tr/"
DOSYA_ADI = "notlar.json"

# Secrets (Github'dan veya Çevresel Değişkenlerden alır)
OGRENCI_NO = os.environ.get("OGRENCI_NO")
SIFRE = os.environ.get("SIFRE")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# XPath
XPATH_KULLANICI_ADI = '//*[@id="username"]'
XPATH_SIFRE = '//*[@id="password"]'
XPATH_GIRIS_BUTONU = '//*[@id="loginForm"]/div[3]/div[1]/button'

def telegram_gonder(mesaj):
    try:
        if BOT_TOKEN and CHAT_ID:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {"chat_id": CHAT_ID, "text": mesaj}
            requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram hatası: {e}")

def eski_notlari_yukle():
    if os.path.exists(DOSYA_ADI):
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def yeni_notlari_kaydet(notlar):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(notlar, f, ensure_ascii=False, indent=4)
    print("💾 Veritabanı dosyası güncellendi.")

def tablodan_notlari_cek(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    satirlar = soup.find_all("tr")
    dersler = {}
    
    print(f"DEBUG: HTML içinde {len(satirlar)} satır bulundu.")

    for index, satir in enumerate(satirlar):
        hucreler = satir.find_all(["td", "th"])
        metinler = [h.get_text(strip=True) for h in hucreler if h.get_text(strip=True)]
        
        # Boş satırları atla
        if not metinler: continue
        
        # Satırdaki tüm verileri birleştir (Örn: Matematik | Vize:50 | Ödev:100)
        satir_metni = " | ".join(metinler)
        
        # Satır indexi ile kaydet ki aynı isimli dersler karışmasın
        dersler[f"Satir_{index}"] = satir_metni

    return dersler

def karsilastir_ve_bildir(eski, yeni):
    if not yeni: return False

    yeni_degerler = set(yeni.values())
    eski_degerler = set(eski.values())
    
    # Sadece yeni eklenen veya değişen satırları bul
    farklar = yeni_degerler - eski_degerler
    
    degisiklik_var = False
    for fark in farklar:
        # İçinde sayı geçen (not olan) ve başlık olmayan satırları bildir
        if any(c.isdigit() for c in fark) and "Ders Adı" not in fark:
            print(f"🔔 Fark tespit edildi: {fark}")
            telegram_gonder(f"📢 NOT GÜNCELLEMESİ!\n\n{fark}")
            degisiklik_var = True
            
    return degisiklik_var

def main():
    chrome_options = Options()
    # Bot olduğunu gizleyen kritik ayar
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yeni_notlar = {}

    try:
        # 1. Sisteme Gir
        print("🌍 UBYS açılıyor...")
        driver.get(UBYS_URL)
        wait = WebDriverWait(driver, 40)
        wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_KULLANICI_ADI))).send_keys(OGRENCI_NO)
        driver.find_element(By.XPATH, XPATH_SIFRE).send_keys(SIFRE)
        driver.find_element(By.XPATH, XPATH_GIRIS_BUTONU).click()
        print("✅ Giriş yapıldı.")
        time.sleep(10)

        # 2. Derslerim'e Git
        driver.get("https://ubys.kastamonu.edu.tr/AIS/Student/Home/Index")
        time.sleep(5)
        
        print(f"📍 Başlangıç URL: {driver.current_url}")
        
        try:
            derslerim_box = driver.find_element(By.XPATH, "//*[contains(text(), 'Derslerim')]")
            driver.execute_script("arguments[0].click();", derslerim_box)
            print("✅ 'Derslerim' kutusuna tıklandı.")
        except:
            print("⚠️ Kutu bulunamadı, manuel gidiliyor...")
            driver.get("https://ubys.kastamonu.edu.tr/AIS/Student/Class/Index")

        time.sleep(10)
        
        # Yeni sekme kontrolü
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            print(f"🔀 Yeni sekmeye geçildi.")

        # 3. Tabloyu Bul (Röntgen Modu)
        print("🔍 Tablo aranıyor...")
        html_kaynagi = ""

        for i in range(3):
            # A) Direkt Sayfada Ara
            tablolar = driver.find_elements(By.TAG_NAME, "table")
            dolu_tablolar = [t for t in tablolar if len(t.find_elements(By.TAG_NAME, "tr")) > 3]
            
            if dolu_tablolar:
                print(f"🎉 Tablo bulundu! (Deneme {i+1})")
                html_kaynagi = dolu_tablolar[0].get_attribute('outerHTML')
                break
            
            # B) Iframe içinde Ara
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if iframes:
                for frame in iframes:
                    try:
                        driver.switch_to.frame(frame)
                        tbl = driver.find_elements(By.TAG_NAME, "table")
                        if tbl and len(tbl[0].find_elements(By.TAG_NAME, "tr")) > 3:
                            html_kaynagi = tbl[0].get_attribute('outerHTML')
                            break
                        driver.switch_to.default_content()
                    except:
                        driver.switch_to.default_content()
                if html_kaynagi: break

            # C) Butona Basmayı Dene
            try:
                btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Geçmiş Dönem') or contains(text(), 'Derslerini Göster')]")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(5)
            except:
                time.sleep(3)

        # 4. Veriyi İşle
        if html_kaynagi:
            yeni_notlar = tablodan_notlari_cek(html_kaynagi)
            print(f"📊 {len(yeni_notlar)} satır veri çekildi.")
            eski_notlar = eski_notlari_yukle()
            
            if karsilastir_ve_bildir(eski_notlar, yeni_notlar):
                print("✅ Değişiklikler bildirildi.")
            else:
                print("💤 Değişiklik yok.")
        else:
            print("❌ HATA: Tablo bulunamadı.")

    except Exception as e:
        print(f"❌ Kritik Hata: {e}")
        telegram_gonder(f"⚠️ Bot hatası: {e}")
    finally:
        # Git hatası almamak için mutlaka kaydet
        if not os.path.exists(DOSYA_ADI) or yeni_notlar:
            yeni_notlari_kaydet(yeni_notlar)
        driver.quit()

if __name__ == "__main__":
    main()
