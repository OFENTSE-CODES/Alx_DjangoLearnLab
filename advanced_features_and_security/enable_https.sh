#!/bin/bash

# Install Certbot for Let's Encrypt SSL
sudo apt update
sudo apt install certbot python3-certbot-nginx

# Replace with your actual domain
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Set up automatic certificate renewal
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer