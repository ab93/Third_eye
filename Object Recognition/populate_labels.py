import os
'''
baglist = os.listdir('/home/avik/overfeat/Images/Bag')
bedlist = os.listdir('/home/avik/overfeat/Images/Bed')
booklist = os.listdir('/home/avik/overfeat/Images/Book')
bottlelist = os.listdir('/home/avik/overfeat/Images/Bottle')
chairlist = os.listdir('/home/avik/overfeat/Images/Chair')
chappallist = os.listdir('/home/avik/overfeat/Images/Chappal')
chargerlist = os.listdir('/home/avik/overfeat/Images/Charger')
cuplist = os.listdir('/home/avik/overfeat/Images/Cup')
doorlist = os.listdir('/home/avik/overfeat/Images/Door')
glasseslist = os.listdir('/home/avik/overfeat/Images/Glasses')
keylist = os.listdir('/home/avik/overfeat/Images/Key')
laptoplist = os.listdir('/home/avik/overfeat/Images/Laptop')
locklist = os.listdir('/home/avik/overfeat/Images/Lock')
mirrorlist = os.listdir('/home/avik/overfeat/Images/Mirror')
muglist = os.listdir('/home/avik/overfeat/Images/Mug')
penlist = os.listdir('/home/avik/overfeat/Images/Pen')
phonelist = os.listdir('/home/avik/overfeat/Images/Phone')
platelist = os.listdir('/home/avik/overfeat/Images/Plate')
shirtlist = os.listdir('/home/avik/overfeat/Images/Shirt')
shoelist = os.listdir('/home/avik/overfeat/Images/Shoe')
spoonlist = os.listdir('/home/avik/overfeat/Images/Spoon')
tablelist = os.listdir('/home/avik/overfeat/Images/Table')
walletlist = os.listdir('/home/avik/overfeat/Images/Wallet')
watchlist = os.listdir('/home/avik/overfeat/Images/Watch')
testlist = os.listdir('/home/avik/overfeat/Images/Test')
'''
boardlist = os.listdir('/home/avik/overfeat/Images_new/Board')
chairlist = os.listdir('/home/avik/overfeat/Images_new/Chair')
desktoplist = os.listdir('/home/avik/overfeat/Images_new/Desktop')
extinguisherlist = os.listdir('/home/avik/overfeat/Images_new/Extinguisher')
godrejlist = os.listdir('/home/avik/overfeat/Images_new/Godrej')
loadlist = os.listdir('/home/avik/overfeat/Images_new/Load')
tanklist = os.listdir('/home/avik/overfeat/Images_new/Tank')
testlist = os.listdir('/home/avik/overfeat/Images_new/Test')

#f = open('/home/avik/overfeat/Images/labels.txt','w')
f = open('/home/avik/overfeat/Images_new/labels.txt','w')

for image in boardlist:
	f.write(image + ',Board\n')

for image in chairlist:
	f.write(image + ',Chair\n')

for image in desktoplist:
	f.write(image+',Desktop')
	f.write('\n')

for image in extinguisherlist:
	f.write(image+',Extinguisher')
	f.write('\n')

for image in godrejlist:
	f.write(image+',Godrej')
	f.write('\n')

for image in loadlist:
	f.write(image+',Load')
	f.write('\n')

for image in tanklist:
	f.write(image+',Tank')
	f.write('\n')

'''
for image in cuplist:
	f.write(image+',Cup')
	f.write('\n')

for image in doorlist:
	f.write(image+',Door')
	f.write('\n')

for image in glasseslist:
	f.write(image+',Glasses')
	f.write('\n')

for image in keylist:
	f.write(image+',Key')
	f.write('\n')

for image in laptoplist:
	f.write(image+',Laptop')
	f.write('\n')

for image in locklist:
	f.write(image+',Lock')
	f.write('\n')

for image in mirrorlist:
	f.write(image+',Mirror')
	f.write('\n')

for image in muglist:
	f.write(image+',Mug')
	f.write('\n')

for image in penlist:
	f.write(image+',Pen')
	f.write('\n')

for image in phonelist:
	f.write(image+',Phone')
	f.write('\n')

for image in platelist:
	f.write(image+',Plate')
	f.write('\n')

for image in shirtlist:
	f.write(image+',Shirt')
	f.write('\n')

for image in shoelist:
	f.write(image+',Shoe')
	f.write('\n')

for image in spoonlist:
	f.write(image+',Spoon')
	f.write('\n')

for image in tablelist:
	f.write(image+',Table')
	f.write('\n')

for image in walletlist:
	f.write(image+',Wallet')
	f.write('\n')

for image in watchlist:
	f.write(image+',Watch')
	f.write('\n')
'''
for image in testlist:
	f.write(image+',Test')
	f.write('\n')
