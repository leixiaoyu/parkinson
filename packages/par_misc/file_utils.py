# utilities functions related to operations on files


def File_Len(file_path):
    # return number of rows in a file
    # full path, including file name, is needed
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Read_File(file_path):
    # return lists containing data within the given file
    # full path, including file name, is needed
    fname = file_path
    with open(fname, 'r') as f:
        f.next()
        matrix, row = [], []
        for line in f:
            temp = line.split(',')
            for e in temp[:-1]:
                try:
                    row.append(float(e))
                except:
                    print 'not able to convert: ' + e
                    row.append(-999)
            matrix.append(row)
            row = []
    return matrix
