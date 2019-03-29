present=int(input("enter the no of classes attended by varun till now:"))
total_1=int(input("enter the no of classes taken till now:"))
total=int(input("total no of classes:"))
percent_p=(present/total_1)*100
print(percent_p)
if percent_p<75:
	print("shortage of attendace and varun need to attend 42 classes out of 56 to maintain 75%")
else:
	print("varun has maintained his attendance")
    
