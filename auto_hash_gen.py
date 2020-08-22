#Author : RKT
#Automatic generate hash password
import os
import sys
import hashlib
os.system("clear")
os.system("figlet -f standard Auto Hash Gen")
print
print "Author : Rahat Khan Tusar(RKT)"
print
print "Github : https://github.com/r3k4t"
print
ip = raw_input("Enter your password : ")
print
print "01"*2000000
print
print "+"*60
os.system("clear")
print "#"*12
print   " MD5 Hash "
print "#"*12
print
print  hashlib.md5(ip).hexdigest()
print
print "#"*12
print   " Sha1 Hash "
print "#"*12
print
print  hashlib.sha1(ip).hexdigest()
print
print "#"*12
print   " Sha256 Hash "
print "#"*12
print
print  hashlib.sha256(ip).hexdigest()
print
print "#"*12
print   " Sha512 Hash "
print "#"*12
print
print  hashlib.sha256(ip).hexdigest()
print 
print "*"*60
print "Thank you for using my program.bye"
print "*"*60
