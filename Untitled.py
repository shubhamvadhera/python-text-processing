
# coding: utf-8

# In[61]:

import csv
import os

source_dir = 'C:\\Users\\svadhera\\Documents\\inputfiles\\'
target_dir = source_dir + '\\processed\\'
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
mainlist=[]
head=True
for root,dirs,files in os.walk(source_dir):
    for fil in files:
        if not fil.endswith(".txt"):
            continue
        inputfile = os.path.join(source_dir,fil)
        input_set = []
        newinp = []
        colinput = []
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
        #print input_set
        for inp in input_set:
            if head:
                col = inp.split(':',1)[0]
                colinput.append(col.strip())
            col = inp.split(':',1)[1]
            newinp.append(col.strip())
            #writer.writerow(newinp)
            #print(newinp)
        if head:
            mainlist.append(colinput)
            head=False
        mainlist.append(newinp)
#print(zip(*mainlist))
with open(target_dir+'out.csv','wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for x in mainlist:
        writer.writerow(x)


# In[ ]:




# In[ ]:



