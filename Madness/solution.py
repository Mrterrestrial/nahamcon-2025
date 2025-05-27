#!/usr/bin/env python3
import requests

BASE = "http://challenge.nahamcon.com:30775"
INTERSTING = BASE + "/interesting"
POLL = BASE + "/poll"

methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]

for m in methods:
    r = requests.request(m, INTERSTING)
    print(f"{m:7} → {r.status_code}")

# now GET the poll endpoint to see the current state and the flag
r = requests.get(POLL)
print(f"\nFinal GET → {r.status_code}")
data = r.json()
print("Boxes state:", {k:v for k,v in data.items() if k.startswith("box_")})
print("\n FLAG:", data["flag"])
