from scapy.all import *
import datetime
import time
import telebot;
from conf import api

bot = telebot.TeleBot(api)

# Список IP, которые сканируют
detected_ips = []

def detect_scan(packet):
    global detected_ips
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        
        if tcp_layer.flags in ("S", ""):
            #Флаг SYN указывает на начало попытки установить TCP-соединение (что может быть частью сканирования сети, как в случае с nmap).
            #Пустой флаг (NULL) может означать NULL-сканирование, которое часто используется для обхода фильтров.
            src_ip = packet[IP].src
            if src_ip not in detected_ips:
                print(f"[*] Обнаружен подозрительный запрос от: {src_ip} в {datetime.datetime.now()}")
                bot.send_message(HERE U NEED TO INSERT YOU'RE CAHT ID WITH UR BOT, f"[*] Обнаружен подозрительный запрос от: {src_ip} в {datetime.datetime.now()}")
                detected_ips.append([src_ip, datetime.datetime.now()])
                time.sleep(5)
print("Сканирование локальной сети на подозрительные запросы...")

try:
    #iface="wlx5c628b74f73b"
    #nmap -sS 192.168.1.0/24
    sniff(filter="tcp", prn=detect_scan, store=0)
except KeyboardInterrupt:
    print("\nПрограмма остановлена.")
        
