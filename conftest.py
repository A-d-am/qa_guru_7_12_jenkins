import os

CURRENT_FILE_PATH = os.path.abspath(__file__)

PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
TESTS_ROOT_PATH = os.path.join(PROJECT_ROOT_PATH, 'tests')
RESOURCES_DIR = os.path.join(TESTS_ROOT_PATH, 'resources')

