exit(0)


            # Disk exists and is partitioned, but may not be formatted
            if os.path.exists(linux_device_file+"1"):
                print linux_device_file+"1 exists.  Checking if we need to format"

                if (os.system("file -sL " + linux_device_file + "* | grep XFS 1>/dev/null")) is not 0:
                    print "Disk has not been formatted...formatting xfs"
                    os.system("mkfs.xfs " + linux_device_file + "1" + " -f")
                    print "done"

                # check /data/XX
                if os.path.exists("/data/" + disk_counter(disk_letter)):
                    print "/data/" + disk_counter(disk_letter) + " does exist"
                else:
                    print "/data/" + disk_counter(disk_letter) + " does not exist"
                    os.system("mkdir -p /data/" + disk_counter(disk_letter))

                # check /etc/fstab
                if check_fstab(device_id=linux_device_file + "1"):
                    print "found " + linux_device_file + " in /etc/fstab, no need to update!"
                else:
                    print "did not find " + linux_device_file + "1" + " in /etc/fstab; updating!"
                    with open("/etc/fstab", "a") as myfile:
                        myfile.write(linux_device_file + "1\t/data/" + disk_counter(disk_letter) + "\txfs\tdefaults,noatime,nodiratime\t0\t0\n")




            # Disk exists and NO partition exists; format and partition
            else:
                print "Creating parition on " + linux_device_file

                # Attempted to use this, but didn't work..Keeping here for possible future use.
                #subprocess.check_call(['parted', disk_file, '--script -- mklabel gpt mkpart primary 0% 100%'])
                os.system("parted " + linux_device_file + " --script -- mklabel gpt mkpart primary xfs 0% 100%")

                print "formatting xfs..."
                os.system("mkfs.xfs " + linux_device_file + "1" + " -f")
                print "done...\n"

                if not os.path.exists("/data/" + disk_counter(disk_letter)):
                    print "/data/" + disk_counter(disk_letter) + " does not exist"


                # check /data/XX
                if os.path.exists("/data/" + disk_counter(disk_letter)):
                    print "/data/" + disk_counter(disk_letter) + " does exist"
                else:
                    print "/data/" + disk_counter(disk_letter) + " does not exist"
                    os.system("mkdir -p /data/" + disk_counter(disk_letter))

                # check /etc/fstab
                if check_fstab(device_id=linux_device_file + "1"):
                    print "found " + linux_device_file + " in /etc/fstab, no need to update!"
                else:
                    print "did not find " + linux_device_file + "1" + " in /etc/fstab; updating!"
                    with open("/etc/fstab", "a") as myfile:
                        myfile.write(linux_device_file + "1\t/data/" + disk_counter(disk_letter) + "\txfs\tdefaults,noatime,nodiratime\t0\t0\n")

