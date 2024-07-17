import requests

url = "https://api.ok.ru/fb.do"
app_id = "512002169614"
public_key = "CPAMBGLGDIHBABABA"
secret_key = "4A8DA4ACC8490778A41CE101"
access_token = "-n-gF6x6vvNFJn9ZSMd8muR3el5MioyY4k2nA8htJvlcdvGUnSAIr6Iu3GPvjzavEu3hePcwdJx4DiD6TGIy0"
id_photo = "974130945273"


def edit_photo(photo_id, description, token):
    params = {
        "method": "photos.editPhoto",
        "photo_id": photo_id,
        "description": description,
        "access_token": token,
        "application_key": public_key,
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()


# Позитив
def test_edit_description():
    result = edit_photo(id_photo, "New Description", access_token)
    assert result is True, f"Expected success, but got {result}"


def test_remove_description():
    result = edit_photo(id_photo, "", access_token)
    assert result is True, f"Expected success, but got {result}"


# Негатив
def test_invalid_id():
    result = edit_photo("invalid_photo_id", "New Description", access_token)
    assert "error_code" in result, f"Expected error, but got {result}"


def test_invalid_token():
    result = edit_photo(id_photo, "New Description", "INVALID_TOKEN")
    assert "error_code" in result, f"Expected error, but got {result}"


def test_no_token():
    result = edit_photo(id_photo, "New Description", "")
    assert "error_code" in result, f"Expected error, but got {result}"


if __name__ == "__main__":
    test_edit_description()
    test_remove_description()
    test_invalid_id()
    test_invalid_token()
    test_no_token()
    print("All tests passed successfully!")
