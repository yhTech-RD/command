#!/usr/bin/env bash

# define need directories
dir=(
    '/storage/'
    '/storage/vm'
    '/storage/repos'
    '/storage/template'
    '/storage/command'
)

# Create need directories
for i in ${dir[@]}; do
    mkdir -p "$i"
done

mount /dev/sda /mnt

# Copy a repo and install base_env for YHCN
rm /etc/yum.repos.d/* -rf
cp /mnt/myrepo.repo /etc/yum.repos.d/myrepo.repo
cp -r /mnt/myrepo /storage/repos/
yum makecache
dnf install python39 -y

# Copy optimize command to YHCN
# this command will remove unneeded Cockpit tools and configura ip address for 10G NIC
cp -r /mnt/command/optimize /storage/command/
chmod +x /storage/command/optimize/optimize
cat > "/etc/bashrc" << EOF
alias optimize='/storage/command/optimize'
EOF

# Copy vmcreate command to YHCN
# this command will create a VM.
cp -r /mnt/command/vmcreate /storage/command/
chmod +x /storage/command/vmcreate/vmcreate
cat > "/etc/bashrc" << EOF
alias vmcreate='/storage/command/vmcreate'
EOF

# Copy template directory
# Copy VM templates
cp /mnt/template_dict.json /storage/template/
cp /mnt/template/* /storage/template/
