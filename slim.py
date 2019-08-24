import os

from const import source_path
from const import target_path
from const import nu_path

def slim():
    print("字体库瘦身开始");
    
    if os.path.isfile(nu_path):
        f = open(nu_path, 'r', encoding='UTF-8')
        genstr = f.read()
    out = ''
    for dir in os.listdir(source_path): 
        child = os.path.join(source_path, dir)
        #print(child)
        if os.path.isfile(child):
            out += "java -jar sfnttool.jar  -s " + genstr + " " + child  + " " +  child.replace(source_path,target_path) + ' && '
            
         
    os.system(out[:-4])
    
    print("字体库瘦身结束");
    
    
    


