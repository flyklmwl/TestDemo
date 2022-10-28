from zipfile import ZipFile
from tqdm import tqdm
import os

# Open your .zip file
with ZipFile(file="e:/python-bak.zip") as zip_file:

    new_path = "e:/tmp"
    
    # Loop over each file
    for file in tqdm(iterable=zip_file.namelist(), total=len(zip_file.namelist())):

        
        # Extract each file to another directory
        # If you want to extract to current working directory, don't specify path
        zip_file.extract(member=file, path=new_path)
        
    for root,dirs,files in os.walk(new_path):
        for d in dirs:
            try:
                new_dname = d.encode('cp437').decode('gbk')
                os.rename(os.path.join(root, d), os.path.join(root, new_dname))
            except:
                new_dname = d.encode('cp437').decode('utf-8')
                os.rename(os.path.join(root, d), os.path.join(root, new_dname))  
    for root,dirs,files in os.walk(new_path):
        for f in files:
            try:
                new_name = f.encode('cp437').decode('gbk')
                os.rename(os.path.join(root, f), os.path.join(root, new_name))
            except:
                new_name = f.encode('cp437').decode('utf-8')
                os.rename(os.path.join(root, f), os.path.join(root, new_name))
