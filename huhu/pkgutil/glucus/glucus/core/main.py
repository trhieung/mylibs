import sys
from pathlib import Path

# Add cve path to sys.path
data_path = Path(__file__).resolve().parent.parent
sys.path.append(str(data_path))

from core.prod import *
