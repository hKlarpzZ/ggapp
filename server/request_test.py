import requests
from PIL import Image
from urllib3.response import HTTPResponse

url = 'http://127.0.0.1:8000/generate_tab'
json = {
    'text': 'shiiiiiiiiit',
    'post_id': '1',
    'img_type': 'left'
}

response = requests.post(url=url, json=json)
print(response.image)

# print(response.raw)
# Image.frombuffer(size=)

# im = Image.frombytes(mode='PNG', data=response.text)


# im.show()