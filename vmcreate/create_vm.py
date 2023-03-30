import sys
import json
import time
import os
import xml.etree.ElementTree as ET


class DefineVm:
    def __init__(
        self, type=None, xml_path=None, name=None, cpu=None, memory=None, disk=None
    ):
        self.type = type
        self.xml_path = xml_path
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def check_type(self):
        supports = json.loads(open("template_dict.json", "r").read())
        if self.type is None:
            print("Error: VM type is needed, Please define a type of the VM.")
            sys.exit()
        elif self.type not in supports.keys():
            print(
                f"Error: {self.type} is not supported, Use --vmlist to show the list of the VM."
            )
            sys.exit()
        else:
            return self.type

    def vm_name(self):
        origin_name = self.check_type()
        default_name = f"{origin_name}-{time.strftime('%Y%m%d%H%M%S')}"
        if self.name is None:
            return default_name
        else:
            return self.name
        
    def get_path(self):
        with open("config.json", "r") as f:
            all_vaules = json.load(f)
        
        xml_path = all_vaules[f"{self.type}"]["xml"]
        qcow2_path = all_vaules[f"{self.type}"]["qcow2"]
        return xml_path, qcow2_path

    def copy_file(self):
        xml_path, qcow2_path = self.get_path()
        os.system(f"cp {xml_path} /storage/vm/{self.name}")
        os.system(f"cp {qcow2_path} /storage/vm/{self.name}")
        
    def vm_cpu(self):
        pass

    def vm_memory(self):
        pass

    def vm_disk(self):
        pass

    def define_vm(self):
        pass
            
    def create_vm(self):
        self.define_vm()


def main():
    create = DefineVm(type="CentOS_8")


if __name__ == "__main__":
    main()
