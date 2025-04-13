import sys
from pathlib import Path

# Add project path to sys.path
data_path = Path(__file__).resolve().parent.parent
sys.path.append(str(data_path))

# pyan3 utils.py test.py --dot --imported-by --grouped > callgraph.dot && dot -Tpng callgraph.dot -o callgraph.png