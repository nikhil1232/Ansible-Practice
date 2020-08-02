#!/bin/sh

# Install Vagrant
apt-get install vagrant -y

# Install Virtualbox
apt-get install virtualbox -y

# Start Vagrant. This would use the Vagrantfile to setup the whole environment. Make sure you have the Vagrantfile present in this repo saved in the same directory from which this script is run.
vagrant up

# Additional command. You could run this if at all your provisions/shell commands were not run during the vagrant up command.
# vagrant provision

# IP address resolution to Hostnames for the main machine. For all the other nodes it is managed in the Vagrantfile.
sudo sh -c "echo '192.168.0.120   frontend-1.com  frontend-1\n192.168.0.121   frontend-2.com  frontend-2\n192.168.0.122   backend-1.com  backend-1\n192.168.0.123   backend-2.com  backend-2' >> /etc/hosts"

# Generate SSH keys in the Controller node and transfer it to the main machine. 
vagrant ssh controller -c "ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y 2>&1 >/dev/null;cat ~/.ssh/id_rsa.pub" > tmp.pub

# Copy the public key of the controller node to the authorized keys of all the other nodes.
scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/backend-1/virtualbox/private_key tmp.pub vagrant@192.168.0.122:~ && vagrant ssh backend-1 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/frontend-1/virtualbox/private_key tmp.pub vagrant@192.168.0.120:~ && vagrant ssh frontend-1 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/frontend-2/virtualbox/private_key tmp.pub vagrant@192.168.0.121:~ && vagrant ssh frontend-2 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/backend-2/virtualbox/private_key tmp.pub vagrant@192.168.0.123:~ && vagrant ssh backend-2 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

rm tmp.pub

# Transfer the connected_users.yml playbook(present in this repo) to the controller node and execute it using ansible.
scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/controller/virtualbox/private_key connected_users.yml vagrant@192.168.0.124:~ && vagrant ssh controller -c "ansible-playbook ~/connected_users.yml"




