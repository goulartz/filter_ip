import re

f_ips = "STRING WITH IPS"

ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

ips = ip_pattern.findall(f_ips)

print("Found IPs:", ips)
