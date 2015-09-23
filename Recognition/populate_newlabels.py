import os
'''
trainList = []
folderList = []

for folder in os.listdir('/home/avik/overfeat/third_eye/Images'):
	contents = os.listdir('/home/avik/overfeat/'+folder)
	trainList.append(contents)
	folderList.append(append)

f = open('/home/avik/overfeat/third_eye/labels.txt','w')

for folder in folderList:
'''

aList = os.listdir('/home/avik/overfeat/third_eye/Images/A')
bList = os.listdir('/home/avik/overfeat/third_eye/Images/B')
cList = os.listdir('/home/avik/overfeat/third_eye/Images/C')
dList = os.listdir('/home/avik/overfeat/third_eye/Images/D')
eList = os.listdir('/home/avik/overfeat/third_eye/Images/E')
fList = os.listdir('/home/avik/overfeat/third_eye/Images/F')
gList = os.listdir('/home/avik/overfeat/third_eye/Images/G')
hList = os.listdir('/home/avik/overfeat/third_eye/Images/H')
iList = os.listdir('/home/avik/overfeat/third_eye/Images/I')
jList = os.listdir('/home/avik/overfeat/third_eye/Images/J')
lList = os.listdir('/home/avik/overfeat/third_eye/Images/L')
mList = os.listdir('/home/avik/overfeat/third_eye/Images/M')
nList = os.listdir('/home/avik/overfeat/third_eye/Images/N')
oList = os.listdir('/home/avik/overfeat/third_eye/Images/O')
pList = os.listdir('/home/avik/overfeat/third_eye/Images/P')


#f = open('/home/avik/overfeat/Images/labels.txt','w')
f = open('/home/avik/overfeat/third_eye/labels.txt','w')

for image in aList:
	f.write(image + ',A\n')

for image in bList:
	f.write(image + ',B\n')

for image in cList:
	f.write(image + ',C\n')

for image in dList:
	f.write(image + ',D\n')

for image in eList:
	f.write(image + ',E\n')

for image in fList:
	f.write(image + ',F\n')

for image in gList:
	f.write(image + ',G\n')

for image in hList:
	f.write(image + ',H\n')

for image in iList:
	f.write(image + ',I\n')

for image in jList:
	f.write(image + ',J\n')

for image in lList:
	f.write(image + ',L\n')

for image in mList:
	f.write(image + ',M\n')

for image in nList:
	f.write(image + ',N\n')

for image in oList:
	f.write(image + ',O\n')

for image in pList:
	f.write(image + ',P\n')



