import shutil
import os
import netifaces
import json
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
    
    files_to_delete = ['services*','logs*']
    for file_name in files_to_delete:
        file_path = "/usr/share/cockpit/systemd" + file_name
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
    
    modify_file = "/usr/share/cockpit/systemd/machines.js"
    with open(modify_file, "r") as f:
        my_list = json.load(f)
        for key in list(my_list['menu'].keys()):
            if key == "services" or key == "logs" in my_list['menu']:
                del my_list['menu'][key]

    with open(modify_file, "w") as f:
        json.dump(my_list, f, indent=4)



def add_address():
    iface_name = ["ens1f0", "ens1f1"]

    for i in iface_name:
        with IPDB() as ipdb:
            iface = ipdb.interfaces[i]
            iface.add_ip("192.168.1.100/24")
            iface.commit()
            iface.up()

    for j in iface_name:
        print(netifaces.ifaddresses(j))


def main():
    remove_file()
    add_address()


if __name__ == "__main__":
    main()
