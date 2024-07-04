import unittest
from io import StringIO
from unittest.mock import patch
from contact_manager_solution import User, Post, SocialMediaPlatform


class TestSocialMediaPlatform(unittest.TestCase):

    def setUp(self):
        self.social_media = SocialMediaPlatform()
        self.user1 = self.social_media.create_user("user1")
        self.user2 = self.social_media.create_user("user2")

    def test_create_user(self):
        self.setUp()
        user = self.social_media.get_user("user1")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "user1")

    def test_create_post(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        post = user1.create_post("Test post content")
        self.assertIsNotNone(post)
        self.assertEqual(post.username, "user1")
        self.assertEqual(post.content, "Test post content")

    def test_like_post(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        user2 = self.social_media.get_user("user2")
        post = user1.create_post("Test post")
        user2.like_post(post)
        self.assertEqual(len(post.likes), 1)
        self.assertIn("user2", post.likes)

    def test_comment_on_post(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        user2 = self.social_media.get_user("user2")
        post = user1.create_post("Test post")
        user2.comment_on_post(post, "Nice post!")
        self.assertEqual(len(post.comments), 1)
        self.assertEqual(post.comments[0]["username"], "user2")
        self.assertEqual(post.comments[0]["comment"], "Nice post!")

    def test_duplicate_user_creation(self):
        result1 = self.social_media.create_user("user1")
        result2 = self.social_media.create_user("user2")
        self.assertIsNone(result1)
        self.assertIsNone(result2)

    def test_like_own_post(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        post = user1.create_post("Test post")
        user1.like_post(post)
        self.assertEqual(len(post.likes), 1)  # User can like their own post

    def test_duplicate_like(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        user2 = self.social_media.get_user("user2")
        post = user1.create_post("Test post")
        user2.like_post(post)
        user2.like_post(post)
        self.assertEqual(len(post.likes), 1)  # User can't like the same post twice

    def test_comment_on_own_post(self):
        self.setUp()
        user1 = self.social_media.get_user("user1")
        post = user1.create_post("Test post")
        user1.comment_on_post(post, "My own post comment")
        self.assertEqual(len(post.comments), 1)  # User can comment on their own post

    @patch('sys.stdout', new_callable=StringIO) # mock console to catch output
    def test_empty_timeline(self, mock_stdout):
        self.social_media.create_user("user3")
        user3 = self.social_media.get_user("user3")
        timeline = user3.view_timeline()
        expected_output = "No posts to display.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output) 

if __name__ == "__main__":
    unittest.main()
