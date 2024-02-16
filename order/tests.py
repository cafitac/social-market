from django.test import TestCase

from member.models import User
from merchandise.models import Merchandise
from order.models.order import Order
from utils.test.fixtures import TestFixture


class OrderViewTestCase(TestCase):

    def setUp(self):
        testFixture: TestFixture = TestFixture()
        self.사용자: User = testFixture.active_user
        self.사용자.save()
        self.상품_1: Merchandise = testFixture.merchandise_1
        self.상품_1.save()
        self.상품_2: Merchandise = testFixture.merchandise_2
        self.상품_2.save()

        self.client.force_login(self.사용자)

    def test_사용자가_상품에_대한_주문을_생성할_수_있다(self):
        # when
        res = self.client.post(
            path="/api/order/orders",
            data={
                "email": self.사용자.email,
                "address": "서울시",
                "order_items": [
                    {
                        "merchandise_id": self.상품_1.id,
                        "amount": 1,
                    },
                    {
                        "merchandise_id": self.상품_2.id,
                        "amount": 2,
                    }
                ],
                "payment_type": "CARD",
            },
            content_type="application/json",
        )
    
        # then
        self.assertEquals(res.status_code, 201)

        data = res.json()

        order = Order.objects.get(pk=data['id'])
        self.assertTrue(Order.objects.filter(pk=data['id']).exists())
        self.assertEquals(order.order_items.count(), 2)
        self.assertEquals(order.order_transaction.status, "READY")

    def test_사용자가_주문에_대한_결제를_할_수_있다(self):
        pass
        # given

        # when

        # then
