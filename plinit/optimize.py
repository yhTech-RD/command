import shutil
import os
import netifaces
from pyroute2 import IPDB


def remove_file():
    """
    remove unneeded files in Cockpit
    """

    dirs_to_delete = ["kdump", "packagekit", "apps", "sosreport", "selinux"]

    for dir_name in dirs_to_delete:
        dir_path = "/usr/share/cockpit/" + dir_name
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Deleted directory: {dir_path}")
        else:
            print(f"Directory not found: {dir_path}")


def add_address():
    iface_name = ["ens1f0", "ens1f1"]

    for i in iface_name:
        iface_index = netifaces.ifaddresses(i)[netifaces.AF_INET][0]["index"]
        with IPDB() as ipdb:
            iface = ipdb.interfaces[iface_index]
            iface.add_ip("192.168.1.100/24")
            iface.up()
            print(f"Added IP address to {i}")


def main():
    remove_file()
    add_address()


if __name__ == "__main__":
    main()
