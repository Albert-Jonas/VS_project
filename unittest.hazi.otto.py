#A teszteset két részből áll: az egyik a sikeres hívást, a másik pedig a hibás hívást teszteli. A tesztben a patch() függvénnyel helyettesítjük a requests.get() függvényt egy Mock objektummal. A Mock objektum aztán meghívódik a get_joke() függvényben, és a mock_get.assert_called_once_with() metódussal ellenőrizzük, hogy a helyes URL-címet hívta-e meg.

import source
import unittest
from unittest.mock import patch, Mock
from requests.exceptions import RequestException

import source  # helyettesítse ezt a fájlnevet a saját modulja fájlnevével

class TestGetJoke(unittest.TestCase):
    @patch('source.requests.get')
    def test_get_joke_success(self, mock_get):
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = {'value': 'Chuck Norris jokes are always funny!'}
        mock_get.return_value = mock_response

        result = source.get_joke()

        self.assertEqual(result, 'Chuck Norris jokes are always funny!')
        mock_get.assert_called_once_with('https://api.chucknorris.io/jokes/random')

    @patch('source.requests.get')
    def test_get_joke_failure(self, mock_get):
        mock_get.side_effect = RequestException()

        result = source.get_joke()

        self.assertEqual(result, 'No jokes')
        mock_get.assert_called_once_with('https://api.chucknorris.io/jokes/random')

if __name__ == '__main__':
    unittest.main()