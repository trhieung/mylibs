

import sys
import os
from pathlib import Path

# Add cve path to sys.path
data_path = Path(__file__).resolve().parent
sys.path.append(str(data_path))

# -------------------------
from glucus.core import callGraph
callGraph.run([os.path.join(data_path, 'test.py')])

#