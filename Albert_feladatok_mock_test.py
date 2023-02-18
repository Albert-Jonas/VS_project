import pytest_mock
import pytest
import requests
from Albert_feladatok_mock import len_joke
from Albert_feladatok_mock import dummy_function
from Albert_feladatok_mock import get_joke

#Teszteset1
def test_dummy_function (mocker):
    
    
    def test_mocking_function (mocker):
        mocker.patch("https://api.chucknorris.io/jokes/random","0")
    assert dummy_function() != 0
