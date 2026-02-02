import sys
from pathlib import Path

# Ensure project root is on sys.path so `from core...` works when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.scanner import scan_dir
from core.incremental_backup import incremental_backup



incremental_backup("C:\-----SEM4-----\projects\Operatingsystem\\files","C:\-----SEM4-----\projects\Operatingsystem\\testing")

