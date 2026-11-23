
import httpx
import random
from pprint import pprint

base_url = "https://dummyjson.com/"

content = "recipe/meal-type/snack"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

pprint(content)

