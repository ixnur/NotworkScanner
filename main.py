
from scapy.all import ARP, Ether, srp
from tqdm import tqdm  # tqdm'yi ekledik
import platform
import os
import netifaces

class NetworkScanner:
    def __init__(self):
        self.devices = []

    def get_local_ip(self):
        try:
            ip = netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_INET][0]['addr']
            return ip
        except (OSError, KeyError):
            return None

    def discover_devices(self, ip_range):
        arp_request = ARP(pdst=ip_range)
        ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether_frame / arp_request

        result, unanswered = srp(packet, timeout=3, verbose=0)
        for sent, received in tqdm(result, desc="Taranıyor", unit="Cihaz"):
            self.devices.append({'ip': received.psrc,
                                 'mac': received.hwsrc,
                                 'vendor': self.get_vendor(received.hwsrc),
                                 'hostname': self.get_hostname(received.psrc)})

    def get_vendor(self, mac_address):
        return ''  # Üretici bilgisini almak için gerekli işlemleri ekleyin.

    def get_hostname(self, ip_address):
        return ''  # Hostname bilgisini almak için gerekli işlemleri ekleyin.

    def print_device_list(self):
        print(f"\nBulunan Cihazlar:")
        print(f"IP Adres\t\tMAC Adres\t\tÜretici\t\tHostname")
        print(f"---------------------------------------------------------------")
        for device in self.devices:
            print(f"{device['ip']}\t\t{device['mac']}\t\t{device['vendor']}\t\t{device['hostname']}")

    def show_device_details(self):
        if not self.devices:
            print(f"Önce cihazları taramanız gerekiyor.")
            return

        ip_to_check = input(f"Bilgilerini görmek istediğiniz cihazın IP adresini girin: ")
        found_device = next((device for device in self.devices if device['ip'] == ip_to_check), None)

        if found_device:
            print(f"\nCihaz Bilgileri:")
            print(f"IP Adres: {found_device['ip']}")
            print(f"MAC Adres: {found_device['mac']}")
            print(f"Üretici: {found_device['vendor']}")
            print(f"Hostname: {found_device['hostname']}")
        else:
            print(f"{ip_to_check} IP adresine sahip bir cihaz bulunamadı.")

    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def display_menu(self):
        print("""
              
 _ __                         __,                           
( /  )   _/_              /  (                              
 /  / __ /  , , , __ _   /<   `.  _, __,  _ _   _ _   _  _  
/  (_(_)(__(_(_/_(_)/ (_/ |_(___)(__(_/(_/ / /_/ / /_(/_/ (_  
              
               """)
        print(f"@ixnur/NotworkScanner")
        print("---------------------------")
        print("1. Cihazları Tara")
        print("2. Cihaz Listesini Göster")
        print("3. Cihaz Bilgilerini Göster")
        print("---------------------------")
        print(f"Q. Programdan Çık")
        print("---------------------------")

    def get_user_choice(self):
        print(f"Ağdaki cihazlar için sırası ile '1' - 'enter' - '2' ")
        print("ip no ile detay için 3")
        choice = input("Seçiminizi yapın (1-3): ")
        return choice

    def run(self):
        while True:
            self.clear_screen()
            self.display_menu()

            choice = self.get_user_choice()

            if choice == '1':
                local_ip = self.get_local_ip()
                if local_ip:
                    ip_range = local_ip.rsplit('.', 1)[0] + ".1/24"
                    self.discover_devices(ip_range)
                    input("Tarama tamamlandı. Devam etmek için Enter'a basın.")
                else:
                    print("Bağlı olduğunuz ağ adaptörünün IP adresi bulunamadı.")
                    input("Devam etmek için Enter'a basın.")
            elif choice == '2':
                self.clear_screen()
                self.print_device_list()
                input("Devam etmek için Enter'a basın.")
            elif choice == '3':
                self.clear_screen()
                self.show_device_details()
                input("Devam etmek için Enter'a basın.")
            elif choice.lower() == 'q':
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçenek. Tekrar deneyin.")
                input("Devam etmek için Enter'a basın.")

if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.run()
