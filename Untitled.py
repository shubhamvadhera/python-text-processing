
# coding: utf-8

# In[44]:

import csv
import os

source_dir = 'C:\\Users\\svadhera\\Documents\\inputfiles\\'
target_dir = source_dir + '\\processed\\'
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for root,dirs,files in os.walk(source_dir):
    for fil in files:
        if not fil.endswith(".txt"):
            continue
        inputfile = os.path.join(source_dir,fil)
        input_set = []
        with open(inputfile) as inputs:
            for line in inputs:
                currLine = line.strip()
                if currLine == '':
                    continue
                if '*****' in currLine:
                    break
                input_set.append(currLine)
        for line in reversed(open(inputfile).readlines()):
            currLine = line.strip()
            if currLine == '' or '*' in currLine:
                continue
            input_set.append(currLine)
            if 'Test Result' in currLine:
                break
        print input_set
        
        with open(target_dir+fil+'_out.csv','wb') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for inp in input_set:
                    lis = inp.split(':',1)
                    lis = [x.strip() for x in lis]
                    writer.writerow(lis)
    


# In[ ]:




# In[ ]:



