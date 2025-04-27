""" Finnhub Model """
from security import safe_requests

__docformat__ = "numpy"
import pandas as pd
from gamestonk_terminal import config_terminal as cfg


def get_rating_over_time(ticker: str) -> pd.DataFrame:
    """Get rating over time data. [Source: Finnhub]

    Parameters
    ----------
    ticker : str
        Ticker to get ratings from

    Returns
    -------
    pd.DataFrame
        Get dataframe with ratings
    """
    response = safe_requests.get(
        f"https://finnhub.io/api/v1/stock/recommendation?symbol={ticker}&token={cfg.API_FINNHUB_KEY}"
    )
    if response.status_code == 200:
        return pd.DataFrame(response.json())

    return pd.DataFrame()
