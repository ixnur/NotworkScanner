# NotworkScanner: Basit bir ağ tarayıcı

Bu Python programı, ağ üzerindeki cihazları taramak için kullanılır.
Kullanıcıya aşağıdaki seçenekleri sunar:

![Ekran Görüntüsü - 2023-12-28 04-21-33](https://github.com/ixnur/NotworkScanner/assets/131625021/241e2583-2a37-451d-8a7a-12503710342f)

![Ekran Görüntüsü - 2023-12-28 04-21-49](https://github.com/ixnur/NotworkScanner/assets/131625021/6664228a-9437-4733-8ddb-74eae38e2e9b)

![3](https://github.com/ixnur/NotworkScanner/assets/131625021/7ec10aab-67f6-4909-a90b-82857aec252b)

![Ekran Görüntüsü - 2023-12-28 04-29-11](https://github.com/ixnur/NotworkScanner/assets/131625021/16f002f5-d16d-481b-8afd-67334d06217c)

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

Proje, `pyarmor` kullanılarak şifrelendi. Projeyi çalıştırmak için şu adımları takip edin:

1. Python yüklü değilse [Python'u indirin ve yükleyin](https://www.python.org/downloads/).
2. Projeyi bilgisayarınıza indirin.
3. Terminal veya komut istemcisinde projenin bulunduğu dizine gidin.
4. Proje dizininde şu komutu çalıştırın:

   ```bash
   pyarmor_runtime main.py

# requirements.txt var indirmeyi unutmayın.
pip install -r requirements.txt

Not:
- Program, scapy ve tqdm kütüphanelerini kullanır. Yüklü değillerse önce yüklemeniz gerekebilir
## Programın doğru çalışması için root veya admin yetkilerine ihtiyaç duyabilir.

# ## Geliştirme Durumu

- **v1.0.0** (28 Aralık 2023)
  - İlk sürüm yayınlandı.
