# import beautifulSoup
import requests

response=requests.get("http://worldtimeapi.org/api/timezone/Asia/Kathmandu")

response_json=response.json()
print(f"The date time is:{response_json['utc_datetime']}")