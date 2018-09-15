import pandas as pd 

def extract_ua_feature(df_launch,df_create,df_activity,start,end):
	print 'start extract ua features...'
	user_set = set()
	features = {}
	feature_num = 0
	print 'all activity records = {0}'.format(len(df_activity))
	df_activity = df_activity[(df_activity['day']>=start) & (df_activity['day']<=end)]
	df_launch = df_launch[(df_launch['day']>=start) & (df_launch['day']<=end)]
	df_create = df_create[(df_create['day']>=start) & (df_create['day']<=end)]
	length = len(df_activity)/20
	print 'part activity records = {0}'.format(len(df_activity))
	count = 0
	for index,row in df_activity.iterrows():
		count += 1
		if count % length == 0:
			print 'has processed {}/20'.format(count/length)
		if row['user_id'] in user_set:
			continue
		user_set.add(row['user_id'])
		feature_list = []
		df = df_activity[df_activity['user_id']==row['user_id']]
		df1 = df_launch[df_launch['user_id']==row['user_id']]
		df2 = df_create[df_create['user_id']==row['user_id']]
		for deta_day in [1,3,7,15]:
			df_day = df[df['day']>(end-deta_day)]
			df1_day = df1[df1['day']>(end-deta_day)]
			df2_day = df2[df2['day']>(end-deta_day)]
			###action numbers
			feature_list.append(len(df_day[df_day['action_type']==0]))
			feature_list.append(len(df_day[df_day['action_type']==1]))
			feature_list.append(len(df_day[df_day['action_type']==2]))
			feature_list.append(len(df_day[df_day['action_type']==3]))
			feature_list.append(len(df_day[df_day['action_type']==4]))
			feature_list.append(len(df_day[df_day['action_type']==5]))
			###page numbers
			feature_list.append(len(df_day[df_day['page']==0]))
			feature_list.append(len(df_day[df_day['page']==1]))
			feature_list.append(len(df_day[df_day['page']==2]))
			feature_list.append(len(df_day[df_day['page']==3]))
			feature_list.append(len(df_day[df_day['page']==4]))
			###launch days
			feature_list.append(len(df1_day))
			###create days
			feature_list.append(len(df2_day))
		features[row['user_id']] = feature_list
		feature_num = len(feature_list)
	print 'finished!'
	return features,user_set,feature_num


def extract_user_feature(df_register,start,end,user_set):
	print 'start extract user features...'
	user_candidate = set()
	features = {}
	feature_num = 3
	for index,row in df_register.iterrows():
		if row['user_id'] not in user_set:
			continue
		if row['register_day'] <= end:
			user_candidate.add(row['user_id'])
		feature_list = []
		feature_list.append(end-row['register_day'])
		feature_list.append(row['register_type'])
		feature_list.append(row['device_type'])
		features[row['user_id']] = feature_list
	print 'finished!'
	return features,user_candidate,feature_num
