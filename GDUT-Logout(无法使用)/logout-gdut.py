# 目前无法使用，由于我太菜了，还未找到原因！

import requests
import socket

def get_local_ip():
    """获取本地IP地址"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = None
    finally:
        s.close()
    return ip

# def load_account_password(filename):
#     """从外部文本文件加载账户密码"""
#     with open(filename, 'r') as file:
#         user_account, user_password = file.readline().strip().split(',')
#     return user_account, user_password

def generate_logout_url(ip, user_account, user_password, callback="dr1002", login_method="1", ac_logout="1", register_mode="1", wlan_user_ipv6="", wlan_vlan_id="1", wlan_user_mac="000000000000", wlan_ac_ip="", wlan_ac_name="", js_version="4.1.3", v="1150", lang="zh"):
    """执行注销校园网登录"""
    url = "http://10.0.3.2:801/eportal/portal/logout"
    params = {
        "callback": callback,
        "login_method": login_method,
        "user_account": user_account,
        "user_password": user_password,
        "ac_logout": ac_logout,
        "register_mode": register_mode,
        "wlan_user_ip": ip,
        "wlan_user_ipv6": wlan_user_ipv6,
        "wlan_vlan_id": wlan_vlan_id,
        "wlan_user_mac": wlan_user_mac,
        "wlan_ac_ip": wlan_ac_ip,
        "wlan_ac_name": wlan_ac_name,
        "jsVersion": js_version,
        "v": v,
        "lang": lang
    }
    response = requests.get(url, params=params)
    return response.status_code, response.text

if __name__ == "__main__":
    # 用于退出登录校园网账户信息
    user_account = "drcom"
    user_password = "123"
    
    # filename = "gdut.txt"
    # user_account, user_password = load_account_password(filename)

    # 获取本地IP地址
    ip = get_local_ip
    
    if ip:
        status_code, response_text = generate_logout_url(ip, user_account, user_password)
        print(f"Status Code: {status_code}")
        print(f"Response Text: {response_text}")
    else:
        print("无法获取本地IP地址")

