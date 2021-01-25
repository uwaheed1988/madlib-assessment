import unittest
from api import app
from PyDictionary import PyDictionary

dictionary=PyDictionary()

class BasicTestCase(unittest.TestCase):

    def test_adjective(self):
        """
        Test madlib api against adjectives
        :return:
        """
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentence = response.data.decode("utf-8")
        adjective = sentence.split()[3]
        adjective_result = dictionary.meaning(adjective)
        self.assertTrue('Adjective' in adjective_result.keys())
    
    def test_verb(self):
        """
        Test madlib api against verb
        :return:
        """
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentence = response.data.decode("utf-8")
        verb = sentence.split()[13]
        verb_result = dictionary.meaning(verb)
        self.assertTrue('Verb' in verb_result.keys())
    
    def test_noun(self):
        """
        Test madlib api against noun
        :return:
        """
        tester = app.test_client(self)
        response = tester.get('/madlib', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        sentence = response.data.decode("utf-8")
        noun = sentence.split()[22].replace('"','').replace('?','')
        noun_result = dictionary.meaning(noun)
        self.assertTrue('Noun' in noun_result.keys())


if __name__ == '__main__':
    unittest.main()
