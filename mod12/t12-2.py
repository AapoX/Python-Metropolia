import requests

def hae_saa(api_key, paikkakunta):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}')
    data = response.json()
    lampotila_kelvin = data['main']['temp']
    lampotila_celsius = lampotila_kelvin - 273.15
    saa_tila = data['weather'][0]['description']
    return saa_tila, lampotila_celsius

def main():
    api_key = 'your_api_key'  # Replace with your API key
    paikkakunta = input("Anna paikkakunta: ")
    saa_tila, lampotila = hae_saa(api_key, paikkakunta)
    print(f"Säätila {paikkakunta}: {saa_tila}, lämpötila: {lampotila:.2f} °C")

if __name__ == "__main__":
    main()