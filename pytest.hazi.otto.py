#Az első teszt ellenőrzi, hogy a get_joke() függvény helyesen téríti-e vissza a vicc szövegét, ha a válasz 200-as státusz kódot tartalmaz. A második teszt ellenőrzi, hogy a függvény helyesen téríti-e vissza a "No jokes" szöveget, ha a válasz nem tartalmaz 200-as státuszkódot.

#A monkeypatch Pytest segítségével lehetőségünk van a requests.get() függvényt helyettesíteni egy másik függvénnyel. Az első tesztesetben az alternatív függvény visszatér egy olyan objektummal, amelynek az json() metódusa visszaadja a viccet tartalmazó szótárat. Az összehasonlítás elvégzése után az eredménynek meg kell egyeznie a tesztesetben meghatározott vicc szövegével.

#A második tesztesetben a mock_requests_get() függvény helyettesíti a requests.get() függvényt, és kivételt dob. Ezt követően ellenőrizzük, hogy a függvény visszatért-e a "No jokes" szöveggel

import requests
import pytest
from requests.exceptions import RequestException

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'

    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'No jokes'

    return joke

def test_get_joke_success(monkeypatch):
    joke_text = "Chuck Norris jokes are always funny!"
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
        def json(self):
            return {"value": joke_text}

    def mock_requests_get(*args, **kwargs):
        return MockResponse(200)

    monkeypatch.setattr(requests, "get", mock_requests_get)

    assert get_joke() == joke_text

def test_get_joke_failure(monkeypatch):
    def mock_requests_get(*args, **kwargs):
        raise RequestException()

    monkeypatch.setattr(requests, "get", mock_requests_get)

    assert get_joke() == 'No jokes'