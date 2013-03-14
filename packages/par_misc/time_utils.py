# utility functions related to process date and time
from time import strftime


def Normalize_DateTime(dt):
    # convert date time into integers
    chs = ['-', ' ', ':']
    for ch in chs:
        dt = dt.replace(ch, '')
    return int(dt)


def Compare_DateTime(dt1, dt2):
    # return true if dt2 is later than dt1
    dtint1 = Normalize_DateTime(dt1)
    dtint2 = Normalize_DateTime(dt2)
    if dtint1 < dtint2:
        return True
    else:
        return False


def Is_Same_Minute(dt1, dt2):
    # return true if dt2 is in the same minute as dt1
    chs = ['-', ' ', ':']
    for ch in chs:
        dt1 = dt1.replace(ch, '')
        dt2 = dt2.replace(ch, '')
    if dt1[:12] == dt2[:12]:
        return True
    else:
        return False


def Get_Timestamp():
    ctime = strftime("%Y-%m-%d-%H-%M-%S")
    return str(ctime).replace('-', '')
