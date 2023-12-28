# NotworkScanner: Basit bir ağ tarayıcı :customs:

![Notwork Scanner](https://github.com/ixnur/NotworkScanner/raw/main/notwork.png)

Bu Python programı, ağ üzerindeki cihazları taramak için kullanılır.
Kullanıcıya aşağıdaki seçenekleri sunar

# Kullanımı
1. Cihazları Tara: Ağdaki cihazları taramak için ARP istekleri gönderir.
2. Cihaz Listesini Göster: Tarama sonuçlarını listeleyerek bulunan cihazları gösterir.
3. Cihaz Bilgilerini Göster: Belirli bir cihazın detaylı bilgilerini gösterir.
q. Programdan Çık: Programı sonlandırır.
(sırası ile 1 enter 2 yapın listeler)


# Kullanım:
- Programı çalıştırdığınızda, bir menü görüntülenir.
- Menüden seçim yaparak istediğiniz işlemi gerçekleştirebilirsiniz.
- Ağ taraması sırasında bulunan cihazlar, IP adresi, MAC adresi, üretici ve hostname bilgileriyle birlikte listelenir.

## Projeyi Çalıştırma
1. Python yüklü değilse [Python'u indirin ve yükleyin](https://www.python.org/downloads/).
2. Projeyi bilgisayarınıza indirin.
3. Terminal veya komut istemcisinde projenin bulunduğu dizine gidin.
4. Proje dizininde şu komutu çalıştırın:

   ```bash
   pyton3 main.py

# requirements.txt var indirmeyi unutmayın.
pip install -r requirements.txt

Not:
- Program, scapy ve tqdm kütüphanelerini kullanır. Yüklü değillerse önce yüklemeniz gerekebilir
## Programın doğru çalışması için root veya admin yetkilerine ihtiyaç duyabilir.

# Geliştirme Durumu
- **v0.0.1** (28 Aralık 2023)
  - İlk sürüm yayınlandı.
