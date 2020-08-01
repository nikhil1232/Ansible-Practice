#!/bin/sh

apt-get install vagrant -y

vagrant up

vagrant provision

sudo sh -c "echo '192.168.0.120   frontend-1.com  frontend-1\n192.168.0.121   frontend-2.com  frontend-2\n192.168.0.122   backend-1.com  backend-1\n192.168.0.123   backend-2.com  backend-2' >> /etc/hosts"

vagrant ssh controller -c "ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y 2>&1 >/dev/null;cat ~/.ssh/id_rsa.pub" > tmp.pub

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/backend-1/virtualbox/private_key tmp.pub vagrant@192.168.0.122:~ && vagrant ssh backend-1 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/frontend-1/virtualbox/private_key tmp.pub vagrant@192.168.0.120:~ && vagrant ssh frontend-1 -c "cat ~/tmp.pub >> ~/.ssh/authorized_keys;rm ~/tmp.pub"

rm tmp.pub

scp -o "StrictHostKeyChecking no" -i /root/.vagrant/machines/controller/virtualbox/private_key connected_users.yml vagrant@192.168.0.124:~ && vagrant ssh controller -c "ansible-playbook ~/connected_users.yml"




