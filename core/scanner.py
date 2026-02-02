import os

def scan_dir(start_path):
    final_files=[]
    for root,dirs,files in os.walk(start_path):
        for filenames in files:
            full_path=os.path.join(root,filenames)
            final_files.append(full_path)
    return final_files
