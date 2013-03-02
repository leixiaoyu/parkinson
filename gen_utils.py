# general utilities

# date time comparer
# input format 2012-01-06 17:14:20

def Compare_DateTime(dt1, dt2):
	# return true if dt2 is later than dt1
	chs = [ '-', ' ', ':' ]
	for ch in chs:
		dt1 = dt1.replace(ch, '')
		dt2 = dt2.replace(ch, '')
	dtint1 = int(dt1)
	dtint2 = int(dt2)
	if dtint1 < dtint2:
		return True
	else:
		return False

def Is_Same_Minute(dt1, dt2):
	# return true if dt2 is in the same minute as dt1
	chs = [ '-', ' ', ':' ]
	for ch in chs:
		dt1 = dt1.replace(ch, '')
		dt2 = dt2.replace(ch, '')
	if dt1[:12] == dt2[:12]:
		return True
	else:
		return False
