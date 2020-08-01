import subprocess
import socket
import re

print("\n")

print("\nChecking for Vagrant Installation\n--------------------------------------------------------------\n\n")
try:
    output = subprocess.check_output(
        "vagrant --version", stderr=subprocess.STDOUT, shell=True, timeout=3,
        universal_newlines=True).rstrip()
except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
else:
    print("Status : PASS\n\n{}\n".format(output))



print("\nChecking for SSH connection in port 22 using IP\n--------------------------------------------------------------\n\n")
for i in range(0,5):
 print("SSH Connection for the IP address 192.168.0.12%s\n" % i)
 try:
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.connect(("192.168.0.12%s" % i, 22))
 except Exception as ex:
    print("Status : FAIL\n",)
 else:
    print("Status : PASS\n")
    test_socket.close()


print("\nChecking for SSH connection in port 22 using hostnames\n--------------------------------------------------------------\n\n")
hosts = ["frontend-1", "frontend-2", "backend-1", "backend-2", "controller"]
for i in hosts:
 print("SSH Connection for the hostname %s\n" % i)
 try:
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.connect((i, 22))
 except Exception as ex:
    print("Status : FAIL\n",)
 else:
    print("Status : PASS\n")
    test_socket.close()


print("\nChecking for SSH connection using password from controller node\n--------------------------------------------------------------\n\n")
for i in range(0,4):
 print("SSH Connection for the IP address 192.168.0.12%s\n" % i)
 try:
    output = subprocess.check_output(
        "vagrant ssh controller -c \"ssh -o PreferredAuthentications=password 192.168.0.12%s\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=15,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
 else:
    print("Status : PASS\n\n{}\n".format(output))


print("\nChecking for port 80 in frontend-1 and frontend-2\n--------------------------------------------------------------\n\n")
for i in range(0,2):
 print("Web Request to 192.168.0.12%s:80\n" % i)
 try:
    output = subprocess.check_output(
        "curl 192.168.0.12%s:80 -s" % i, stderr=subprocess.STDOUT, shell=True, timeout=15,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
 else:
    print("Status : PASS\n\n{}\n".format(output))



print("\nChecking for Mariadb Installation in backend-1 and backend-2\n--------------------------------------------------------------\n\n")
hosts = ["backend-1", "backend-2"]
for i in hosts:
 print("Mariadb installation for the hostname: %s\n" % i)
 try:
    output = subprocess.check_output(
        "vagrant ssh %s -c \"mariadb --version\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
 else:
    print("Status : PASS\n\n{}\n".format(output))




print("\nChecking for MYSQL root login using the password 'fred' in backend-1 and backend-2\n--------------------------------------------------------------\n\n")
hosts = ["backend-1", "backend-2"]

for i in hosts:
 print("MYSQL root login using the password 'fred' in the host: %s\n" % i)
 try:
    output = subprocess.check_output(
        "vagrant ssh %s -c \"echo -e '[mysql]\nuser = root\npassword = fred' > ~/.my.cnf\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL - Not able to configure .my.cnf file for %s host\n" % i, exc.returncode, exc.output)
 else:
    try:
      output = subprocess.check_output(
        "vagrant ssh %s -c \"mysql -u root -e 'select user()'\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
    except subprocess.CalledProcessError as exc:
      print("Status : FAIL\n", exc.returncode, exc.output)
    else:
      print("Status : PASS\n\n{}\n".format(output))


print("\nChecking for MYSQL user 'foo' login using the password 'far' in backend-1 and backend-2\n--------------------------------------------------------------\n\n")
hosts = ["backend-1", "backend-2"]

for i in hosts:
 print("MYSQL user 'foo' login using the password 'far' in the host: %s\n" % i)
 try:
    output = subprocess.check_output(
        "vagrant ssh %s -c \"echo -e '[mysql]\nuser = foo\npassword = far' > ~/.my.cnf\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL - Not able to configure .my.cnf file for %s host\n" % i, exc.returncode, exc.output)
 else:
    try:
      output = subprocess.check_output(
        "vagrant ssh %s -c \"mysql -u foo -e 'select user()'\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
    except subprocess.CalledProcessError as exc:
      print("Status : FAIL\n", exc.returncode, exc.output)
    else:
      print("Status : PASS\n\n{}\n".format(output))



print("\nChecking for Vim Installation in all the hosts\n--------------------------------------------------------------\n\n")
hosts = ["frontend-1", "frontend-2", "backend-1", "backend-2", "controller"]
for i in hosts:
 print("Vim installation for the hostname: %s\n" % i)
 try:
    output = subprocess.check_output(
        "vagrant ssh %s -c \"vim --version\"" % i, stderr=subprocess.STDOUT, shell=True, timeout=50,
        universal_newlines=True).rstrip()
 except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
 else:
    print("Status : PASS\n")


print("\nChecking for Ansible Installation in the controller\n--------------------------------------------------------------\n\n")
try:
    output = subprocess.check_output(
        "vagrant ssh controller -c \"ansible --version\" | head -n 1", stderr=subprocess.STDOUT, shell=True, timeout=30,
        universal_newlines=True).rstrip()
except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)
else:
    print("Status : PASS\n\n{}\n".format(output))



print("\nChecking for connected_users.yml file in the controller\n--------------------------------------------------------------\n\n")
try:
    output = subprocess.check_output(
        "vagrant ssh controller -c \"sudo find / -name connected_users.yml 2>/dev/null\"", stderr=subprocess.STDOUT, shell=True, timeout=30,
        universal_newlines=True).rstrip()

    #print(len(output))
    #print("lalal")
    lala = re.sub(r'^Connection.*\n?', '', output, flags=re.MULTILINE)
    #print(lala.strip())
    #print(output.strip().rsplit("\n",2)[0])
    #print("lalal")
    if re.match(r'^\s*$', lala):
       print("Status : FAIL\n")
    else:
       print("Status : PASS\n\n{}\n".format(output))
except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)


print("\nChecking for output files of the \"w\" command executed on all machines by the controller node\n--------------------------------------------------------------\n\n")
try:
    output = subprocess.check_output(
        "vagrant ssh controller -c \"sudo find / -name 'connected_users_*' 2>/dev/null\"", stderr=subprocess.STDOUT, shell=True, timeout=30,
        universal_newlines=True).rstrip()
    lala = re.sub(r'^Connection.*\n?', '', output, flags=re.MULTILINE)
    if re.match(r'^\s*$', lala):
       print("Status : FAIL\n")
    else:
       length = lala.count('\n')
       if (length >= 4):
         print("Status : PASS\n\n{}\n".format(output))
       else:
         print("Status : FAIL\n")
except subprocess.CalledProcessError as exc:
    print("Status : FAIL\n", exc.returncode, exc.output)










