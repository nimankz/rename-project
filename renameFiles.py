import os,glob
pathlist=glob.glob(os.path.join(r"E:\movies","*"))
mylist=[]
for item in pathlist:
	# print(item)
	item=item.split("\\")
	# print(item)
	mylist.append(item[-1])

# print(mylist)
unLikedWords=[ 'x265',"1080p","softsub","DigiMoviez","BluRay","WEB-DL",'DigiMoviez_2', 'WEB-DL','SoftSub','REMASTERED','Digimoviez','BluRay', 'DigiMoviez']
newList=[]
for item in mylist:
	item=item.split(".")
	shouldBeRemoved=[]
	for x in item:
		# print(x)
		if (x in unLikedWords):
			# print(f"item removed:{x}")
			shouldBeRemoved.append(x)
	for i in shouldBeRemoved:
		item.remove(i)

	# print(item)
	newList.append(".".join(item))

# print(mylist)
# print(newList)
for item in range(len(newList)):
	oldFile=os.path.join(r"E:\movies",mylist[item])
	newFile=os.path.join(r"E:\movies",newList[item])
	os.rename(oldFile,newFile)