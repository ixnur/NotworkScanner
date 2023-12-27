from scapy.all import ARP, Ether, srp
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

        result = srp(packet, timeout=3, verbose=0)[0]

        self.devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]

    def print_device_list(self):
        print("\nBulunan Cihazlar:")
        print("IP Adres\t\tMAC Adres")
        print("-----------------------------------------")
        for device in self.devices:
            print(f"{device['ip']}\t\t{device['mac']}")

    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def display_menu(self):
        print("\nMekatronik.org Ağ Tarayıcıya Hoş Geldiniz!")
        print("1. Cihazları Tara")
        print("2. Cihaz Listesini Göster")
        print("3. Programdan Çık")
  
    def get_user_choice(self):
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
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçenek. Tekrar deneyin.")
                input("Devam etmek için Enter'a basın.")

if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.run()
