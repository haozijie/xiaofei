import codecs
def load_data(feature_file,label_file):
	x = []
	y = []
	user2feature = {}
	user2label = {}
	with codecs.open(feature_file,mode='r',encoding='utf-8') as fin:
		for line in fin:
			lines = line.strip().split(',')
			user2feature[lines[0]] = map(float,lines[1:])
	with codecs.open(label_file,mode='r',encoding='utf-8') as fin:
		for line in fin:
			lines = line.strip().split(',')
			user2label[lines[0]] = lines[1:]
	for user_id,feature in user2feature.iteritems():
		x.append(feature)
		if user2label.has_key(user_id):
			y.append([1])
		else:
			y.append([0])
	return x,y

def load_data4test(feature_file,label_file):
	users  = []
	x = []
	user_launch = set()
	user2feature = {}
	user2label = {}
	with codecs.open(feature_file,mode='r',encoding='utf-8') as fin:
		for line in fin:
			lines = line.strip().split(',')
			user2feature[lines[0]] = map(float,lines[1:])
	with codecs.open(label_file,mode='r',encoding='utf-8') as fin:
		for line in fin:
			lines = line.strip().split(',')
			user2label[lines[0]] = lines[1:]
	for user_id,feature in user2feature.iteritems():
		users.append(user_id)
		x.append(feature)
		if user2label.has_key(user_id):
			user_launch.add(user_id)
	return users,x,user_launch

def load_data4inference(feature_file):
	users  = []
	x = []
	user2feature = {}
	with codecs.open(feature_file,mode='r',encoding='utf-8') as fin:
		for line in fin:
			lines = line.strip().split(',')
			user2feature[lines[0]] = map(float,lines[1:])
	for user_id,feature in user2feature.iteritems():
		users.append(user_id)
		x.append(feature)
	return users,x