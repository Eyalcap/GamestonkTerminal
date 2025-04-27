"""Finbrain model"""
from security import safe_requests

__docformat__ = "numpy"


def get_technical_summary_report(ticker: str) -> str:
    """Get technical summary report provided by FinBrain's API

    Parameters
    ----------
    ticker : str
        Ticker to get the technical summary

    Returns
    -------
    report:str
        technical summary report
    """
    result = safe_requests.get(f"https://api.finbrain.tech/v0/technicalSummary/{ticker}")
    report = ""
    if result.status_code == 200:
        if "technicalSummary" in result.json():
            report = result.json()["technicalSummary"]
        else:
            print("Unexpected data format from FinBrain API")
    else:
        print("Request error in retrieving sentiment from FinBrain API")

    return report
