
from core.scanner import scan_dir
from core.helper_metadata import load_metadata, save_metadata, is_modified
from concurrent.futures import ThreadPoolExecutor
import os 
import shutil
import time

def copyfile(argument):
    source_file, dest_file = argument

    os.makedirs(os.path.dirname(dest_file), exist_ok=True)

    shutil.copy2(source_file, dest_file)

    print("[COPY]", source_file)


def incremental_backup(source, destination):

    start_time = time.time()

    print("\n========================================")
    print("      Incremental Backup Started")
    print("========================================\n")

    metadata = load_metadata()
    all_files = scan_dir(source)
    new_meta = {}

    files_to_copy = []

    skipped = 0
    copied = 0

    for file_path in all_files:

        stat = os.stat(file_path)

        if is_modified(file_path, metadata):

            relative = os.path.relpath(file_path, source)
            dest_file = os.path.join(destination, relative)

            files_to_copy.append((file_path, dest_file))
            copied += 1

        else:
            print("[SKIP]", file_path)
            skipped += 1

        new_meta[file_path] = {
            "mtime": stat.st_mtime,
            "size": stat.st_size
        }

    print("\nStarting multithreaded copy...\n")

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(copyfile, files_to_copy)

    save_metadata(new_meta)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("\n----------------------------------------")
    print("Backup Summary")
    print("----------------------------------------")
    print("Total files scanned :", len(all_files))
    print("Files copied        :", copied)
    print("Files skipped       :", skipped)
    print("Time taken          :", total_time, "seconds")
    print("----------------------------------------\n")
