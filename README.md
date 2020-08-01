# Ansible-Practice
A small practice scenario envolving deployment of various services in automated way and managing those services using containerized products/tools like vagrant and orchestration tools like ansible   

## Practice Scenario
1) Create a script which will create 5 containers that could be used with vagrant for orchestration. With the following names: frontend-1, frontend-2, backend-1, backend-2, controller

2) All those containers must have ssh access on port 22.

3) frontend-1, frontend-2, backend-1, backend-2 would be accessible using certificates and without password from the controller node. All nodes should be accessible from the hypervisor or any other node through their name or IP address
 
4) frontend-1 and frontend-2 should have installed a HTTP server such as Apache and offering port 80 open and serving a page which says “hello world”.

5) backend-1 and backend-2 should have installed a MariaDB (or any other database such as postgre) and configured with the user ‘foo’ and password ‘far’. Root password for the database must be changed to ‘fred’.

6) All nodes except frontend-1 must have vim installed. frontend-1 must NOT have vim installed.
        
7) A playbook called “connected_users.yml” should execute “w -i -f” command in all nodes and save the output in the controller node in a file called “connected_users_$node_$date_$time.log” which would identify the node, time and date where it was executed the command.

8) A test can be written to check the previous tasks have been performed. This could be written in Python or using Robot Framework. Can be executed before any task is performed and fails all the test cases and after all tasks are performed by providing passing all tests.


## Solutions: Practice Scenario
1) Create a script which will create 5 containers that could be used with vagrant for orchestration. With the following names: frontend-1, frontend-2, backend-1, backend-2, controller: 
##### Solution:
A bash script(main.sh) that would help in setting up everything required in order to complete the assessment. A vagrant file was also prepared(present in this repository) that would help in creation of 5 nodes with the names specified above. (NOTE: FOR completing this whole assessment all you need to run is the "**bash main.sh**" and all the files present in this repository should be cloned in the same directory)

2) All those containers must have ssh access on port 22. 
##### Solution:
 All the nodes would be accessible via port 22 by default after setting up the vagrant nodes.

3) frontend-1, frontend-2, backend-1, backend-2 would be accessible using certificates and without password from the controller node. All nodes should be accessible from the hypervisor or any other node through their name or IP address: 
##### Solution:
The code involving the denial of password based authentication in the controller node is present in the main.sh file and the Vagrant file.
 
4) frontend-1 and frontend-2 should have installed a HTTP server such as Apache and offering port 80 open and serving a page which says “hello world”: 
##### Solution:
The Apache httpd server installation and setting up a custom page is managed in the vagrant file itself.
        
5) backend-1 and backend-2 should have installed a MariaDB (or any other database such as postgre) and configured with the user ‘foo’ and password ‘far’. Root password for the database must be changed to ‘fred’:
##### Solution:
The Mariadb installation and additional configurations like modifying passwords and adding new users are all managed in the vagrant file which includes a shell script within itself.

6) All nodes except frontend-1 must have vim installed. frontend-1 must NOT have vim installed:
##### Solution:
The installation of vim in all the nodes except the frontend-1 node is managed via the vagrant file.

7) A playbook called “connected_users.yml” should execute “w -i -f” command in all nodes and save the output in the controller node in a file called “connected_users_$node_$date_$time.log” which would identify the node, time and date where it was executed the command:
##### Solution:
The code to install, configure and run ansible is present in the bash script itself (main.sh). It also includes the connected_users.yml playbook file that would run the "w" command on all the nodes and would save the output in a format as specified in the problem statement.

8) A test can be written to check the previous tasks have been performed. This could be written in Python or using Robot Framework. Can be executed before any task is performed and fails all the test cases and after all tasks are performed by providing passing all tests:
##### Solution:
A python file (test.py) is also present in the directory that could be run to check if all the test cases/statements have been passed failed. 


## Instructions: For setting up
```shell
# Clone the whole repository
git clone https://github.com/nikhil1232/Ansible-Practice
cd Ansible-Practice
bash main.sh
```

## Instructions: To check for PASS and FAIL cases

# Clone the whole repository
> git clone https://github.com/nikhil1232/Ansible-Practice
> cd Ansible-Practice
# Run this once before running the main.sh script
> python3 test.py
> bash main.sh
# Once setup is ready try to run the same python script again to check for pass and fail cases.
> python3 test.py


