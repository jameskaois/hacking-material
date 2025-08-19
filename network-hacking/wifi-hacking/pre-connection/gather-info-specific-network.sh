# Make sure your wireless adapter is connected to Linux machine
# Enable monitor mode on it

# Change wireless adapter interface based on your machine with ifconfig
# Gather info into result file of a specific network (for further attack like brute-force)
airodump-ng --bssid <bssid of target> --channel <channel of target> --write result wlan0

# Do not write the result file
airodump-ng --bssid <bssid of target> --channel <channel of target> wlan0