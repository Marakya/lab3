import main
import pytest
import imghdr

# проверим, что на выходе картинка
def test_kl():
    result = main.generate_image("")
    assert imghdr.what(result) == "jpeg"




