import requests


def get_weather(city, params=None):
    response = requests.get(f"https://wttr.in/{city}", params=params)
    response.raise_for_status()
    print(response.text)



if __name__ == '__main__':
    params = {"m": "",
              "lang": "ru",
              "M": "",
              "n": "",
              "q": "",
              "T": ""
              }
    citys = ["san%20francisco", "svo", "london", "череповец", ]
    for city in citys:
        get_weather(city, params)
