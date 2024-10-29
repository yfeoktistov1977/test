#choose apropriate ARCH

# copy our linux-4.3.taurus.config to ../packages-src-taurus/linux-4.3/arch/arm/configs/taurus_defconfig
#then delete ./config from ../packages-src-taurus/linux-4.3
#then run(with appropriate ARCH for device) :

cd ./linux-4.3
export ARCH=arm
#make taurus_defconfig ARCH=arm
make .config ARCH=arm
make menuconfig ARCH=arm

#then copy ../packages-src-taurus/linux-4.3/.config to linux-4.3.taurus.config
