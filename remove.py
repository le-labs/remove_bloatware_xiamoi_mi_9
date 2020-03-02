import os
from ppadb.client import Client as AdbClient

os.system("adb devices")

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

with open("bloat_packages.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if stripped_line[0] != "#":
        # Check apk is installed
        for device in devices:
            print(stripped_line + " is installed: " + str(device.is_installed(stripped_line)))
        # Uninstall
        for device in devices:
            device.shell("pm uninstall -k --user 0 " + stripped_line)

        # Check apk is installed
        for device in devices:
            print(stripped_line + " is installed: " + str(device.is_installed(stripped_line)))
