import argparse

import create_vm
import option_list

parser = argparse.ArgumentParser(description="A command to Create Virtual Machine in fast way.")
default_name = None

# 添加参数
parser.add_argument("--type", type=str, help="Define the type of the VM")
parser.add_argument("--vmlist", action="store_true", help="Show the list of the VM")
parser.add_argument("--name", default=default_name, type=str, help="Define the name of the VM, default is "
                                                                   "VM_Type-NowTime",)
parser.add_argument(
    "--cpu", type=int, default=None, help="Define the number of cpus for a VM"
)
parser.add_argument(
    "--memory", type=int, default=None, help="Define the memory of the VM"
)
parser.add_argument("--disk", type=int, default=None, help="Define VM's size of disk")

# 解析参数
args = parser.parse_args()


def main():
    if args.vmlist:
        option_list.print_option_list()
    else:
        # create_vm.create_vm(vm_type=args.type, name=args.name, cpu=args.cpu, memory=args.memory, disk=args.disk)
        pass


if __name__ == "__main__":
    main()
