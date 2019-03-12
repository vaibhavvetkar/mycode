#!/usr/bin/env python3

import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

##this is the private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

##add fingerprint to known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

##creds to connect
sshsession.connect(hostname="10.10.2.3", username = "bender", pkey = mykey)

##simple list of commands 
our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

for x in our_commands:
    print(commandissue(x).decode('utf-8'))