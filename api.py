import flask, requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from const import BASE_URL, RETRIES, TIMEOUT, RETURN_TEMPLATE

app = flask.Flask(__name__)

@app.route('/madlib', methods=['GET'])
def home():
    """
    It returns a complete sentence with an adjective, a verb and a noun (fetched from a word)
    :return: string
    """
    session = requests.session()
    session.mount(BASE_URL, HTTPAdapter(max_retries=Retry(total=RETRIES)))
    words = [get_word(f'{BASE_URL}{each}', session) for each in ('adjective', 'verb', 'noun')]
    session.close()
    if all(words):
        return RETURN_TEMPLATE.format(*words)
    else:
        return "Mainstream server is down!"

def get_word(url, session):
    """
    This method takes in a url and returns the adjective/noun/verb.
    :param url: string
    :return: string
    """
    word = ""
    word_data = session.get(url, timeout=TIMEOUT)
    if word_data.status_code == 200:
        word = word_data.content.decode("utf-8").replace('"','')
    return word



if __name__ == '__main__':
    app.run(host='0.0.0.0')
