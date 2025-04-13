import sys
from pathlib import Path

# Add project path to sys.path
data_path = Path(__file__).resolve().parent.parent
sys.path.append(str(data_path))

from core import *

def run_poc():
    print(f'Hi from run_poc() of {PROJECT_NAME}')