# data file organizer
import shutil
import os
import tarfile


def ExtractFiles(src_folder, tgt_folder):
    files_full = os.listdir(src_folder)
    for f in files_full:
        if len(f) > 9:
            candidate_name = f.split('_')[1]
            target_folder = tgt_folder + candidate_name
            if not os.path.isdir(target_folder):
                os.makedirs(target_folder)
            tar = tarfile.open(src_folder + f)
            tar.extractall(target_folder)


def CleanDir(unzip_dir, csv_dir):
    walker = os.walk(unzip_dir)
    for path, dirs, files in walker:
        for f in files:
            if os.path.splitext(f)[1] == '.csv':
                candidate = f.split('_')[2]
                if not os.path.isdir(csv_dir + candidate):
                    os.makedirs(csv_dir + candidate)
                shutil.copyfile(path + '/' + f, csv_dir + candidate + '/' + os.path.basename(f))


def Merger(candidate, keyword, src_dir, tgt_dir):
    fout_name = candidate + '_' + keyword + '.csv'
    fout_fullpath = tgt_dir + fout_name
    if os.path.isfile(fout_fullpath):
        os.remove(fout_fullpath)
    fout = open(fout_fullpath, 'a+')
    t = 1
    for path, dirs, files in os.walk(src_dir):
        for f in files:
            if os.path.splitext(f)[1] == '.csv' and f.split('_')[1] == keyword:
                lines = open(path + f, 'r')
                if t == 1:
                    for line in lines:
                        fout.write(line)
                    t = 2
                else:
                    lines.next()
                    for line in lines:
                        fout.write(line)
    fout.close()


def Trivial_Fixer(can, can_wrg, keyword, src_dir, tgt_dir):
    f_org_n = can + '_' + keyword + '.csv'
    f_app_n = can_wrg + '_' + keyword + '.csv'
    f_out_nf = tgt_dir + f_org_n
    f_org = open(src_dir + f_org_n, 'r')
    f_out = open(f_out_nf, 'a+')
    for line in f_org:
        f_out.write(line)
    f_org.close()
    f_app = open(src_dir + f_app_n, 'r')
    f_app.next()
    for line in f_app:
        f_out.write(line)
    f_app.close()
    f_out.close()


def Convert_MetaFormat(src_file, tgt_dir, isPatient, startingNum):
    """convert original file into semi-meta format delimetered by comma"""
    tgt_file = tgt_dir + os.path.basename(src_file)[:-4] + '_meta.csv'
    fout = open(tgt_file, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i == 0:
                continue
            else:
                data = line.split(',')[1:-1]
                data.append(isPatient)
                data.append(str(startingNum + i))
                output = ''
                for d in data[:-1]:
                    output = output + d + ','
                output = output + data[-1]
                fout.write(output + '\n')
    fout.close()


def Csv_to_Meta(src_file, tgt_dir):
    """convert semi-meta format into meta format, separated by tabs"""
    tgt_file = tgt_dir + os.path.basename(src_file)[:-4] + '.meta'
    fout = open(tgt_file, 'w')
    with open(src_file, 'r') as fin:
        for line in fin:
            fout.write(line.replace(',', '\t'))
    fout.close()


def All_In_One(src_dir, tgt_dir, keyword, people):
    fout_name = 'total_records' + '_' + keyword + '.csv'
    fout_fullpath = tgt_dir + fout_name
    fout = open(fout_fullpath, 'w')
    for candidate in people:
        f_together = src_dir + candidate + '_' + keyword + '_meta_sample.csv'
        with open(f_together, 'r') as fin:
            for line in fin:
                fout.write(line)
