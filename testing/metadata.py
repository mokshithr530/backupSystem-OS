import os
file= "files\\files.txt" #if u use single hash it treats it like a escape sequence
stat=os.stat(file)
print(stat.st_mtime)
print(stat.st_size)

#yes it changes
