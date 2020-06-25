# CBackup firstly makes backup directory and config file so
# you need to run it once then in config you have to
# put path of directory

# Script automatically remove old backup seven days before

# if you want this script to makes backup everyday at 00:00
# I recommend you a CRON

from pathlib import Path
import os, shutil, sys, datetime

# get date seven days back
def sevenDaysBack():
    Previous_Date = datetime.datetime.today() - datetime.timedelta(days=7)
    dataBack = Previous_Date.strftime("%d-%m-%Y")
    return dataBack

Path("backup").mkdir(parents=True, exist_ok=True)

# empty src path
src = ""


#create config or open if exist
try:
    fo = open("config.txt","r")
    pass
    src = fo.read()
    src = src.replace("src: ","")
    fo.close()
except IOError:
   fo = open("config.txt","w+")
   fo.write("src: ")
   fo.close()
   exit()

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

today = datetime.date.today()

# today date - dd-mm-yy
d1 = today.strftime("%d-%m-%Y")

# path of script
sPath = os.path.dirname(os.path.realpath(__file__))

# Destination path
dst = sPath + "/backup/" + d1 + "/"

# create directory with present day
Path("backup/" + d1).mkdir(parents=True, exist_ok=True)

# date seven days before - dd-mm-yy
# and makes path for old backup
d2 = sevenDaysBack()
dirpath = Path(sPath + "/backup/",d2)

if(src != ""):
    copytree(src, dst)
    if dirpath.exists() and dirpath.is_dir:
        shutil.rmtree(dirpath)
    exit()
else:
    print("config is empty")
