import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    networks = ifaces.scan_results()
    security_levels = {const.AKM_TYPE_NONE: "Open", const.AKM_TYPE_WPA: "WPA", const.AKM_TYPE_WPAPSK: "WPA-PSK", const.AKM_TYPE_WPA2: "WPA2",
                       const.AKM_TYPE_WPA2PSK: "WPA2-PSK", const.AKM_TYPE_UNKNOWN: "Unknown / Other"}
    #No WPA3 support in pywyfi atm?
    #const.AKM_TYPE_WPA3: "WPA3",
    with open('wifi_networks.txt', 'w') as f:
        for network in networks:
            security = security_levels.get(network.akm[0])
            f.write(
                f"SSID: {network.ssid} | BSSID: {network.bssid} | Security: {security}  | Signal Quality: {network.signal} \n")


scan_wifi()