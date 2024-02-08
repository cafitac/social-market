from django.test import TestCase

from utils.test.fixtures import TestFixture


class MailViewTestCase(TestCase):

    def setUp(self):
        self.비활성화_사용자 = TestFixture().non_active_user
        self.비활성화_사용자.save()

    def test_사용자가_메일_인증을_통해_계정을_활성화합니다(self):
        self.client.force_login(self.비활성화_사용자)

        user_active_mail = TestFixture().active_mail
        user_active_mail.save()

        res = self.client.get(path=f"/api/mail/{user_active_mail.activate_code}")
        self.assertEquals(res.status_code, 200)

        user_active_mail.refresh_from_db()

        self.assertTrue(user_active_mail.is_expired)
