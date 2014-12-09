#!/usr/bin/python
import os
import subprocess

user = 'boada'
server = 'instrumentation.tamu.edu'

#open the ssh connection and move the files around.
p = subprocess.Popen(['ssh',user+'@'+server],shell=False,stdin=subprocess.PIPE)

p.stdin.write("cd backups\n")
p.stdin.write("rm -rf backup.3\n")
p.stdin.write("mv backup.2 backup.3 \n")
p.stdin.write("mv backup.1 backup.2 \n")
p.stdin.write("cd backup.0/ && find . -print | cpio -dpl ../backup.1/ \n")

# then close the ssh connection
p.stdin.write("exit\n")

p.wait()

# Now we are starting the actual backup process

flags = '-avz --delete --exclude=.gvfs/'
directory = '/home/steven/'

os.system("rsync "+flags+" "+directory+" "+user+"@"+server+":~/backups/backup.0/")

