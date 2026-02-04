# System Backup Tool (Operating System Project)

## Overview
This project is a Python-based System Backup Tool designed to perform efficient and reliable backups using incremental backup techniques and multithreading.  
It demonstrates important Operating System concepts such as file handling, concurrency, metadata management, and thread-based parallelism.

---

## Features

### ✔ Implemented Features
- **Directory Scanner**  
  Recursively scans all files from a given source directory.

- **Incremental Backup**  
  Copies only newly added or modified files based on metadata comparison.

- **Multithreaded File Copying**  
  Uses ThreadPoolExecutor to perform parallel file copy operations for improved performance.

- **Metadata Management**  
  Stores file information (size and modification time) in JSON format to track changes.

- **Preserves File Permissions**  
  Uses `shutil.copy2()` to retain file metadata such as permissions and timestamps.

- **User-Friendly Console Output**
  Displays:
  - number of files scanned  
  - files copied  
  - files skipped  
  - total execution time  

---

## Technologies Used
- Python 3
- JSON for metadata storage
- OS module for file system operations
- Concurrent Futures for multithreading

---

## Project Structure

backupSystem-OS/
│
├── core/
│ ├── scanner.py
│ ├── incremental_backup.py
│ ├── helper_metadata.py
│
├── testing/
│ ├── backup.py
│
├── README.md


---

## How It Works

1. The scanner module scans the source directory and lists all files.
2. Metadata from the previous backup is loaded.
3. Each file is compared using:
   - modification time  
   - file size  
4. Only modified or new files are copied.
5. Copy operations are performed using multiple threads.
6. Updated metadata is saved for the next run.

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd backupSystem-OS
