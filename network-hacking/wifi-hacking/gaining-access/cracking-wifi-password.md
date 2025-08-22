# WEP (Wired Equivalent Privacy) Cracking

- Old encryption
- Uses an algorithm called **RS4**

## Workflow

![Guide Image](../../../screenshots/network-hacking/cracking-wifi-1.png)

![Guide Image](../../../screenshots/network-hacking/cracking-wifi-2.png)

- IV is too **small.**
- IV is sent in **plain text.**
- IVs will repeat on **busy networks.**
- This makes WEP vulnerable to statistical attacks.

## Cracking

- Capture a large number of of packets/IVs.
- Analyse captured IVs and crack the key.

| `airodump-ng —bssid <bssid> —channel <channel> --write result <wlan interface>` | Capture packets of network → write it to a file for anaylising |
| --- | --- |
| `aircrack-ng <xx.cap file>` | Crack the key by using captured packets |

## Fake Authentication

- If network is not busy.
- It would take some time to capture the IVs.

→ Force the AP to generate new IVs.

→ Associate with the AP before launching the attack.

| `aireplay-ng --fakeauth 0 -a <bssid network> -h <wireless adapter MAC> <wireless interface>` | Force the network to add wireless adapter to the client (not yet connected) |
| --- | --- |

## ARP Request Replay

- Wait for an ARP packet.
- Capture it, and replay it (retransmit it).
- This causes the AP to produce another packet with a **new IV**.
- Keep doing this till we have enough IVs to crack the key.

| `aireplay-ng --arpreplay 0 -b <bssid network> -h <wireless adapter MAC> <wireless interface>` | Force network to create new IVs/packets. |
| --- | --- |

# WPA / WPA2 Cracking

- Both can be cracked using the **same method.**
- Made to address the issues in WEP.
- Much more secure.
- Each packet is encrypted using a unique temporary key.

→ Packets contain no useful information.

## WPS

- WPS is a feature that can be used with WPA & WPA2.
- Allows clients to connect without the password.
- Authentication is done using a 8 digit pin.
    - 8 Digits is very small.
    - We can try all possible pins in a relatively short time.
    - Then the WPS pin can be used to compute the actual password.

*Note: This only works if the router is configured not to use PBC (Push Button Authentication).*

| `wash —-interface <wireless interface>` | Scans nearby networks and **lists only those that have WPS enabled**  |
| --- | --- |
| `reaver —-bssid <target router address> -—channel <channel> —-interface <wireless interface> -vvv —-no-associate`  | Sends **WPS PIN guesses** to the router without associate (use fake auth manually) |

## Capturing The Handshake

Using `airodump-ng` write of a specific network and `aireplay-ng —-deauth` to capture the handshake

- The handshake does not contain data that helps recover the key.
- It contains data that can be used to check if a key is valid or not.

## Creating A WordList

- Crunch can be used to create a wordlist.

![Guide image](../../../screenshots/network-hacking/cracking-wifi-3.png)

- Wordlists links:
    
    ```
    ftp://ftp.openwall.com/pub/wordlists/
    http://www.openwall.com/mirrors/
    https://github.com/danielmiessler/SecLists
    http://www.outpost9.com/files/WordLists.html
    http://www.vulnerabilityassessment.co.uk/passwords.htm
    http://packetstormsecurity.org/Crackers/wordlists/
    http://www.ai.uga.edu/ftplib/natural-language/moby/
    http://www.cotse.com/tools/wordlists1.htm
    http://www.cotse.com/tools/wordlists2.htm
    http://wordlist.sourceforge.net/
    ```
    

## Cracking Using Wordlists

Two things needed to crack WPA/WPA2:

1. 4-Way Handshake
2. Wordlist