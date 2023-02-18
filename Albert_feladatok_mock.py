import requests

# Ki kell helyettesíteni benne néhány teszthet dolgokat (pl az egyik függvényt vagy az API hívást). 

def len_joke():
    joke = get_joke()
    return len(joke)

def dummy_function():
    return len_joke


def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'

    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'No jokes'

    return joke


if __name__ == '__main__':
    print(get_joke())
    print (len_joke())