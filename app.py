import requests
from api_key import api_key

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

text = input("Insira um texto para ser traduzido: ")

payload = {
    "source_language": "pt",
    "target_language": "en",
    "text": text
}

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())