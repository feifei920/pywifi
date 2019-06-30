import pywifi
from pywifi import const


def bies():
    wifi = pywifi.PyWiFi()    #扫描附近的wifi
    ifaces = wifi.interfaces()[0]     #获取无线网卡
    ifaces.scan()     #扫描WiFi
    bessis = ifaces.scan_results()   #获取扫描结果
    for data in bessis:
        print(data.ssid)   #wifi的名称


if __name__ == "__main__":
    bies()