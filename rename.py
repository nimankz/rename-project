import os, glob

pathlist=glob.glob(os.path.join(r"C:\Users\GreenLeaf\Desktop\practice\extra practice",'*.py'))
mylist=[]
for item in pathlist:
	print(item)
	item=item.split("\\")
	print(item)
	mylist.append(item[-1])

print(mylist)
# for python_file in glob.glob(os.path.join('*.py')):
#     print (python_file)

# old_file=os.path.join("myFile.txt")
# new_file=os.path.join("yourFile.txt")

# os.rename(old_file,new_file)
