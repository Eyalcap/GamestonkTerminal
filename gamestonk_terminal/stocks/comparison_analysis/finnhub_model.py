"""Finnhub model"""
from security import safe_requests

__docformat__ = "numpy"

from typing import List, Tuple
from gamestonk_terminal import config_terminal as cfg


def get_similar_companies(ticker: str) -> Tuple[List[str], str]:
    result = safe_requests.get(
        f"https://finnhub.io/api/v1/stock/peers?symbol={ticker}&token={cfg.API_FINNHUB_KEY}"
    )

    if result.status_code == 200:
        similar = result.json()
        user = "Finnhub"

    else:
        print("Similar companies not found.")
        similar = [""]
        user = "Error"
    return similar, user
