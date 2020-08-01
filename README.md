# Ansible-Practice
A small practice scenario envolving deployment of various services in automated way and managing those services using containerized products/tools like vagrant and orchestration tools like ansible   

## Practice Scenario
1) Create a script which will create 5 containers that could be used with vagrant for orchestration. With the following names: frontend-1, frontend-2, backend-1, backend-2, controller

2) All those containers must have ssh access on port 22.

3) frontend-1, frontend-2, backend-1, backend-2 would be accessible using certificates and without password from the controller node. All nodes should be accessible from the hypervisor or any other node through their name or IP address
 
4) frontend-1 and frontend-2 should have installed a HTTP server such as Apache and offering port 80 open and serving a page which says “hello world”.
        Given keywords: apache, httpd.conf, port
5) backend-1 and backend-2 should have installed a MariaDB (or any other database such as postgre) and configured with the user ‘foo’ and password ‘far’. Root password for the database must be changed to ‘fred’.

6) All nodes except frontend-1 must have vim installed. frontend-1 must NOT have vim installed.
        Given keywords: ansible modules, apt, dnf, rpm, apt_rpm
7) A playbook called “connected_users.yml” should execute “w -i -f” command in all nodes and save the output in the controller node in a file called “connected_users_$node_$date_$time.log” which would identify the node, time and date where it was executed the command.

8) A test can be written to check the previous tasks have been performed. This could be written in Python or using Robot Framework. Can be executed before any task is performed and fails all the test cases and after all tasks are performed by providing passing all tests.

