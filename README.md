---

# 📡 **WiFi Scanner (ARP Network Scanner)**  

This is a simple **WiFi Scanner** built using Python and **Scapy**. It sends **ARP requests** to identify active devices on a network, helping users discover connected devices on a local subnet.  

## ⚡ **Features**  
✅ Scan a network for connected devices  
✅ Displays active IP and MAC addresses  
✅ Uses **Scapy** for ARP request handling  
✅ Simple and user-friendly interface  

## 📌 **Installation & Setup**  
This script requires **Python 3** and **Scapy**.  

### 🔹 **For Linux (Kali, Ubuntu, Debian-based systems)**  
```bash
sudo apt install python3-pip
pip install scapy
```
### 🔹 **For Windows**  
1. Install **Npcap** from [nmap.org/npcap](https://nmap.org/npcap/) (required for Scapy).  
2. Install the required Python module:  
   ```bash
   pip install scapy
   ```

## 🚀 **How to Use**  
1. Run the script:  
   ```bash
   python3 wifi_scanner.py
   ```
2. Enter the target **IP address range** in CIDR notation (e.g., `192.168.1.0/24`).  
3. The script will send ARP requests and display the **active devices** on the network.  

Here's the corrected **Example Output** section for your **README.md** file, matching your actual output format:  

## 📌 **Example Output**  
```
Please enter the IP address and range that you want to send the ARP request to (ex 192.168.1.0/24): 192.168.0.0/24
192.168.0.0/24 is a valid IP address range

Begin emission
***
Finished sending 256 packets

Received 3 packets, got 3 answers, remaining 253 packets

SRC                 MANUF      PSRC
48:22:54:b5:ef:ea  TPLink     192.168.0.1
e6:58:f9:d9:f0:4c  unknown    192.168.0.101
06:cf:67:5e:ab:1a  unknown    192.168.0.103
```

## ⚠️ **Disclaimer**  
This tool is intended for **educational and ethical** purposes only. Unauthorized network scanning without permission is **illegal** and may result in legal consequences. Always obtain proper authorization before scanning any network.  

## 🤝 **Connect with Me**  
🔗 **GitHub**: [RaianKibriaRohan](https://github.com/RaianKibriaRohan)  
🔗 **LinkedIn**: [Raian Kibria Rohan](https://www.linkedin.com/in/raian-kibria-rohan-89997a323/)  

---
