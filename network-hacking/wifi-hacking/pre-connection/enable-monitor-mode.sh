# Check your wireless adapter interface mode
iwconfig

# Turn off wireless adapter interface
ifconfig wlan0 down

# Enable monitor mode
iwconfig wlan0 mode monitor

# Turn on wireless adapter interface
ifconfig wlan0 up