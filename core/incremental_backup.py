from core.scanner import scan_dir
from core.helper_metadata import load_metadata, save_metadata, is_modified
import os 
import shutil


def incremental_backup(source, destination):

    metadata = load_metadata()
    all_files = scan_dir(source)
    new_meta = {}

    for file_path in all_files:

        stat = os.stat(file_path) 

        if is_modified(file_path, metadata):

            print("Copying:", file_path)

            relative = os.path.relpath(file_path, source)
            dest_file = os.path.join(destination, relative)

            os.makedirs(os.path.dirname(dest_file), exist_ok=True)

            shutil.copy2(file_path, dest_file)

        else:
            print("Skipping:", file_path)

        new_meta[file_path] = {
            "mtime": stat.st_mtime,
            "size": stat.st_size
        }

    save_metadata(new_meta)

    print("Incremental backup completed.")
        