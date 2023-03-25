import os
import json

def get_path():
    with open("config.json", "r") as f:
        all_vaules = json.load(f)
    
    xml_path = all_vaules[f"{}"]["xml"]
    qcow2_path = all_vaules[f"{}"]["qcow2"]

def copy_vm_file(vm_template, vm_xml, qcow2_path):
    os.system(f"cp {vm_xml} /storage/vm/{vm_template}")
    os.system(f"cp {qcow2_path} /storage/vm{vm_template}")


def main():
    vm_template = input()
    vm_xml = input()
    qcow2_path = input()
    copy_vm_file(vm_template, vm_xml, qcow2_path)

if __name__ == "__main__":
    main()