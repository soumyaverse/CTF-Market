from string import ascii_lowercase as lowercase

lowcase = str(lowercase)

def decrypt(p):
	p_index = lowcase.find(p)
	return lowercase[p_index-1] # replace 1 according to your situation

encrypted_flag = input('Enter encrypted flag: ')
flag = ''
for p in encrypted_flag:
	flag+=decrypt(p)

print(flag)