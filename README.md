# 🏫 Kastamonu UBYS Not Takip Sistemi
### (Kastamonu UBYS Grade Tracker)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Cloud-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Notifications-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)

</div>

---

### 🇹🇷 Türkçe (Turkish)

**Kastamonu Üniversitesi** öğrencileri için geliştirilmiş, **7/24 çalışan** otomatik not takip sistemi.

Siz uyurken veya gezerken bu bot GitHub sunucularında (Cloud) çalışır, UBYS'ye girer ve notlarınızı kontrol eder. Eğer yeni bir not girilmişse veya hocanız var olan bir notu güncellemişse **anında telefonunuza Telegram bildirimi** gönderir.

**Bilgisayarınızı açık tutmanıza gerek YOKTUR!** Kurulumu yaptıktan sonra tamamen bulut tabanlı çalışır.

### 🇺🇸 English

An automated grade tracking system designed for **Kastamonu University** students that runs **24/7**.

While you sleep or travel, this bot runs on GitHub servers, logs into the UBYS portal, and checks your grades. If a new grade is announced or updated, it sends an **instant Telegram notification** to your phone.

**You do NOT need to keep your computer on!** Once set up, it runs entirely on the cloud.

---

## 🌟 Özellikler / Features

| Özellik (Feature) | Açıklama (Description) |
| :--- | :--- |
| **☁️ Cloud-Native** | GitHub Actions üzerinde çalışır. Telefonunuzdan yönetebilirsiniz. (Runs on GitHub Actions.) |
| **🚀 Anlık Bildirim** | Not girildiği saniye Telegram'dan mesaj gelir. (Instant Telegram alerts.) |
| **🧠 Akıllı Takip** | Sadece *yeni* veya *değişen* notları bildirir. Spam yapmaz. (Only notifies on changes.) |
| **🔒 %100 Güvenli** | Şifreleriniz GitHub'ın "Secrets" kasasında şifreli saklanır. Kimse göremez. (Credentials are encrypted.) |
| **🕵️ Hayalet Mod** | Gelişmiş "Anti-Bot" korumasını aşar, gerçek insan gibi davranır. (Bypasses bot detection.) |

---

## 🛠️ Kurulum Rehberi (5 Dakikada Hazır)

Kod bilmenize gerek yok! Aşağıdaki adımları sırasıyla yapın.

### Adım 1: Projeyi Kopyalayın (Fork)
Bu sayfanın sağ üst köşesindeki **"Fork"** butonuna basın ve `Create fork` diyerek projeyi kendi hesabınıza kopyalayın.

### Adım 2: Telegram Botu Ayarlayın
1.  Telegram'da **[@BotFather](https://t.me/BotFather)** kullanıcısını bulun.
2.  `/newbot` yazın ve botunuza bir isim verin.
3.  Size vereceği **HTTP API Token**'ı kopyalayın.
4.  Oluşturduğunuz bota Telegram'dan bir "Selam" mesajı atın.
5.  Tarayıcınızdan `https://api.telegram.org/bot<TOKEN_BURAYA>/getUpdates` adresine gidin.
6.  Çıkan yazılarda `"chat":{"id":123456...` kısmındaki numarayı (Chat ID) alın.

### Adım 3: Şifreleri Ekleyin (Secrets)
Kendi GitHub sayfanızda kopyaladığınız projeye gidin:
1.  Üstten **Settings** (Ayarlar) sekmesine tıklayın.
2.  Soldaki menüden **Secrets and variables** > **Actions** kısmına girin.
3.  **New repository secret** butonuna basarak şu 4 bilgiyi ekleyin:

| Name (İsim) | Value (Değer) | Açıklama |
| :--- | :--- | :--- |
| `OGRENCI_NO` | `245xxxxxx` | Öğrenci Numaranız |
| `SIFRE` | `Sifreniz123` | UBYS Giriş Şifreniz |
| `BOT_TOKEN` | `12345:AAH...` | BotFather'dan aldığınız Token |
| `CHAT_ID` | `12345678` | Kendi Chat ID numaranız |

### Adım 4: Botu Başlatın!
1.  Üst menüden **Actions** sekmesine gidin.
2.  Sol tarafta **"UBYS Not Takip Botu"** yazısını göreceksiniz, ona tıklayın.
3.  Sağ tarafta **Run workflow** butonuna basın ve yeşil butona tıklayın.

🎉 **Tebrikler!** Botunuz aktif edildi. Artık her 30 dakikada bir notlarınızı kontrol edecek.

---

## ⚠️ Yasal Uyarı / Disclaimer

**[TR]** Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir. Kastamonu Üniversitesi Bilgi İşlem Daire Başkanlığı ile resmi bir bağı yoktur. Sisteme zarar vermez (sadece okuma yapar), ancak kullanım sorumluluğu tamamen kullanıcıya aittir.

**[EN]** This project is open-source and developed for educational purposes. It is not officially affiliated with Kastamonu University. Use at your own risk.

---

## 🤝 İletişim & Destek (Support)

Bir sorun yaşarsanız veya geliştirmek isterseniz:
* **Developer:** [Yusuf Sami Turan](https://github.com/ysfsturan)
* **Issues:** Hata bildirimi için "Issues" sekmesini kullanabilirsiniz.
