
# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"

  $script = <<-SCRIPT
  sudo sh -c "echo '192.168.0.124   controller.com  controller' >> /etc/hosts"
  sudo sh -c "echo '192.168.0.120   frontend-1.com  frontend-1' >> /etc/hosts"
  sudo sh -c "echo '192.168.0.121   frontend-2.com  frontend-2' >> /etc/hosts"
  sudo sh -c "echo '192.168.0.122   backend-1.com  backend-1' >> /etc/hosts"
  sudo sh -c "echo '192.168.0.122   backend-2.com  backend-2' >> /etc/hosts"
  SCRIPT

  $web = <<-SCRIPT
  sudo apt-get install apache2 -y && systemctl start apache2.service
  sudo sh -c "echo '<h1>Hello World</h1>' > /var/www/html/index.html"
  SCRIPT

  $db = <<-SCRIPT
  sudo apt-get update -y
  sudo apt-get install mariadb-server mariadb-client -y
  SCRIPT

  $edit = <<-SCRIPT
  sudo apt-get install vim -y
  SCRIPT

  $edit2 = <<-SCRIPT
  sudo apt-get remove vim --purge -y
  SCRIPT

  $sshblock = <<-SCRIPT
  sudo sh -c "echo 'Match address 192.168.0.124\n    PasswordAuthentication no' >> /etc/ssh/sshd_config"
  sudo service sshd restart
  SCRIPT

  $ans = <<-SCRIPT
  sudo apt-add-repository ppa:ansible/ansible
  sudo apt-get update -y
  sudo apt-get install ansible -y
  sudo sh -c "echo '[ser]\n192.168.0.120\n192.168.0.121\n192.168.0.122\n192.168.0.123' >> /etc/ansible/hosts"
  SCRIPT

  $default_network_interface = `ip route | grep -E "^default" | awk '{printf "%s", $5; exit 0}'` 

  config.vm.define "frontend-1" do |f1|
    f1.vm.hostname = "frontend-1"
    f1.vm.network "public_network", :bridged => "wl01", :ip => "192.168.0.120", bridge: "#$default_network_interface"
    f1.vm.provision "shell", inline: $script
    f1.vm.provision "shell", inline: $web
    f1.vm.provision "sshblock", type: "shell", inline: $sshblock
    f1.vm.provision "edit2", type: "shell", inline: $edit2
  end

  config.vm.define "frontend-2" do |f2|
    f2.vm.hostname = "frontend-2"
    f2.vm.network "public_network", :bridged => "wl01", :ip => "192.168.0.121", bridge: "#$default_network_interface"
    f2.vm.provision "shell", inline: $script
    f2.vm.provision "shell", inline: $web
    f2.vm.provision "sshblock", type: "shell", inline: $sshblock
  end

  config.vm.define "backend-1" do |b1|
    b1.vm.hostname = "backend-1"
    b1.vm.network "public_network", :bridged => "wl01", :ip => "192.168.0.122", bridge: "#$default_network_interface"
    b1.vm.provision "shell", inline: $script
    b1.vm.provision "db", type: "shell", inline: $db
    b1.vm.provision "db2", type: "shell", path: "sql.sh"
    b1.vm.provision "shell", inline: $edit
    b1.vm.provision "sshblock", type: "shell", inline: $sshblock
  end  

  config.vm.define "backend-2" do |b2|
    b2.vm.hostname = "backend-2"
    b2.vm.network "public_network", :bridged => "wl01", :ip => "192.168.0.123", bridge: "#$default_network_interface"
    b2.vm.provision "shell", inline: $script
    b2.vm.provision "db", type: "shell", inline: $db
    b2.vm.provision "db2", type: "shell", path: "sql.sh"
    b2.vm.provision "shell", inline: $edit
    b2.vm.provision "sshblock", type: "shell", inline: $sshblock
  end 

  config.vm.define "controller" do |controller|
    controller.vm.hostname = "controller"
    controller.vm.network "public_network", :bridged => "wl01", :ip => "192.168.0.124", bridge: "#$default_network_interface"
    controller.vm.provision "shell", inline: $script 
    controller.vm.provision "shell", inline: $edit
    controller.vm.provision "ans", type: "shell", inline: $ans
  end
end
