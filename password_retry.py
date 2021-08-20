password = 'a123456'
x = 3
while x > 0:
	pwd = input('please enter ur password:')
	if pwd == password:
		print('succeed to log in!')
		break
	else:
		x = x - 1
		print('please enter again to log in,you have ' ,x ,'times left.')
		
	
		

 
