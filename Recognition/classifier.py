from sklearn import svm
from sklearn import linear_model
import numpy as np 

clf  = svm.LinearSVC()

train_file = open('/home/avik/overfeat/third_eye/train_features')
labels_file = open('/home/avik/overfeat/third_eye/labels.txt')
test_file = open('/home/avik/overfeat/third_eye/test_features')

label_dict = {}

for line in labels_file:
	line = line.strip()
	line = line.split(',')
	image = line[0]
	label = line[1]
	label_dict[image] = label

line_number = -1
train_features = []
train_labels = []

for line in train_file:
	line_number += 1
	line = line.strip()
	line = line.split(" ")
	if len(line) == 2:
		image = line[0]
	elif len(line) == 3:
		continue
	else: 
		line = [float(i) for i in line]
		#print len(line)
		#if len(line) > 4096:
		#	print image,line_number			
		train_features.append(line[0:4096])
		train_labels.append(label_dict[image])

#print train_features
train_features = np.array(train_features).astype(np.float)
print train_features.shape 
train_labels = np.array(train_labels)	
print train_labels.shape

clf.fit(train_features,train_labels)	
#print clf.predict(test_feature_2)

test_features = []
test_id = []

line_number = -1
for line in test_file:
	line_number += 1
	line = line.strip().split(" ")
	if len(line) == 1:
		image = line[0]
		test_id.append(image)
	elif len(line) == 3:
		continue
	else: 
		line = [float(i) for i in line]			
		test_features.append(line[0:4096])
		
test_id = np.array(test_id)
test_features = np.array(test_features).astype(np.float)
print test_features.shape 

index = 0
for ID in test_id:
	print ID, clf.predict(test_features[index])
	index +=1

#print clf.predict(test_features)
#print test_id