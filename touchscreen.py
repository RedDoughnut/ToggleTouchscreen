import os
from win32comext.shell import shell as shell

tloc = "HID\\ELAN9008&COL01\\5&2BED5342&0&0000"

output = os.popen(f'pnputil /enum-devices /instanceid "{tloc}"').read()

if output.find("Disabled")==-1: #enabled
    commands = f'pnputil /disable-device "{tloc}"'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
else: #disabled
    commands = f'pnputil /enable-device "{tloc}"'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)