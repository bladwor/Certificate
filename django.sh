#!/bin/bash
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000
python3 /var/www/html/manage.py runsslserver 194.87.146.144:8000
