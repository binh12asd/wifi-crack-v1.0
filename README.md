# 🔥 EROOTG WIFI HACKING TOOL – ULTIMATE EDITION v9.0

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Android%20%7C%20iOS-lightgrey?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-9.0-red?style=for-the-badge">
</p>

<p align="center">
  <b>Công cụ kiểm tra bảo mật WiFi mạnh mẽ, được phát triển bởi EROOTG</b><br>
  <i>Chỉ dùng cho mục đích học tập và nghiên cứu bảo mật</i>
</p>

<p align="center">
  <img src="screenshot.png" width="600" alt="Tool Screenshot">
</p>

---

## ⚠️ **TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM**

> **CÔNG CỤ NÀY CHỈ ĐƯỢC SỬ DỤNG CHO MỤC ĐÍCH GIÁO DỤC VÀ KIỂM TRA BẢO MẬT CỦA CHÍNH BẠN HOẶC KHI CÓ SỰ CHO PHÉP RÕ RÀNG.**
>
> **Tác giả không chịu bất kỳ trách nhiệm nào đối với việc sử dụng công cụ này cho các hoạt động bất hợp pháp. Việc xâm nhập trái phép vào mạng không phải của bạn là vi phạm pháp luật ở hầu hết các quốc gia.**

---

## 🚀 **GIỚI THIỆU**

**EROOTG WiFi Hacking Tool** là công cụ dòng lệnh mạnh mẽ được phát triển để kiểm tra bảo mật mạng WiFi. Tool hỗ trợ nhiều kỹ thuật tấn công và kiểm tra phổ biến:

- 📡 Quét và phát hiện mạng WiFi xung quanh
- 🔑 Bắt handshake WPA/WPA2
- ⚡ Bắt PMKID (tấn công WPA3/WPA2 không cần client)
- 💥 Tấn công ngắt kết nối (Deauth Attack)
- 🎯 Tấn công WPS (Reaver/Bully)
- ✨ Tấn công Pixie Dust (lỗ hổng WPS)
- 🔓 Crack mật khẩu với wordlist
- 🖥️ Crack nhanh với GPU (Hashcat)
- 📝 Tạo wordlist thông minh
- 👿 Tạo Evil Twin AP
- 🔨 Tấn công nâng cao với MDK4
- 🤖 Tự động tấn công (Auto Attack)

---

## 📥 **CÀI ĐẶT**

### **1. Tải Tool**

