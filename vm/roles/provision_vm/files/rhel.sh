> {{ nic0_path }}
echo "TYPE=Ethernet" >> {{ nic0_path }}
echo "BOOTPROTO=none" >> {{ nic0_path }}
echo "NAME={{ nic0 }}" >> {{ nic0_path }}
echo "DEVICE={{ nic0 }}" >> {{ nic0_path }}
echo "ONBOOT=yes" >> {{ nic0_path }}
echo "IPADDR={{ vm_ip }}" >> {{ nic0_path }}
echo "NETMASK={{ subnet_ip }}" >> {{ nic0_path }}
echo "GATEWAY={{ gateway_ip }}" >> {{ nic0_path }}
echo "DEFROUTE=yes" >> {{ nic0_path }}
> {{ nic1_path }}
echo "TYPE=Ethernet" >> {{ nic1_path }}
echo "BOOTPROTO=none" >> {{ nic1_path }}
echo "NAME={{ nic1 }}" >> {{ nic1_path }}
echo "DEVICE={{ nic1 }}" >> {{ nic1_path }}
echo "ONBOOT=yes" >> {{ nic1_path }}
echo "IPADDR={{ vm_ip_prod }}" >> {{ nic1_path }}
echo "NETMASK={{ subnet_ip_prod }}" >> {{ nic1_path }}
systemctl restart network
