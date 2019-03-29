import csv

with open('file.csv','a',newline="") as myfile:
	wr = csv.writer(myfile,dialect='excel')
	wr.writerow(['game of trones','winter is coming'])
	wr.writerow(['game of trones','winter is coming'])
	wr.writerow(['game of trones','winter is coming'])
	wr.writerow(['game of trones','winter is coming'])
	wr.writerow(['game of trones','winter is coming'])

# with open('file.csv','r',newline="") as myfile:
# 	rd=csv.reader(myfile)
# 	print(rd)
# 	for i in rd:
# 		print(i)