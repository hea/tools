import time
import datetime
import math
import os

ISOTIMEFORMAT='%Y-%m-%d %X'

CLOSETIME='17:30:00'

if __name__ == '__main__':
	date = time.strftime("%Y-%m-%d",time.localtime())
	dstart=datetime.datetime.now();
	dend=datetime.datetime.strptime(date+' '+CLOSETIME, "%Y-%m-%d %X")
	cha=dend-dstart;
	valuecha=int(math.ceil(cha.total_seconds())) 
	print valuecha
	os.system('shutdown -s -t '+str(valuecha))
