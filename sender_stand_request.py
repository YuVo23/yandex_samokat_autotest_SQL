import configuration
import requests
import data

#Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, 
                         json = body,
                         headers=data.headers)

#Получение номера заказа
def get_track_id(body):
    response = post_new_order(body)
    track_id = response.json()["track"]
    return track_id


#Получение заказа по треку
def get_order_by_track(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.TRACK_NUMBER, 
                            params={"t": track_number})
    return response
