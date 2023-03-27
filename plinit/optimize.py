import shutil
import os

def remove_file():
    '''
    remove unneeded files in Cockpit
    '''

    dirs_to_delete = ['kdump', 'packagekit', 'apps', 'sosreport', 'selinux']

    for dir_name in dirs_to_delete:
        dir_path = '/usr/share/cockpit/' + dir_name
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Deleted directory: {dir_path}")
        else:
            print(f"Directory not found: {dir_path}")

def main():
    remove_file()

if __name__ == '__main__':
    main()
