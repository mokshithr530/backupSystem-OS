import os
import json

METADATA_FILE = "backup_metadata.json"

def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {}
    else:
        with open(METADATA_FILE,"r") as f:
            return json.load(f)
        
def save_metadata(data):
    with open(METADATA_FILE,"w") as f:
        json.dump(data, f, indent=4)
        

def is_modified(file_path, metadata):
    # If file is not present in old metadata → NEW file
    if file_path not in metadata:
        return True

    # Get current file stats from OS
    stat = os.stat(file_path)
    current_mtime = stat.st_mtime
    current_size = stat.st_size

    # Get old stored metadata
    old_mtime = metadata[file_path]["mtime"]
    old_size = metadata[file_path]["size"]

    # Compare
    if current_mtime != old_mtime or current_size != old_size:
        return True

    return False