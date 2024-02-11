from django.contrib.auth.hashers import make_password
from django.test import TestCase

from member.models import User
from utils.test.fixtures import TestFixture


class LoginViewTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.사용자: User = TestFixture().active_user
        self.raw_password = self.사용자.password
        self.사용자.password = make_password(self.사용자.password)
        self.사용자.save()

    def test_사용자가_로그인을_할_수_있다(self):
        # when
        res = self.client.post(
            path="/api/auth/login",
            data={
                "username": self.사용자.username,
                "password": self.raw_password,
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertIsNotNone(data['token'])
