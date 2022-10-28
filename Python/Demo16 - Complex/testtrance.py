from tqdm import trange
from time import sleep
from zipfile import ZipFile

# with ZipFile(file="e:/python-bak.zip") as zip_file:
    # for file in tqdm(iterable=zip_file.namelist(), total=len(zip_file.namelist())):

lv = False
num0, num1 = 0, 1

with ZipFile(file="e:/python-bak.zip") as zip_file:
    for file in trange(len(zip_file.namelist()), desc='loop0', position = num0):
        zip_file.extract(member=file, path="e:/tmp")