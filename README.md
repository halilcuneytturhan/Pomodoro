# 🍅 Kral Pomodoro & Odaklanma Zamanlayıcısı

Modern, kesintisiz ve tamamen özelleştirilebilir bir Pomodoro (Odaklanma) uygulaması. Python ve Streamlit kullanılarak geliştirilmiş olup, arka planda gelişmiş bir "Durum Makinesi" (State Machine) mimarisi barındırır.

## ✨ Öne Çıkan Özellikler

* **Kesintisiz Deneyim (Flicker-Free):** Streamlit'in yeni `@st.fragment` mimarisi sayesinde saniye güncellemelerinde sayfa yenilenmez, ekran titremez.
* **Akıllı Durum Yönetimi:** `st.session_state` ile Ders ve Mola modları arasında akıllı geçiş yapar.
* **Dinamik UI/UX:** Modlara göre (Odaklanma / Mola) sayacın rengi, yazıları ve tasarımı otomatik değişir (Neon Yeşil ve Neon Mavi).
* **Hazır Paketler:** Tek tıkla 20 Dk Başlangıç, 25 Dk İdeal veya 15/30 Dk Uzun Mola setleri.
* **Tam Kontrol:** Başlat, Duraklat ve Sıfırla özellikleriyle süreyi anlık olarak yönetme imkanı.
* **CSS Enjeksiyonu:** Standart Streamlit arayüzünün dışına çıkılmış, HTML ve CSS gömülerek devasa ve şık bir dijital saat görünümü elde edilmiştir.

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Gerekli kütüphaneleri indirin:**
Projeyi çalıştırmak için bilgisayarınızda Python yüklü olmalıdır. Terminali açın ve şu komutu yazın:
```bash
pip install streamlit
