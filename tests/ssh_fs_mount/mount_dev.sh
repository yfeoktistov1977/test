#sudo apt-get install sshfs
sudo modprobe fuse
sshfs root@10.2.195.249:/ ./mnt_dev
