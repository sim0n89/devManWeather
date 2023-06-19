import requests

response = requests.get('https://wttr.in/san%20francisco?nTqu&lang=en')
print (response.text)

response = requests.get('https://wttr.in/svo')
print (response.text)

response = requests.get('https://wttr.in/london')
print(response.text)

response = requests.get('https://wttr.in/череповец?m&m&lang=ru&M&n&q&T' )
print(response.text)