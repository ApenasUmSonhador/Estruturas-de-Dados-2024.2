import sys
from pathlib import Path

def setup():
    # Caminho para a pasta 'Tests'
    base_path = Path(__file__).resolve().parent
    tests_path = base_path / 'Tests'
    sys.path.append(str(tests_path))