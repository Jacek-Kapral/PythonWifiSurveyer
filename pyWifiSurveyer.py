import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    networks = ifaces.scan_results()
    for network in networks:
        print(network.ssid)

scan_wifi()