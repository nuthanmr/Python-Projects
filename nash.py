test1=int(input("test1"))
test2=int(input("test2"))
test3=int(input("test3"))
avg=0
if (test1>test3) and (test2>test3):
	avg=(test1+test2)/2
	print("avg=",avg)
elif(test2>test1) and (test3>test1):
	avg=(test2+test3)/2
	print("avg=",avg)
else:
	(test1>test2) and (test3>test2)
	avg=(test1+test3)/2
	print("avg=",avg)
