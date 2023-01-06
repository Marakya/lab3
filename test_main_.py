import main_
import pytest
import imghdr

def test_error():
    with pytest.raises(ValueError):
        main_.text_sum(12323434)

def test_read_sum():
    summ = main_.predict_text('Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among those that will be taken down, the company said.  The policy includes the termination of accounts of anti-vaccine influencers.  Tech giants have been criticised for not doing more to counter false health information on their sites.  In July, US President Joe Biden said social media platforms were largely responsible for peoples scepticism in getting vaccinated by spreading misinformation, and appealed for them to address the issue.')
    assert type(summ) == str

def test_null():
    summ = main_.predict_text("")
    assert type(summ) == str

# проверим, что на выходе картинка
def test_kl():
    result = main_.generate_image("")
    assert imghdr.what(result) == "jpeg"




