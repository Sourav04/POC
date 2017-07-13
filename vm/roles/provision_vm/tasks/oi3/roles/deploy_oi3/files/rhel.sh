#!/bin/bash
sudo su
> {{ nic0_path }}
touch {{ nic0_path }}
echo "TYPE=Ethernet" >> {{ nic0_path }}
echo "BOOTPROTO=none" >> {{ nic0_path }}
echo "NAME={{ nic0 }}" >> {{ nic0_path }}
echo "DEVICE={{ nic0 }}" >> {{ nic0_path }}
echo "ONBOOT=yes" >> {{ nic0_path }}
echo "IPADDR={{ vm_ip }}" >> {{ nic0_path }}
echo "NETMASK={{ subnet_ip }}" >> {{ nic0_path }}
echo "GATEWAY={{ gateway_ip }}" >> {{ nic0_path }}
echo "DEFROUTE=yes" >> {{ nic0_path }}
ifup {{ nic0 }}
systemctl restart network
