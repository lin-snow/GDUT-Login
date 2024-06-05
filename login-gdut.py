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

def load_account_password(filename):
    """从外部文本文件加载账户密码"""
    with open(filename, 'r') as file:
        user_account, user_password = file.readline().strip().split(',')
    return user_account, user_password

def generate_login_url(ip, user_account, user_password, wlan_ac_ip, callback="dr1004", login_method="1", wlan_user_ipv6="", wlan_user_mac="000000000000", wlan_ac_name="", js_version="4.1.3", terminal_type="2", lang="zh-cn", v="2041"):
    """生成登录URL并发起请求"""
    url = "http://10.0.3.2:801/eportal/portal/login"
    params = {
        "callback": callback,
        "login_method": login_method,
        "user_account": user_account,
        "user_password": user_password,
        "wlan_user_ip": ip,
        "wlan_user_ipv6": wlan_user_ipv6,
        "wlan_user_mac": wlan_user_mac,
        "wlan_ac_ip": wlan_ac_ip,
        "wlan_ac_name": wlan_ac_name,
        "jsVersion": js_version,
        "terminal_type": terminal_type,
        "lang": lang,
        "v": v,
        "lang": lang
    }
    response = requests.get(url, params=params)
    return response.status_code, response.text

if __name__ == "__main__":
    # 从外部文本文件加载账户密码
    filename = "gdut.txt"
    user_account, user_password = load_account_password(filename)
    wlan_ac_ip = "172.16.254.2"

    # 获取本地IP地址
    ip = get_local_ip()
    
    if ip:
        status_code, response_text = generate_login_url(ip, user_account, user_password, wlan_ac_ip)
        print(f"Status Code: {status_code}")
        print(f"Response Text: {response_text}")
    else:
        print("无法获取本地IP地址")

