def foo(num):
	for i in range(1,num+1):
		if(i%105==0):
			print('Fizz Buzz Fun')
		elif(i%15==0):
			print('Fizz Buzz')
		elif(i%21==0):
			print('Fizz Fun')
		elif(i%35==0):
			print('Buzz Fun')
		elif(i%3==0):
			print('Fizz')
		elif(i%5==0):
			print('Buzz')
		elif(i%7==0):
			print('Fun')
		else:
			print(i)
if __name__=='__main__':
	num=50
	foo(num)