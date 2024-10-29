modinfo -b /lib/modules/$(uname -r)/kernel $(cat /lib/modules/$(uname -r)/modules.builtin) > ./modules.builtin.modinfo
