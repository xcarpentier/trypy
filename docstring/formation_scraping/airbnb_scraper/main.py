import requests
from requests.exceptions import RequestException
from pathlib import Path
from bs4 import BeautifulSoup
import logging


FILEPATH = Path(__file__).parent / "airbnb.html"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def fetch_content(url: str, from_disk: bool = False) -> str:
    if from_disk and FILEPATH.exists():
        return _read_from_file()
    else:
        try:
            logger.debug(f"Making request to {url}")
            response = requests.get(url)
            response.raise_for_status
            html_content = response.text
            _write_to_file(content=html_content)
            return html_content
        except RequestException as e:
            logger.error(f"Coudn't fetch content from {url} due to {str(e)}.")
            raise e


def get_average_price(html: str):
    prices = []
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div", {"data-testid": "card-container"})
    return divs


def _write_to_file(content: str) -> bool:
    logger.debug("Writing content to file.")
    with open(FILEPATH, "w") as f:
        f.write(content)
    return FILEPATH.exists()


def _read_from_file() -> str:
    logger.debug("Reading content from file.")
    with open(FILEPATH, "r") as f:
        return f.read()


if __name__ == "__main__":
    url = "https://www.airbnb.com/s/Rio-de-Janeiro--Rio-de-Janeiro--Brazil/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-06-01&monthly_length=3&monthly_end_date=2024-07-01&price_filter_input_type=0&channel=EXPLORE&query=Rio%20de%20Janeiro%2C%20Rio%20de%20Janeiro%2C%20Brazil&date_picker_type=monthly_stay&adults=1&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=92&place_id=ChIJW6AIkVXemwARTtIvZ2xC3FA&federated_search_session_id=46764c44-91a4-4aff-840f-fdb0ed5a4180&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D"
    content = fetch_content(url=url, from_disk=True)
    print(get_average_price(html=content))
