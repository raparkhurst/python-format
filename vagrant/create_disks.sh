#!/bin/bash

DISKS=20

for d in `seq 1 $DISKS`; do
    echo "Creating disk image ${d}..."
    VBoxManage createhd --filename ./disks/drive-${d} --size 1000
done
