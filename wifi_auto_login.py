import subprocess
import time
import requests

WIFI_NAME = "ISM-Campus-Wi-Fi"  # <--- Institute Wi-Fi SSID(Make changes whenever needed)
USERNAME = "<youre_username_here>"                 # <--- Replace with your actual username
PASSWORD = "<youre_password_here>"              # <--- Replace with your actual password

LOGIN_URL = "https://wifilogin.iitism.ac.in/login"
payload = {
    "dst": "https://www.google.com",
    "popup": "true",
    "username": USERNAME,
    "password": PASSWORD
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://wifilogin.iitism.ac.in/login"
}


def get_current_wifi():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
        for line in result.splitlines():
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return None


def connect_to_wifi(ssid):
    print(f"[+] Connecting to {ssid}...")
    subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], capture_output=True)
    for i in range(15):  
        time.sleep(0.5)
        current = get_current_wifi()
        if current == ssid:
            break



def login_portal():
    print("[+] Sending login request...")
    try:
        response = requests.post(LOGIN_URL, data=payload, headers=headers, timeout=5)
        if response.status_code == 200:
            print("[+] Login request sent successfully.")
        else:
            print(f"[!] Unexpected response. Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error during login: {e}")


def main():
    current = get_current_wifi()
    if current != WIFI_NAME:
        print(f"[!] Currently connected to: {current}")
        connect_to_wifi(WIFI_NAME)
        new_wifi = get_current_wifi()
        if new_wifi != WIFI_NAME:
            print("[!] Failed to connect to desired Wi-Fi.")
            return
        else:
            print(f"[+] Successfully connected to {WIFI_NAME}")
    else:
        print(f"[+] Already connected to {WIFI_NAME}")

    login_portal()


if __name__ == "__main__":
    main()
