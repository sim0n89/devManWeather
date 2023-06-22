import requests

def get_weather(city, params=None):
    response = requests.get("https://wttr.in/" + city, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))
        return
    print(response.text)


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
