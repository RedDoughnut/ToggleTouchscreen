import os
from win32comext.shell import shell as shell

tloc = "" # Enter your device instance id here!

output = os.popen(f'pnputil /enum-devices /instanceid "{tloc}"').read()

if output.find("Disabled")==-1: # Touchscreen enabled already, so turn it off
    commands = f'pnputil /disable-device "{tloc}"'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
else: # Touchscreen disabled, so turn it on
    commands = f'pnputil /enable-device "{tloc}"'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
