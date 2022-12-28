# Dealing with APIs
# 1XX HOLD ON
# 2XX HERE YOU GO
# 3XX GO AWAY
# 4XX YOU SCREWED UP
# 5XX I SCREWED UP
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json");
if response.status_code != 200:
    raise Exception('An error occured')
print(response.json()['iss_position'])
print(response.status_code)
