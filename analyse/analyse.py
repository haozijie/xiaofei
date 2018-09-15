import pandas as pd
# import matplotlib.pyplot as plt
def analyse_user():
	df_activity = pd.read_csv('../rawData/user_activity_log.txt',sep='\t',names=['user_id','day','page','video_id','author_id','action_type']) 
	# df_launch = pd.read_csv('../data/app_launch_log.txt',sep='\t')
	# print df_activity.describe()
	df_activity_lasted7 = df_activity[(df_activity['day']>=24) & (df_activity['day']<=30)]
	activity_user = set()
	for index,row in df_activity_lasted7.iterrows():
		if index % 10000 == 0:
			print index
			# break
		activity_user.add(row['user_id'])
	all_num = len(activity_user)
	print 'activity user number = {0}'.format(all_num)

	df = df_activity[df_activity['day']<24]
	dict_user2time = {}
	for index,row in df.iterrows():
		if index == 100000:
			print index
		if row['user_id'] not in activity_user:
			continue
		if dict_user2time.has_key(row['user_id']):
			if row['day']>dict_user2time[row['user_id']]:
				dict_user2time[row['user_id']] = row['day']
		else:
			dict_user2time[row['user_id']] = row['day']

	dict_day2num = {}
	for key,value in dict_user2time.iteritems():
		day = 24-value
		dict_day2num[day] = dict_day2num.get(day,0)+1
	list_num = sorted(dict_day2num.iteritems(),key=lambda d:d[0],reverse=False)
	x = []
	y = []
	count = 0
	for item in list_num:
		x.append(item[0])
		y.append(item[1])
		count += float(item[1])
		print float(count)/float(all_num)
	plt.plot(x,y)
	plt.show()


def analyse_launch_activity():
	df_launch = pd.read_csv('../rawData/app_launch_log.txt',sep='\t',names=['user_id','day'])
	df_activity = pd.read_csv('../rawData/user_activity_log.txt',sep='\t',names=['user_id','day','page','video_id','author_id','action_type'])
	start = 24
	end = 30
	df_launch = df_launch[(df_launch['day']>=start)&(df_launch['day']<=end)]
	df_activity = df_activity[(df_activity['day']>=start)&(df_activity['day']<=end)]
	user1 = set()
	user2 = set()
	for index,row in df_launch.iterrows():
		user1.add(row['user_id'])
	print 'launch tabel has {0}'.format(len(user1))
	# for index,row in df_activity.iterrows():
	# 	user2.add(row['user_id'])
	df_activity = df_activity.drop_duplicates(subset='user_id')
	print 'activity tabel has {0}'.format(len(df_activity))
	# print 'jiaoji has {0}'.format(len(user1&user2))





if __name__ == '__main__':
	analyse_launch_activity()