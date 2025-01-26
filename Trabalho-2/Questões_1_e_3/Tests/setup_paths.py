import sys
from pathlib import Path

def setup():
    base_path = Path(__file__).resolve().parent.parent
    classes_path = base_path / 'Classes'
    sys.path.append(str(classes_path))