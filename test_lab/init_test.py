from os import path
from src.config.settings import (
    APP_DIR,
    ROOT_DIR
)

def test_paths_for_correct():
    assert path.exists(APP_DIR) == True
    assert path.exists(ROOT_DIR) == True
