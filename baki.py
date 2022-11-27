from dirsync import sync
import os

source = 'D:\\family'
target = 'E:\\family'

try:
    os.mkdir(target)
except OSError as error:
    print(error)
sync(source, target, 'sync', purge=True)