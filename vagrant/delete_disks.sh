#!/bin/bash


echo "WARNING THIS CAN BE VERY DESTRUCTIVE!!!!"

for i in `VBoxManage list hdds | grep UUID | awk '{print $2}'`; do VBoxManage closemedium disk ${i} --delete; done
