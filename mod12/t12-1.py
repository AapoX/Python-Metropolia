import requests

def hae_vitsi():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()
    return data['value']

def main():
    vitsi = hae_vitsi()
    print(vitsi)

if __name__ == "__main__":
    main()