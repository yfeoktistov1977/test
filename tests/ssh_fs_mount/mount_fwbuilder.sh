#sudo apt-get install sshfs
sudo modprobe fuse
sshfs fwbuilder@esattore.okb-ipmce.lcl:/home/fwbuilder ./mnt
