from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser",
        password="password",
        email="test@email.com",
        )
        cls.post = Post.objects.create(
        title="A good title",
        body="Nice body content",
        author=cls.user,
        )
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
    
    def test_post_create_view(self):
        response = self.client.post(
            reverse("post_new"),
            {
                'title': "A good title",
                'body': "Nice body content",
                'author': self.user.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "A good title")
        self.assertEqual(Post.objects.last().body, "Nice body content")
        

    def test_post_update_view(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                'title': "Updated title",
                'body': "Updated text",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
