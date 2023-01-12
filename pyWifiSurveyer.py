import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    networks = ifaces.scan_results()
    with open('wifi_networks.txt', 'w') as f:
        for network in networks:
            f.write(
                f"SSID: {network.ssid} | BSSID: {network.bssid} | Signal Quality: {network.signal} \n")


scan_wifi()