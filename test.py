import unittest
import nltk
from api import app
from nltk.corpus import wordnet as wn


def check_word(word):
    nltk.download('wordnet')
    pos_l = []
    for tmp in wn.synsets(word):
        if tmp.name().split('.')[0] == word:
            pos_l.append(tmp.pos())
    return pos_l


class BasicTestCase(unittest.TestCase):

    def test_adjective(self):
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentense = response.data.decode("utf-8")
        adjective = sentense.split()[3]
        adjective_result = check_word(adjective)
        self.assertTrue(adjective_result != None and len(adjective_result) > 0 and 's' in adjective_result)
    
    def test_verb(self):
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentense = response.data.decode("utf-8")
        verb = sentense.split()[13]
        verb_result = check_word(verb)
        self.assertTrue(verb_result != None and len(verb_result) > 0 and 'v' in verb_result)
    
    def test_noun(self):
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentense = response.data.decode("utf-8")
        noun = sentense.split()[22].replace('"','').replace('?','')
        noun_result = check_word(noun)
        self.assertTrue(noun_result != None and len(noun_result) > 0 and 'n' in noun_result)


if __name__ == '__main__':
    unittest.main()