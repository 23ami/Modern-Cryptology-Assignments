
import pexpect

code = pexpect.spawn('/usr/bin/ssh student@172.27.26.188')
code.expect('student@172.27.26.188\'s password:')
code.sendline('cs641')
code.expect('Enter your group name: ', timeout=50) 
code.sendline("code_breaker")

code.expect('Enter password: ', timeout=50)
code.sendline("patraass")

code.expect('\r\n\r\n\r\nYou have solved 5 levels so far.\r\nLevel you want to start at: ', timeout=50)
# Note: After clearing level 3 this needs to be changed to "solved 4 levels so far"
code.sendline("5")

code.expect('.*')
code.sendline("go")

code.expect('.*')
code.sendline("wave")

code.expect('.*')
code.sendline("dive")

code.expect('.*')
code.sendline("go")

code.expect('.*')
code.sendline("read")
#print(code.before)
code.expect('.*')

f = open("plaintexts1.txt", 'r')
f1= open("ciphertexts1.txt",'w')

for line in f.readlines():
	li = line.split()
	for l in li:
		code.sendline(l)
		s = str(code.before)[48:64]
		f1.write(s)
		f1.write(" ")
		code.expect("Slowly, a new text starts*")	
		code.sendline("c")
		code.expect('The text in the screen vanishes!')
	f1.write("\n")

code.sendline("ffffffffffffffmu")
s = str(code.before)[48:64]
f1.write(s)
f1.write(" ")
code.close()
f.close()
f1.close()