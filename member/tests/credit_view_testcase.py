from django.test import TestCase

from member.models import Credit, User
from utils.test.fixtures import TestFixture


class CreditViewTestCase(TestCase):

    def setUp(self):
        fixture = TestFixture()
        self.사용자: User = fixture.active_user
        self.사용자.save()
        self.크레딧: Credit = fixture.credit
        self.크레딧.save()

    def test_사용자는_크레딧을_조회할_수_있다(self):
        # given
        self.client.force_login(self.사용자)

        # when
        res = self.client.get(path="/api/member/users/credit")

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(data['balance'], 0)

    def test_사용자는_결제에_필요한_크레딧을_충전할_수_있다(self):
        # given
        self.client.force_login(self.사용자)

        # when
        res = self.client.post(
            path="/api/member/users/credit",
            data={
                "balance": 10000,
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 200)
        data = res.json()
        self.assertEquals(data['balance'], 10000)
