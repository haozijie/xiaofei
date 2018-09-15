import codecs
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
import utils
def inference_gbdt(feature_file,model_file):
	print 'loading inference dataset...'
	users,x = utils.load_data4inference(feature_file)
	clf = joblib.load(model_file)
	predict_y = clf.predict_proba(x)
	user2predict = {}
	length = len(users)
	for i in range(0,length):
		user2predict[users[i]] = predict_y[i][1]   ###predict 1 proba
	user2predict_list = sorted(user2predict.iteritems(),key=lambda d:d[1],reverse=True)

	print 'write result to file...'
	fout = codecs.open('../submit/gbdt_result_0618_night.csv',mode='w',encoding='utf-8')
	best_threshold = 0.4
	count = 0
	for item in user2predict_list:
		if item[1]<best_threshold:
			break
		count += 1
		fout.write(item[0]+'\n')
	print 'lasted 15 days activity user number = {0}'.format(length)
	print 'future 7 days activity user number = {0}'.format(count)
	fout.close()


if __name__ == '__main__':
	inference_gbdt(feature_file='../cacheData/inference_feature_16_30.csv',\
		model_file='./modelFiles/gbdt_55_1529322329_online_lr0.05_num200_depth3_fr0.8_sr0.8.m')