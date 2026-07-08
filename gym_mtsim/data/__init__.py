import os

from .fxmacrodata import load_release_calendar

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FOREX_DATA_PATH = os.path.join(DATA_DIR, 'symbols_forex.pkl')
STOCKS_DATA_PATH = os.path.join(DATA_DIR, 'symbols_stocks.pkl')
CRYPTO_DATA_PATH = os.path.join(DATA_DIR, 'symbols_crypto.pkl')
MIXED_DATA_PATH = os.path.join(DATA_DIR, 'symbols_mixed.pkl')

__all__ = [
    'FOREX_DATA_PATH',
    'STOCKS_DATA_PATH',
    'CRYPTO_DATA_PATH',
    'MIXED_DATA_PATH',
    'load_release_calendar',
]
