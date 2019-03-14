#!/usr/bin/env python3
"""moving files with SFTP"""

import os ## allows low level agnostic OS access
import paramiko ## make SSH connections

def main():
    listofmachines = [{"ip" : "10.10.2.3", "un" : "bender"}, {"ip" : "10.10.2.4", "un" : "fry"}, {"ip" : "10.10.2.5", "un" : "zoidberg"}]
    for machine in listofmachines:

        t = paramiko.Transport(machine["ip"], 22) ## connection obj IP/ port
        t.connect(username = machine["un"], password= "alta3")

        sftpobj = paramiko.SFTPClient.from_transport(t)

        sftpobj.put("fake.conf", "fake.moved.obj")

        sftpobj.close()
        t.close()
main()
