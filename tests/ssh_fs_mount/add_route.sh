#10.2.2.32 - gateway for 10.2.x.x network
#route
#ip route show
#sudo ip route del 10.10.0.0/16
sudo ip route add 10.10.0.0/16 via 10.2.2.32 dev eth0
