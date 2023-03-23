import argparse, libvirt, sys, os, json, time

# 创建解析器对象
parser = argparse.ArgumentParser(description="A command to Create Virtual Machine in fast way.")
supports = json.load(open('./templete_dict.json', 'r'))
default_name = None

# 添加参数
parser.add_argument("--type", type=str, help="Defind the type of the VM")
parser.add_argument("--vmlist", action="store_true", help="Show the list of the VM")
parser.add_argument("--name", default=default_name, type=str,
                    help="Defind the name of the VM, default is VM_Type-NowTime")
parser.add_argument("--cpu", type=int, default=None, help="Define the number of cpus for a VM")
parser.add_argument("--memory", type=int, default=None, help="Defind the memory of the VM")
parser.add_argument("--disk", type=int, default=None, help="Defind VM's size of disk")

# 解析参数
args = parser.parse_args()


# 实现逻辑
def option_list():
    args.vmlist = print("\n".join(list(supports.keys())))
    sys.exit()


def check_name():
    if args.name is None:
        args.name = f"{args.type}-{time.strftime('%H%M%S')}"

    return args.name


def check_type():
    if args.type is None:
        print("Error: VM type is needed, Please define a type of the VM.")
        sys.exit()
    elif args.type not in supports.keys():
        print(f"Error: {args.type} is not supported.Please use '--vmlist' to check the list of the VM.")
        sys.exit()
    else:
        return args.type


def get_path():
    xml_path = supports[args.create]['xml']
    qcow2_path = supports[args.create]['qcow2']
    return xml_path, qcow2_path


def copy_file(vm_type, xml_path, qcow2_path):
    os.system(f'cp {xml_path} /storage/vm/{vm_type}')
    os.system(f'cp {qcow2_path} /storage/vm/{vm_type}')


def defind_vm():
    cpu = None
    memory = None
    disk = None
    if args.cpu or args.memory or args.disk == True:
        if args.cpu:
            pass
        if args.memory:
            pass
        if args.disk:
            pass

    return all


def change_xml():
    pass


def create_vm():
    pass


def main():
    if args.vmlist == True:
        option_list()
    else:
        copy_file(check_type(), get_path()[0], get_path()[1])
        if args.cpu or args.memory or args.disk:
            create_vm()
        create_vm()


if __name__ == "__main__":
    main()

# 输出结果
# if args.vmlist == True:
#     args.vmlist = print("\n".join(list(supports.keys())))
#     sys.exit()

# if args.type == None:
#     print("Error: VM type is needed, Please define a type of the VM.")
#     sys.exit()
# elif args.type not in supports.keys():
#     print(f"Error: {args.type} is not supported.Please use '--vmlist' to check the list of the VM.")
# else:
#     if args.name == None:
#         args.name = f"{args.type}-{time.strftime('%H%M%S')}"
#     else:
#         args.name = str(args.name)
#     # 创建VM, 逻辑待补充
#     pass


#     xml_path = supports[args.create]['xml']
#     qcow2_path = supports[args.create]['qcow2']

#     # os.system(f'copy {xml_path} /storage/vm/{default}')
#     # os.system(f'copy {qcow2_path} /storage/vm/{default}')
