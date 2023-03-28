#!/usr/bin/env bash
set -euo pipefail


# This is a comment describing the code. The code is used to prepare the
# workdir variable for use in the script. The workdir variable is used to
# specify the location of the repository.
workdir=${1:-$PWD/myrepo/}

dnf install -y createrepo modulemd-tools

if [ ! -d $workdir ]; then
    mkdir -p $workdir
fi

packages=(
    "python39"
)

cd $workdir

for package in "${packages[@]}"; do
    dnf download -y --resolve --downloadonly --downloaddir="$workdir" "$package"
done

createrepo $workdir

repo2module -s stable . modules.yaml
modifyrepo_c --mdtype=modules modules.yaml "$workdir/repodata/"

cat > "$workdir/myrepo.repo" << EOF
[myrepo]
name=MyRepo
baseurl=file:///storage/repos/myrepo
enabled=1
gpgcheck=0
EOF

cat "$workdir/myrepo.repo"