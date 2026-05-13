import json
import difflib
from os import listdir, remove
from os.path import isfile, join

try:
    remove("./data/diff.txt")
except:
    pass

#dirs = ['datasets','linkedServices','notebooks','others','pipelines','sqlscripts','triggers','integrationRuntimes','dataflows','credentials','bigDataPools','sqlPools']
dirs = ['datasets','linkedServices','pipelines']
for dir in dirs:
    with open('data/diff.txt', 'a') as f:
        f.write('\n')
    file_dir1 = 'data/'+dir+'1/'
    file_dir2 = 'data/'+dir+'2/'

    onlyfiles = [f for f in listdir(file_dir1) if isfile(join(file_dir1, f))]
    for file in onlyfiles:
        message = ''
    
        filepath1 = file_dir1+file
        with open(filepath1) as f:
            text1 = f.read()

        filepath2 = file_dir2+file
        try:
            with open(filepath2) as f:
                text2 = f.read()
            diff = difflib.unified_diff(text1.splitlines(), text2.splitlines(), lineterm='')
            diff_string = '\n'.join(list(diff))
            if diff_string:
                message = filepath1[5:]+' (current dev env) is different than '+filepath2[5:] + ' (new dev2 env)\n'

                with open('data/'+dir+'_diffs/diff_'+file[:-5]+'.txt', 'w') as f:
                    f.write(diff_string)
        except Exception as e:
            print(e)
            message = filepath1[5:] + ' not found in new dev2 env\n'

        print(message)
        with open('data/diff.txt', 'a') as f:
            f.write(message)