```bash
# Clone repository (khuyến nghị)
git clone https://github.com/binh12asd/wifi-crack-v1.0.git
cd wifi-crack-v1.0

# Hoặc tải trực tiếp file main.py
wget https://raw.githubusercontent.com/binh12asd/wifi-crack-v1.0/main/main.py
2. Cài Đặt Trên PC (Linux)
Yêu cầu hệ thống
Hệ điều hành: Kali Linux, Parrot OS, Ubuntu 20.04+

Quyền root (sudo)

Card WiFi hỗ trợ monitor mode (khuyến nghị chipset Atheros, Ralink, Realtek)

Các bước cài đặt
Bước 1: Cập nhật hệ thống

bash
sudo apt update && sudo apt upgrade -y
Bước 2: Cài đặt Python và pip

bash
sudo apt install python3 python3-pip -y
Bước 3: Cài đặt các công cụ cần thiết

bash
sudo apt install aircrack-ng hashcat hcxtools reaver bully mdk4 hostapd dnsmasq tcpdump -y
Bước 4: Cài đặt thư viện Python

bash
pip3 install scapy netifaces
Bước 5: Cấp quyền chạy cho script

bash
chmod +x main.py
Bước 6: Chạy tool

bash
sudo python3 main.py
Lưu ý: Luôn chạy với sudo để có đủ quyền thao tác với card mạng.

3. Cài Đặt Trên Termux (Android)
Yêu cầu
Android 7+

Termux từ F-Droid (không dùng bản trên Play Store)

Điện thoại đã root (khuyến nghị) hoặc ít nhất có hỗ trợ monitor mode

Các bước cài đặt
Bước 1: Cài Termux từ F-Droid

Tải F-Droid: https://f-droid.org

Tìm và cài đặt Termux

Bước 2: Cập nhật gói

bash
pkg update && pkg upgrade -y
Bước 3: Cài đặt Python và git

bash
pkg install python git -y
Bước 4: Cài đặt các công cụ WiFi (nếu có hỗ trợ)

bash
pkg install root-repo
pkg install aircrack-ng -y
Bước 5: Clone tool

bash
git clone https://github.com/binh12asd/wifi-crack-v1.0.git
cd wifi-crack-v1.0
Bước 6: Cài thư viện Python

bash
pip install scapy netifaces
Bước 7: Chạy tool

bash
python main.py
⚠️ Lưu ý quan trọng:

Trên Android không root, các tính năng như monitor mode, deauth, WPS,... sẽ không hoạt động.

Bạn chỉ có thể dùng các tính năng nhẹ như quét mạng cơ bản.

Để có đầy đủ tính năng, cần root và card WiFi hỗ trợ monitor mode.

4. Cài Đặt Trên iSH (iOS)
Yêu cầu
iPhone/iPad

Ứng dụng iSH Shell từ App Store

Các bước cài đặt
Bước 1: Cài iSH từ App Store

Mở App Store, tìm iSH Shell, tải về và cài đặt.

Bước 2: Mở iSH và cập nhật gói

bash
apk update
apk upgrade
Bước 3: Cài đặt Python và git

bash
apk add python3 py3-pip git
Bước 4: Clone tool

bash
git clone https://github.com/binh12asd/wifi-crack-v1.0.git
cd wifi-crack-v1.0
Bước 5: Cài thư viện Python

bash
pip3 install scapy netifaces
Bước 6: Chạy tool

bash
python3 main.py
⚠️ Lưu ý quan trọng:

iSH là giả lập Linux, không thể điều khiển trực tiếp phần cứng WiFi của iPhone.

Các chức năng tấn công sẽ không hoạt động.

Bạn chỉ có thể dùng để học code Python, thực hành các lệnh cơ bản, hoặc quét mạng (nếu có thư viện hỗ trợ).

🎯 HƯỚNG DẪN SỬ DỤNG
Chạy tool
bash
# Trên Linux
sudo python3 main.py

# Trên Termux / iSH
python3 main.py
Menu chính
Khi chạy tool, bạn sẽ thấy menu với các tùy chọn:

text
╔════════════════════════════════════════════════════════════════╗
║                         MENU CHÍNH                             ║
╠════════════════════════════════════════════════════════════════╣
║  [01] SCAN MẠNG         [07] CRACK WORDLIST        [13] STATS ║
║  [02] BẮT HANDSHAKE     [08] HASHCAT               [14] KẾT QUẢ║
║  [03] BẮT PMKID         [09] TẠO WORDLIST          [15] MONITOR║
║  [04] DEAUTH ATTACK     [10] EVIL TWIN             [16] EXIT   ║
║  [05] WPS ATTACK        [11] MDK4                             ║
║  [06] PIXIE DUST        [12] AUTO ATTACK                      ║
╚════════════════════════════════════════════════════════════════╝
Các bước cơ bản
Bật monitor mode (chọn 15) → chọn interface WiFi

Scan mạng (chọn 01) → nhập thời gian quét

Chọn mục tiêu từ danh sách

Thực hiện tấn công phù hợp (bắt handshake, WPS, deauth,...)

Crack mật khẩu với wordlist (chọn 07 hoặc 08)

📊 CÁC TÍNH NĂNG CHI TIẾT
STT	Chức năng	Mô tả
01	SCAN MẠNG	Quét các mạng WiFi xung quanh, hiển thị BSSID, ESSID, kênh, tín hiệu, mã hóa
02	BẮT HANDSHAKE	Bắt handshake WPA/WPA2, tự động deauth để ép client reconnect
03	BẮT PMKID	Bắt PMKID (WPA3/WPA2) – không cần client
04	DEAUTH ATTACK	Ngắt kết nối client khỏi AP
05	WPS ATTACK	Tấn công WPS bằng bully/reaver
06	PIXIE DUST	Tấn công lỗ hổng WPS Pixie Dust
07	CRACK WORDLIST	Crack handshake/PMKID với wordlist
08	HASHCAT	Crack nhanh với GPU (hashcat)
09	TẠO WORDLIST	Tạo wordlist thông minh dựa trên ESSID/BSSID
10	EVIL TWIN	Tạo AP giả mạo để bắt handshake
11	MDK4	Tấn công nâng cao với mdk4
12	AUTO ATTACK	Tự động thử tất cả phương pháp
13	STATS	Xem thống kê chi tiết
14	KẾT QUẢ	Xem mật khẩu đã crack
15	MONITOR	Bật/tắt monitor mode
⚙️ CẤU HÌNH VÀ KIỂM TRA
Kiểm tra card WiFi hỗ trợ monitor mode
bash
iw list | grep -A 8 "Supported interface modes"
Kiểm tra interface WiFi
bash
iwconfig
ip a
Nếu không có airmon-ng
bash
sudo apt install aircrack-ng        # Linux
pkg install aircrack-ng              # Termux (root)
Stop các tiến trình gây nhiễu
bash
sudo airmon-ng check kill
🐞 XỬ LÝ LỖI THƯỜNG GẶP
Lỗi No module named 'scapy'
bash
pip3 install scapy          # Linux
pip install scapy           # Termux
pip3 install scapy          # iSH
Lỗi Permission denied
bash
# Luôn chạy với quyền root trên Linux
sudo python3 main.py
Lỗi Interface not found
bash
# Kiểm tra lại tên interface
iwconfig
ip a
# Sửa trong code nếu cần
Lỗi monitor mode không bật được
bash
# Thử các lệnh sau
sudo airmon-ng check kill
sudo airmon-ng start wlan0    # thay wlan0 bằng interface của bạn
sudo ip link set wlan0 down && sudo iw dev wlan0 set type monitor && sudo ip link set wlan0 up
📸 ẢNH CHỤP MÀN HÌNH
<p align="center"> <img src="screenshot.png" width="600" alt="Tool Demo"> <br> <i>Giao diện chính của tool</i> </p>
(Lưu ý: Bạn cần tự chụp ảnh màn hình và upload file screenshot.png lên repo)

🤝 ĐÓNG GÓP
Mọi đóng góp đều được chào đón! Nếu bạn muốn cải thiện tool:

Fork repository

Tạo branch mới (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Mở Pull Request

📞 LIÊN HỆ & HỖ TRỢ
GitHub Issues: https://github.com/binh12asd/wifi-crack-v1.0/issues

Telegram: t.me/erootg

Discord: Đang cập nhật

Tool được phát triển bởi EROOTG – Dành cho cộng đồng hacker, pentester và những người đam mê bảo mật.

📜 GIẤY PHÉP
Dự án này được phân phối dưới giấy phép MIT. Xem file LICENSE để biết thêm chi tiết.

⭐ ỦNG HỘ
Nếu bạn thấy tool hữu ích, hãy Star ⭐ repository này để ủng hộ tác giả!

<p align="center"> <b>🔥 HAPPY HACKING – ONLY FOR EDUCATION! 🔥</b> </p><p align="center"> <sub>Copyright © 2026 EROOTG. All rights reserved.</sub> </p> ```