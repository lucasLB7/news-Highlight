import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Parent class tests variables instances
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('wired','wired News','tech news provider','wired.com','tech','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'wired')
        self.assertEquals(self.new_source.name,'wired News')
        self.assertEquals(self.new_source.description,'tech news provider')
        self.assertEquals(self.new_source.url,'wired.com')
        self.assertEquals(self.new_source.category,'tech')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('wired','Peter Polle','Hackers exploiting druplageddon','Hackers exploiting druplageddon to set up DDOS botnets like mirai','wired.com','wired.com/7643t94.jpg','2018-03-11T07:48:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'wired')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'Hackers exploiting druplageddon')
        self.assertEquals(self.new_article.description,'Hackers exploiting druplageddon to set up DDOS botnets like mirai')
        self.assertEquals(self.new_article.url,'wired.com')
        self.assertEquals(self.new_article.image,'wired.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2018-03-11T07:48:16Z')