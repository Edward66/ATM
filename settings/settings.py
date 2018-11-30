import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DB = os.path.join(BASE_DIR, 'db/')

BASE_LOG = os.path.join(BASE_DIR, 'log/')

INTEREST = {
    'withdraw': 0.05,
}
