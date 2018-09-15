import time
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
import utils

def train_gbdt(phase='online'):
	print 'loading train dataset...'
	train_x,train_y = utils.load_data('../cacheData/train_feature_2_16.csv','../cacheData/train_labe_17_23.csv')
	print 'start training gbdt...'
	p = {'lr':0.05,'number':200,'depth':3,'feature_ratio':0.9,'sample_ratio':0.9}
	clf = GradientBoostingClassifier(loss='exponential',learning_rate=p['lr'],n_estimators=p['number'],\
		max_depth=p['depth'],max_features=p['feature_ratio'],subsample=p['sample_ratio'],verbose=1)
	clf.fit(train_x,train_y)
	print 'finished!'

	filename = 'gbdt_'+str(len(train_x[0]))+'_'+str(int(time.time()))+'_'+phase+\
	'_lr'+str(p['lr'])+'_num'+str(p['number'])+'_depth'+str(p['depth'])+'_fr'+str(p['feature_ratio'])+\
	'_sr'+str(p['sample_ratio'])+'.m'
	joblib.dump(clf,'./modelFiles/'+filename)


if __name__ == '__main__':
	train_gbdt(phase='online')
