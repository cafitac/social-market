from django.test import TestCase

from member.models import User


class UserViewTestCase(TestCase):

    def test_사용자가_회원가입을_합니다(self) -> None:
        res = self.client.post(
            path="/api/member/users",
            data={
                "username": "user1",
                "password": "user1user1",
                "re_password": "user1user1",
                "email": "user1@gmail.com",
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 201)

        data: dict = res.json()
        self.assertTrue(User.objects.filter(username=data['username']).exists())
