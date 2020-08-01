#!/bin/bash
sudo mysql -e "CREATE USER 'foo'@localhost IDENTIFIED BY 'far';"
sudo mysql -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('fred');"
sudo mysql -e "UPDATE mysql.user SET plugin = '' WHERE user = 'root' AND host = 'localhost';"
sudo mysql -e "DROP USER ''@'localhost'"
sudo mysql -e "DROP USER ''@'$(hostname)'"
sudo mysql -e "DROP DATABASE test"
sudo mysql -e "FLUSH PRIVILEGES"
