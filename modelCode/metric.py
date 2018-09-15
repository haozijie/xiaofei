import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
import utils
import pdb
def test_gbdt():
	print 'loading test dataset...'
	users,test_x,user_launch = utils.load_data4test('../cacheData/test_feature_9_23.csv','../cacheData/test_labe_24_30.csv')
	clf = joblib.load('./modelFiles/gbdt_55_1529322572_online_lr0.05_num200_depth3_fr0.9_sr0.9.m')
	predict_y = clf.predict_proba(test_x)
	user2predict = {}
	# pdb.set_trace()
	length = len(users)
	for i in range(0,length):
		user2predict[users[i]] = predict_y[i][1]   ###predict 1 proba
	user2predict_list = sorted(user2predict.iteritems(),key=lambda d:d[1],reverse=True)


	thresholds = [0.7,0.6,0.55,0.5,0.45,0.4,0.3]
	result = 0
	best_threshold = 0
	best_count = 0
	for threshold in thresholds:
		count = 0
		count_correct = 0		
		for item in user2predict_list:
			if item[1] < threshold:
				break
			count += 1
			user_id = item[0]
			if user_id in user_launch:
				count_correct += 1
		f1 = metric(count,count_correct,len(user_launch))
		if f1>result:
			result = f1
			best_threshold = threshold
			best_count = count
	print 'best F1 = {0}'.format(result)
	print 'best threshold = {0}'.format(best_threshold)
	print 'best count = {0}'.format(best_count)


def metric(count1,count2,count3):
	p = float(count2)/float(count1)
	r = float(count2)/float(count3)
	f1 = (2*p*r)/(p+r)
	return f1



if __name__ == '__main__':
	test_gbdt()