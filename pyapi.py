# import module to call apis
import requests

parameters = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

# Print the status code of the response.
print(response.status_code)
print(response.content)
