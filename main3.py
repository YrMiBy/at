import requests

def get_cat_breeds():
   url = "https://api.thecatapi.com/v1/breeds"
   response = requests.get(url)  # отправление запроса
   if response.status_code == 200:  # если статус-код ответа = 200 возвращаем данные в формате JSON
       return response.json()
   else:
       return None


