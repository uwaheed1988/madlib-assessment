import flask
import requests
app = flask.Flask(__name__)


@app.route('/madlib', methods=['GET'])
def home():
    adjective = get_word("https://reminiscent-steady-albertosaurus.glitch.me/adjective")
    verb = get_word("https://reminiscent-steady-albertosaurus.glitch.me/verb")
    noun = get_word("https://reminiscent-steady-albertosaurus.glitch.me/noun")

    return "It was a " + adjective + " day. I went downstairs to see if I could " + verb + " dinner. I asked, \"Does the stew need fresh " + noun + "?\""


def get_word(url):
    word = ""
    word_data = requests.get(url)
    if word_data.status_code == 200:
        word = word_data.content.decode("utf-8").replace('"','')
    return word



if __name__ == '__main__':
    app.run(debug=True)