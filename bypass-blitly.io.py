# Nhập thư viện (nếu thiếu thì dùng lệnh pip install + tên thư viện)
import json
import requests
from bs4 import BeautifulSoup
import re

# Đặt tên biến
URL = input("Hãy nhập địa chỉ của Link Rút Gọn có tên miền: https://blitly.io/...\nNhập ở đây: ")
response = requests.get(URL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
scripts = soup.find_all("script")

# Clear old data
url = None

# Thuật cmn toán được Support bởi ChatGPT =)))
for script in scripts:
    if script.string is not None and 'url' in script.string:
        pattern = r'url:"(.*?)"'
        match = re.search(pattern, script.string)
        
        if match: # Nếu tin chuẩn thì...
            url = match.group(1)
            updated_url1 = url.replace("u002F", "/")
            updated_url2 = updated_url1.replace("\/", "/")
            print("Địa chỉ Link gốc:" ,updated_url2)
            break

if not url: # Nếu tin đéo chuẩn thì...
    print("E: Hệ thống Bypass đã bị lỗi hoặc có vấn đề với tên miền, vui lòng thử lại hoặc liên hệ Coder!")