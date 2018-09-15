import time
import datetime
def timestamp2datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def datetime2timestamp(date):
	timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S") 
	timeStamp = int(time.mktime(timeArray)) 
	return timeStamp

def datetimeAdd(date,days):
	date_time = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')	
	day = (date_time + datetime.timedelta(days)).strftime('%Y-%m-%d %H:%M:%S')
	return day

def datetimeSubtract(date,days):
	if len(date.split(' ')) == 2:
		date_time = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
		day = (date_time - datetime.timedelta(days)).strftime('%Y-%m-%d %H:%M:%S')
	else:
		date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
		day = (date_time - datetime.timedelta(days)).strftime('%Y-%m-%d')
	return day

####inputs:
####date1->string  date2->string
####return:
####days->int
def detaTowDays(date1,date2):
	d1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
	d2 = datetime.datetime.strptime(date2,'%Y-%m-%d')
	days = ( d1 - d2 ).days
	return days

if __name__ == '__main__':
	date = "2017-04-30"
	days = 90
	print datetimeSubtract(date,days)