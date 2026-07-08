import os

from .fxmacrodata import (
    FXMacroDataClient,
    load_fxmacrodata_announcements,
    load_fxmacrodata_dataset,
    load_fxmacrodata_forex,
    load_fxmacrodata_predictions,
    load_release_calendar,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FOREX_DATA_PATH = os.path.join(DATA_DIR, "symbols_forex.pkl")
STOCKS_DATA_PATH = os.path.join(DATA_DIR, "symbols_stocks.pkl")
CRYPTO_DATA_PATH = os.path.join(DATA_DIR, "symbols_crypto.pkl")
MIXED_DATA_PATH = os.path.join(DATA_DIR, "symbols_mixed.pkl")

__all__ = [
    "FOREX_DATA_PATH",
    "STOCKS_DATA_PATH",
    "CRYPTO_DATA_PATH",
    "MIXED_DATA_PATH",
    "FXMacroDataClient",
    "load_fxmacrodata_announcements",
    "load_fxmacrodata_dataset",
    "load_fxmacrodata_forex",
    "load_fxmacrodata_predictions",
    "load_release_calendar",
]
