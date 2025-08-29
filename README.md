# DNS Zone Transfer Script

This Python script performs DNS zone transfers (AXFR) to discover subdomains and DNS records for a target domain. It utilizes the `dnspython` library to query DNS servers and attempt zone transfers from specified authoritative nameservers.

---

## Features
- Accepts target domain via command-line argument (`-target`)
- Attempts zone transfer from specified nameservers
- Lists all subdomains and DNS records found during the transfer
- Easy to extend or modify for custom DNS enumeration tasks

---

## Requirements
- Python 3
- `dnspython` library

You can install the required library with:

```bash
pip install -r requirements.txt
```
or manually:

```bash
pip install dnspython
```
## Usage

Run the script with the target domain as a parameter:

```bash
chmod +x your_script
python3 your_script.py -target example.com
```
Replace your_script.py with your filename and example.com with the domain you want to enumerate.

## Note
This script was developed during the DNS Enumeration Using Python class on Hack The Box. It is intended for educational purposes and authorized testing environments only.

## Disclaimer
Always ensure you have permission to perform DNS enumeration or zone transfers on the target domain. Unauthorized testing may be illegal.

## License
This project is for educational purposes only.