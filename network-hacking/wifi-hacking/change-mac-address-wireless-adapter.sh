# Change to root to have access
sudo -i
[sudo] password for xxxxx:

# Change wlan0 to your wireless adapter interface (use ifconfig to know)
# Turn off wireless adapter interface down
ifconfig wlan0 down

# Change MAC address to 00:11:22:33:44:55
ifconfig wlan0 hw ehter 00:11:22:33:44:55

# Turn on wireless adapter interface down
ifconfig wlan0 up