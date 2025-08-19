# Make sure your wireless adapter is connected to Linux machine
# Enable monitor mode on it

# Change wireless adapter interface based on your machine with ifconfig
# Show nearby 2.4GHz wireless networks
airodump-ng wlan0

# Show nearby 5GHz wireless networks (make sure your adapter supports it)
airodump-ng --band a wlan0

# Show both 2.4GHz & 5GHz netwoks at once (slower scan than just one band a time)
airodump-ng --band abg wlan0