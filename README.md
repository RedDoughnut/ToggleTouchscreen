# ToggleTouchscreen
This program will allow you to toggle touchscreen on Windows 10+ machine. Run touchscreen.py to start the program.

# Important!
Before you start program you need to locate your touchscreen device in Device Manager. Follow next steps:

1. Open Device Manager
   Open search and search for device manager, and then click on it. (Alternativly: Windows+R -> "devmgmt.msc")

2. Open "Human Interface Devices" category.

3. Double-Click on "HID-compliant touch screen" device.
   If you don't see it it means your device doesn't have touchscreen.

4. Go to "Details" tab.

5. Switch property to "Device instance path"

6. Copy the value.

7. Go to touchscreen.py and in variable named "tloc" put value you copied.

variable tloc should look like this: 
tloc = "HID\ELAN9008&COL01\\5&2BED5342&0&0000"

**Note**: If there's error in code replace each "\" with "\\", **only in tloc variable**.
