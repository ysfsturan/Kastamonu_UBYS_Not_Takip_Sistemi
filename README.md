# 🏫 Kastamonu UBYS Grade Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)

</div>

---

### 🇹🇷 Proje Hakkında (About)

Bu proje, Kastamonu Üniversitesi UBYS (Üniversite Bilgi Yönetim Sistemi) üzerindeki notları manuel olarak kontrol etme zahmetini ortadan kaldırmak için geliştirilmiş bir **otomasyon aracıdır.**

Proje, **GitHub Actions** altyapısını kullanarak "Serverless" (Sunucusuz) bir mantıkla çalışır. Belirlenen periyotlarda (Cron Job) tetiklenen Python betiği, **Selenium WebDriver** kullanarak sisteme giriş yapar, güncel not verilerini çeker ve yerel veritabanı (JSON) ile karşılaştırır. Herhangi bir değişiklik tespit edildiğinde **Telegram API** üzerinden kullanıcıya anlık `push` bildirimi gönderir.

### 🇺🇸 Project Overview

This is an open-source automation tool designed to streamline the grade-checking process for Kastamonu University students.

Running on **GitHub Actions** as a scheduled workflow, the bot utilizes **Selenium WebDriver** to authenticate and scrape grade data from the UBYS portal. It implements a logic to compare fetched data with the previous state. Upon detecting any updates or new entries, it triggers an instant notification via the **Telegram API**.

---

## ⚙️ Teknik Detaylar / Tech Specs

| Teknoloji (Tech) | Kullanım Amacı (Usage) |
| :--- | :--- |
| **Python 3.9** | Core scripting ve veri işleme. |
| **Selenium** | Headless Chrome tarayıcısı ile DOM manipülasyonu ve veri kazıma (Scraping). |
| **GitHub Actions** | Scriptin bulut sunucularda periyodik olarak çalıştırılması (CI/CD). |
| **Telegram Bot API** | Kullanıcıya asenkron bildirim gönderimi. |
| **JSON** | Veri kalıcılığı ve değişiklik takibi (Diff Checking). |

---

## 🛠️ Kurulum ve Dağıtım (Setup & Deployment)

Bu projeyi kendi GitHub hesabınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 1. Repoyu Forklayın
Sağ üstteki **"Fork"** butonunu kullanarak projeyi kendi hesabınıza kopyalayın.

### 2. Telegram Bot Yapılandırması
1.  **[@BotFather](https://t.me/BotFather)** üzerinden yeni bir bot oluşturun.
2.  Size verilen **API Token** bilgisini not edin.
3.  Kendi Chat ID'nizi öğrenmek için botunuza mesaj atıp `https://api.telegram.org/bot<TOKEN>/getUpdates` adresini kontrol edin.

### 3. Environment Variables (Sırlar)
Projenin çalışabilmesi için hassas verilerinizi (Credentials) GitHub Secrets alanına eklemeniz gerekmektedir.
`Settings` > `Secrets and variables` > `Actions` > `New repository secret` yolunu izleyin:

| Secret Key | Açıklama |
| :--- | :--- |
| `OGRENCI_NO` | Okul numaranız. |
| `SIFRE` | UBYS giriş şifreniz. |
| `BOT_TOKEN` | Telegram Bot Token. |
| `CHAT_ID` | Telegram Chat ID. |

### 4. Workflow'u Tetikleyin
**Actions** sekmesine gidin, sol menüden `UBYS Not Takip Botu` iş akışını seçin ve **Run workflow** butonu ile servisi başlatın. Bot artık her 30 dakikada bir çalışacaktır.

---

## ⚠️ Yasal Uyarı / Disclaimer

Bu yazılım tamamen **eğitim amaçlı** ve kişisel kullanım için geliştirilmiştir. Kastamonu Üniversitesi Bilgi İşlem Daire Başkanlığı ile resmi bir bağlantısı yoktur. Sisteme zarar vermez (Sadece Read-Only işlem yapar). Kullanım sorumluluğu kullanıcıya aittir.

---

<div align="center">

Made with ❤️ by [Yusuf Sami Turan](https://github.com/ysfsturan)

</div>
