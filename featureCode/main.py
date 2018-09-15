import os
import codecs
import time
import pandas as pd 
from extract_features import extract_user_feature,extract_ua_feature

###function: generate label file
def gen_labels(df_launch,start,end,filename):
	print 'write labels to file: {0}'.format(filename)
	user_set = set()     ### record activity user in future 7 days
	with codecs.open(filename,mode='w',encoding='utf-8') as fout:
		df_launch = df_launch[(df_launch['day']>=start) & (df_launch['day']<=end)]
		for index,row in df_launch.iterrows():
			if row['user_id'] not in user_set:
				user_set.add(row['user_id'])
				fout.write(str(row['user_id'])+','+'1'+'\n')
	print 'finished!'
###function2: generate label file based activity table
def gen_labels1(df_activity,start,end,filename):
	print 'write labels to file: {0}'.format(filename)
	with codecs.open(filename,mode='w',encoding='utf-8') as fout:
		df_activity = df_activity[(df_activity['day']>=start) & (df_activity['day']<=end)]
		df_activity = df_activity.drop_duplicates(subset='user_id')
		for index,row in df_activity.iterrows():
				fout.write(str(row['user_id'])+','+'1'+'\n')
	print 'finished!'


###function: feature engineer
def feature_engineer(df_register,df_launch,df_create,df_activity,start,end,filename):
	ua_features,user_all,feature_num2 = extract_ua_feature(df_launch,df_create,df_activity,start,end)
	user_features,user_candidate,feature_num1 = extract_user_feature(df_register,start,end,user_all)

	print 'feature engineering to file: {0}'.format(filename)
	with codecs.open(filename,mode='w',encoding='utf-8') as fout:
		for user_id in user_all:
			if user_id not in user_candidate:
				continue
			line = ''

			if user_id in user_features:
				for item in user_features[user_id]:
					line += str(item)+',' 
			else:
				line += '-1,'*feature_num1

			if user_id in ua_features:
				for item in ua_features[user_id]:
					line += str(item)+','
			else:
				line += '0,'*feature_num2

			fout.write(str(user_id)+','+line.strip(',')+'\n')
	print 'finished!'



	
###input: phase='train' or 'test' or 'inference'
def main(phase='train'):
	#####Determine whether to divide the dataset####
	print 'read all data flies...'
	df_register = pd.read_csv('../rawData/user_register_log.txt',sep='\t',names=['user_id','register_day','register_type','device_type'])
	df_launch = pd.read_csv('../rawData/app_launch_log.txt',sep='\t',names=['user_id','day'])   ### user_id  day
	df_create = pd.read_csv('../rawData/video_create_log.txt',sep='\t',names=['user_id','day'])  ### user_id  day
	df_activity = pd.read_csv('../rawData/user_activity_log.txt',sep='\t',names=['user_id','day','page','video_id','author_id','action_type'])
	
	train_start = 2
	train_end = 16
	train_feature_file = '../cacheData/'+'train_feature_'+str(train_start)+'_'+str(train_end)+'.csv'
	train_label_start = 17
	train_label_end = 23
	train_label_file = '../cacheData/'+'train_labe_'+str(train_label_start)+'_'+str(train_label_end)+'.csv'

	test_start = 9
	test_end = 23
	test_feature_file = '../cacheData/'+'test_feature_'+str(test_start)+'_'+str(test_end)+'.csv'
	test_label_start = 24
	test_label_end = 30
	test_label_file = '../cacheData/'+'test_labe_'+str(test_label_start)+'_'+str(test_label_end)+'.csv'

	inference_start = 16
	inference_end = 30
	inference_feature_file = '../cacheData/'+'inference_feature_'+str(inference_start)+'_'+str(inference_end)+'.csv'
	print 'finished!'

	#####generate feature files & label files####
	if phase == 'train':
		print 'goto phase = train...'
		if not os.path.exists(train_feature_file):
			feature_engineer(df_register,df_launch,df_create,df_activity,train_start,train_end,train_feature_file)
		else:
			print 'has existed train feature file'

		if not os.path.exists(train_label_file):
			gen_labels1(df_activity,train_label_start,train_label_end,train_label_file)
		else:
			print 'has existed label file'

	elif phase == 'test':
		print 'goto phase = test...'
		if not os.path.exists(test_feature_file):
			feature_engineer(df_register,df_launch,df_create,df_activity,test_start,test_end,test_feature_file)
		else:
			print 'has existed test feature file'
		if not os.path.exists(test_label_file):
			gen_labels1(df_activity,test_label_start,test_label_end,test_label_file)
		else:
			print 'has existed test label file'

	elif phase == 'inference':
		print 'goto phase = inference...'
		if not os.path.exists(inference_feature_file):
			feature_engineer(df_register,df_launch,df_create,df_activity,inference_start,inference_end,inference_feature_file)
		else:
			print 'has existed inference feature file'


if __name__ == '__main__':
	start = time.time()
	main(phase='inference')
	print 'cost time = {0}'.format(round(time.time()-start,2))