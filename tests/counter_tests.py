import unittest

from run import app


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_thread_counter_page_100(self):
        responses = []
        for _ in range(100):
            response = self.app.get('/counter/thread', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 100)

    def test_thread_counter_page_500(self):
        responses = []
        for _ in range(500):
            response = self.app.get('/counter/thread', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 500)

    def test_thread_counter_page_1000(self):
        responses = []
        for _ in range(1000):
            response = self.app.get('/counter/thread', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 1000)

    def test_thread_counter_page_3000(self):
        responses = []
        for _ in range(3000):
            response = self.app.get('/counter/thread', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 3000)

    def test_actor_counter_page_100(self):
        responses = []
        for _ in range(100):
            response = self.app.get('/counter/actor', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 100)

    def test_actor_counter_page_500(self):
        responses = []
        for _ in range(500):
            response = self.app.get('/counter/actor', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 500)

    def test_actor_counter_page_1000(self):
        responses = []
        for _ in range(1000):
            response = self.app.get('/counter/actor', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 1000)

    def test_actor_counter_page_3000(self):
        responses = []
        for _ in range(3000):
            response = self.app.get('/counter/actor', follow_redirects=True)
            responses.append(str(response))
        self.assertEqual(len(responses), 3000)

if __name__ == "__main__":
    unittest.main()
