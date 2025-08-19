# Reset Forgotten Windows Password (Educational Guide)

⚠️ **Disclaimer**  
This tutorial is for **educational purposes only**. The method described here demonstrates how an attacker or technician could reset a Windows password if they have **physical access** to the machine.  
- Do **not** attempt this on any device you do not own or do not have explicit permission to test.  
- The purpose is to learn how such attacks work and how to protect your own systems.  

---

## Overview
If you forget your Windows password, it is possible to reset it without losing data.  
This method does **not require coding skills** and can be performed by almost anyone with physical access to the device.  

The technique works by replacing the **Windows Sticky Keys Utility** (`sethc.exe`) with `cmd.exe` during boot.
When Windows starts, you can open a system-level command prompt from the login screen and reset the password.

---

## Requirements
- A Windows machine (can be a VM or an actual laptop)
- Physical access to the target machine.  
- Basic knowledge of using the command prompt.  

> 📝 This tutorial is demonstrated on Windows 11, but the same method can also be applied to Windows 10.

---

## Steps to Reset Password

### 1. Turn on Windows machine and Boot it to Windows Recovery Environment (WinRE)
- On your lock screen, hold `SHIFT` and press `RESTART` to enter WinRE mode:

<img src="../../screenshots/windows-hacking/restart-from-login-screen.jpg" alt="Guide Image" style="width:80%; height:auto;">

### 2. Go to Recovery Settings and File Systems
- Choose `Troubleshoot`.

<img src="../../screenshots/windows-hacking/resset-windows-password-1.png" alt="Guide Image" style="width:80%; height:auto;">

- Choose `Advanced options`.

<img src="../../screenshots/windows-hacking/resset-windows-password-2.png" alt="Guide Image" style="width:80%; height:auto;">

- Choose `Command Prompt`.

<img src="../../screenshots/windows-hacking/resset-windows-password-3.png" alt="Guide Image" style="width:80%; height:auto;">

*Then, a black command prompt interface will popup.*

<img src="../../screenshots/windows-hacking/resset-windows-password-3-1.png" alt="Guide Image" style="width:80%; height:auto;">

- Type `notepad` to the command prompt.

*Note: We're not gonna create any new files, but to rename files.*

<img src="../../screenshots/windows-hacking/resset-windows-password-4.png" alt="Guide Image" style="width:80%; height:auto;">

- In the `notepad` interface, choose `File > Open`.

<img src="../../screenshots/windows-hacking/resset-windows-password-4-1.png" alt="Guide Image" style="width:80%; height:auto;">

### 3. Modify System Files via File Explorer
- Go to `This PC > Local Disk (:C)`.

<img src="../../screenshots/windows-hacking/resset-windows-password-5.png" alt="Guide Image" style="width:80%; height:auto;">

- Go to folder `Windows > System32`.

<img src="../../screenshots/windows-hacking/resset-windows-password-6.png" alt="Guide Image" style="width:80%; height:auto;">

- Change the options: `Files of type: All Files`.
- Search the file: has name `sethc`.
- Change its name to `sethc-netvn`.

*Note: After changing the name, you may still see the name `sethc` but it is okay, just make sure you have changed the name.*

<img src="../../screenshots/windows-hacking/resset-windows-password-7.png" alt="Guide Image" style="width:80%; height:auto;">

- Search the file: has name: `cmd`.
- Change its name to `sethc`.

*Note: After changing the name, you may still see the name `cmd` but it is okay, just make sure you have changed the name.*

<img src="../../screenshots/windows-hacking/resset-windows-password-8.png" alt="Guide Image" style="width:80%; height:auto;">

### 4. Reboot the Windows Machine and Reset the Password
- Close File Explorer, Notepad and Command Prompt.
- Click `Continue`.

<img src="../../screenshots/windows-hacking/resset-windows-password-9.png" alt="Guide Image" style="width:80%; height:auto;">

- After rebooting, on your lock screen, press the `SHIFT` key on your keyboard **5 times**.
- It will trigger a command propmt pop up.
- Type `net localgroup administrators`.

<img src="../../screenshots/windows-hacking/resset-windows-password-10.png" alt="Guide Image" style="width:80%; height:auto;">

- You should see the `Administrator: <Your username>`
- Type `net user <your username> *`
- Type your new password **2 times**, and if you see the successfull messsage, you have completed resetting the password:
```bash
C:\Windows\System32> net user <username> *
Type a password for the user:
Retype the password to confirm:
The command completed successfully.
```

*Note: If your username has space such as `Michael Jackson`, add double quote to the command: `net user "Michael Jackson" *`*

- Close the command prompt and type your **new password** to login to your Windows machine.

## Key Takeaways

This method works because Windows allows replacing system utilities in recovery mode.

No user data is lost — only the password is reset.

Disk encryption (BitLocker, VeraCrypt) prevents this attack, since the drive would be locked in recovery mode.

## Author & Credits
This tutorial was written by James Cao

- 📌 Connect with me:
    - 🌐 [GitHub](https://github.com/jameskaois)
    - 🐦 [X (Twitter)](https://x.com/jameskaois)
