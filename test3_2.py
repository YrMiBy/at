from main3 import get_cat_breeds

def test_get_weather_success(mocker):  # используем фикстуру mocker
    mock_get = mocker.patch('main3.requests.get')
    mock_get.return_value.status_code = 405 # Создаем мок-ответ для успешного запроса
    mock_get.return_value.json.return_value = {
        'cat': [{'cat': 'siame'}],
    }

    api_key = 'https://api.thecatapi.com/v1/images/search'
    weather_data = get_cat_breeds()

    assert weather_data == {
        'cat': [{'cat': 'siame'}],
    }
