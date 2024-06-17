
"""1. test_scores_service - it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
2. main_function to call our tests function. The main function will return -1 as an OS exit
code if the tests failed and 0 if they passed. """

from bs4 import BeautifulSoup
import requests as req


def test_scores_service():
    webpage = req.get('http://127.0.0.1:5000')
    html = BeautifulSoup(webpage.content, "html.parser")
    div_text = int(html.find("div", {"id": "score"}).get_text())
    if 0 < div_text < 1000:
        return True
    return False


def main_function():
    if test_scores_service():
        print("ok")
        return 0
    return -1


print(main_function())
