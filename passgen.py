import random
import sys
 
def pwgen1(length):



    keylist='0123456789'
    password=[]
 
    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)

def pwgen2(length):



    keylist='abcdefghijklmnopqrstuvwxyz'
    password=[]
 
    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)



def pwgen3(length):



    keylist='0123456789abcdefghijklmnopqrstuvwxyz'
    password=[]
 
    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)



def pwgen4(length):



    keylist='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password=[]
 
    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)



def pwgen5(length):
    i = 0
    password = []
    keylist = '!"#$%&()*+,-./0123456789:<=>?@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^'
    while len(password) < length:
	a_char = random.choice(keylist)
	password.append(a_char)
    return ''.join(password)



if __name__ == '__main__':

	if (len(sys.argv)) == 1:
		leng = input("Pass length:\t")
		times = 1
	else:
		leng = int(sys.argv[1])
		print (sys.argv[1] + " chars random passwords")
		if len(sys.argv) == 2:
			times = 1
		else:
			times = int(sys.argv[2])
			print ("for "+sys.argv[2]+" times")
			if len(sys.argv) == 4:
			    passfile = open(sys.argv[3], 'w')
			    print("writing in " + sys.argv[3] + " file")
			
			
	i = 0;
	strs = ''
	print("\n\t Numbers only")
	for i in range(times):
		strs = pwgen1(leng) + "\n"
		print (strs)
		if (len(sys.argv) == 4):
		    passfile.write(strs)
	print("\n\t Chars in low case only")
	for i in range(times):
		strs = pwgen2(leng) + "\n"
		print (strs)
		if (len(sys.argv) == 4):
		    passfile.write(strs)
	print("\n\t Numbers and low case chars")
	for i in range(times):
		strs = pwgen3(leng) + "\n"
		print (strs)
		if (len(sys.argv) == 4):
		    passfile.write(strs)
	print("\n\t Numbers and chars")
	for i in range(times):
		strs = pwgen4(leng) + "\n"
		print (strs)
		if (len(sys.argv) == 4):
		    passfile.write(strs)	
	print("\n\t All ASCII")
	for i in range(times):
		strs = pwgen5(leng) + "\n"
		print (strs)
		if (len(sys.argv) == 4):
		    passfile.write(strs)	
	if (len(sys.argv) == 4):
	    passfile.close()
