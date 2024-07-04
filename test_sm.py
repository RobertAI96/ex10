import unittest
from io import StringIO
from mock import patch
from contact_manager_task import User, SM

class TestSM(unittest.TestCase):

    def setUp(self):
        self.social_media = SM()
        self.user1 = self.social_media.cu("user1")
        self.user2 = self.social_media.cu("user2")

    def test_cu(self):
        self.setUp()
        user = self.social_media.gu("user1")
        self.assertIsNotNone(user)
        self.assertEqual(user.u, "user1")

    def test_cp(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        post = user1.cp("Test post content")
        self.assertIsNotNone(post)
        self.assertEqual(post["u"], "user1")
        self.assertEqual(post["c"], "Test post content")

    def test_lp(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        user2 = self.social_media.gu("user2")
        post = user1.cp("Test post")
        user2.lp(post)
        self.assertEqual(len(post["l"]), 1)
        self.assertIn("user2", post["l"])

    def test_cp(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        user2 = self.social_media.gu("user2")
        post = user1.cp("Test post")
        user2.cop(post, "Nice post!")
        self.assertEqual(len(post["cm"]), 1)
        self.assertEqual(post["cm"][0]["u"], "user2")
        self.assertEqual(post["cm"][0]["c"], "Nice post!")

    def test_dpu(self):
        result1 = self.social_media.cu("user1")
        result2 = self.social_media.cu("user2")
        self.assertIsNone(result1)
        self.assertIsNone(result2)

    def test_lpo(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        post = user1.cp("Test post")
        user1.lp(post)
        self.assertEqual(len(post["l"]), 1)  # User can like their own post

    def test_dpl(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        user2 = self.social_media.gu("user2")
        post = user1.cp("Test post")
        user2.lp(post)
        user2.lp(post)
        self.assertEqual(len(post["l"]), 1)  # User can't like the same post twice

    def test_cpo(self):
        self.setUp()
        user1 = self.social_media.gu("user1")
        post = user1.cp("Test post")
        user1.cop(post, "My own post comment")
        self.assertEqual(len(post["cm"]), 1)  # User can comment on their own post

    @patch('sys.stdout', new_callable=StringIO) # mock console to catch output
    def test_tle(self, mock_stdout):
        self.social_media.cu("user3")
        user3 = self.social_media.gu("user3")
        timeline = user3.rt()
        expected_output = "No posts to display.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output) 

if __name__ == "__main__":
    unittest.main()
