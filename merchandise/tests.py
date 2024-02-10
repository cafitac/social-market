from django.test import TestCase

from member.models import User
from merchandise.models import Merchandise
from utils.test.fixtures import TestFixture


class MerchandiseViewTestCase(TestCase):

    def setUp(self):
        self.사용자: User = TestFixture().active_user
        self.사용자.save()

    def test_create_merchandise(self):
        self.client.force_login(self.사용자)

        res = self.client.post(
            path="/api/merchandise/merchandises",
            data={
                "name": "상품",
                "description": "상품 설명",
                "price": 10000,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 201)

        data = res.json()

        self.assertTrue(Merchandise.objects.filter(pk=data['id']).exists())

    def test_get_own_merchandises(self):
        self.test_create_merchandise()

        res = self.client.get(path="/api/merchandise/merchandises")
        self.assertEquals(res.status_code, 200)

        data = res.json()

        self.assertEquals(len(data), 1)
