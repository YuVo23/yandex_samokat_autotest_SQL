#Юлия Волынцева, 29 когорта - Финальный провект. Инженер по тестированию плюс

import data
import sender_stand_request

def test_getting_order_by_track_id():
    track_id = sender_stand_request.get_track_id(data.order_body)
    response = sender_stand_request.get_order_by_track(track_id)
    assert response.status_code == 200
