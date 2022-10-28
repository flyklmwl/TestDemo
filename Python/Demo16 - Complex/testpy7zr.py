import py7zr
from tqdm import tqdm
import time


# archive = py7zr.SevenZipFile(r'e:\python-bak.7z', mode='r')
# archiveinfo = archive.archiveinfo()
# archive.extractall(path="e:/tmp")
# print(type(archive))
# print(archiveinfo.filename)
# print(archiveinfo.stat)
# print(archiveinfo.header_size)
# print(archiveinfo.uncompressed)
# print(archiveinfo.blocks)
# archive.close()

with zipfile.ZipFile('e:\python-bak.zip', 'r') as zipf:   
    for name in tqdm(zipf.namelist()[:1000],desc='Extract files', unit='files'):
        zipf.extract(name, path='e:\tmp')
    zipf.close()