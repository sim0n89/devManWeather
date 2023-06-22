import requests


def get_weather(city, params=None):
    try:
        response = requests.get("https://wttr.in/" + city, params=params)
        response.raise_for_status()
        print(response.text)
    except Exception as e:
        print("Error: " + str(e))
        return



if __name__ == '__main__':
    weatherUrls = [
        {
            "city": "san%20francisco",
            "params": {'nTqu': "",
                       "lang": "ru", }
        },
        {
            "city": "svo",
            "params": {'nTqu': "",
                       "lang": "ru", }
        },
        {
            "city": "london",
            "params": {'nTqu': "",
                       "lang": "ru", }
        },
        {
            "city": "череповец",
            "params": {"m": "",
                       "lang": "ru",
                       "M": "",
                       "n": "",
                       "q": "",
                       "T": ""
                       }
        }
    ]

    for url in weatherUrls:
        get_weather(url["city"], url["params"])
        pass
