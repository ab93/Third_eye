import os

boardlist = os.listdir('/home/avik/overfeat/Images_new/Board')
chairlist = os.listdir('/home/avik/overfeat/Images_new/Chair')
desktoplist = os.listdir('/home/avik/overfeat/Images_new/Desktop')
extinguisherlist = os.listdir('/home/avik/overfeat/Images_new/Extinguisher')
godrejlist = os.listdir('/home/avik/overfeat/Images_new/Godrej')
loadlist = os.listdir('/home/avik/overfeat/Images_new/Load')
tanklist = os.listdir('/home/avik/overfeat/Images_new/Tank')

testlist = os.listdir('/home/avik/overfeat/Images_new/Test')

trainlist = boardlist+chairlist+desktoplist+extinguisherlist+godrejlist+loadlist+tanklist

g = open('/home/avik/overfeat/Images_new/labels.txt','r')

label_dict = {}

for line in g:
	line = line.strip().split(',')
	image = line[0]
	label = line[1]
	label_dict[image] = label

print label_dict

for image in trainlist:
	label = label_dict[image]
	image_path = '/home/avik/overfeat/Images_new/' + label + '/' + image
	os.system('convert ' + image_path + ' -resize 240x240\! ' + '/home/avik/overfeat/Images_new/' + label + '/' + image)

for image in testlist:
	image_path = '/home/avik/overfeat/Images_new/Test/' + image
	os.system('convert ' + image_path + ' -resize 240x240\! ' + '/home/avik/overfeat/Images_new/Test/' + image)