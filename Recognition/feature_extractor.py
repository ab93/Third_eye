import os

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

testlist = os.listdir('/home/avik/overfeat/third_eye/Images/Test')

trainlist = aList+bList+cList+dList+eList+fList+gList+hList+iList+jList+lList+mList+nList+oList+pList

g = open('/home/avik/overfeat/third_eye/labels.txt','r')

label_dict = {}

for line in g:
	line = line.strip().split(',')
	image = line[0]
	label = line[1]
	label_dict[image] = label

print label_dict


print "Extracting training features....!"

image_number = 0
for image in trainlist:
	label = label_dict[image]
	image_path = '/home/avik/overfeat/third_eye/Images/' + label + '/' + image
	os.system(' echo ' + image +' '+ label + '>> train_features' )
	os.system('/home/avik/overfeat/bin/linux_64/overfeat -f ' + image_path + ' >> train_features')
	image_number += 1
	print image_number

print "Extracting testing features.....!"



image_number = 0
for image in testlist:
	image_path = '/home/avik/overfeat/third_eye/Images/Test/' + image 
	os.system(' echo ' + image + '>> test_features' )
	os.system('/home/avik/overfeat/bin/linux_64/overfeat -f ' + image_path + ' >> test_features')
	image_number+= 1
	print image_number
