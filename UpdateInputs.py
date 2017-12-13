import re
import os


pattern1=re.compile("^\[rest://(.*)\]$")
pattern2=re.compile("endpoint =.*")
index=None
endpoint=None
flag=False
with open("inputs.conf",'r') as f, open("new_file.txt",'w') as f1:
    for line  in f:
        match1=re.search(pattern1,line)
        if match1:
            print("Found pattern1 on line: "+line)
            index=match1.group(1)
            
            with open("maplecroft_indices.txt") as maplecroft_indices:
                for lines in maplecroft_indices:
                    if index in lines:
                        lists=lines.split("|")
                        endpoint=lists[1]
                        flag=True
                        break
                    else:
                        flag=False
                        
        match2=pattern2.search(line)
        if match2 and flag==True:
            print(index+" --- "+endpoint);
            endpoint="endpoint = "+endpoint
            line=endpoint

        f1.write(line)

f.close()
f1.close()
os.remove('inputs.conf')  
os.rename("new_file.txt", 'inputs.conf')  
