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
        self.크레딧 = testFixture.credit
        self.크레딧.save()
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
        self.assertEquals(order.total_price(), (self.상품_1.price * 1) + (self.상품_2.price * 2))
        self.assertEquals(order.order_transaction.status, "READY")

    def test_사용자가_주문에_대한_결제를_할_수_있다(self):
        # given
        order: Order = self._사용자가_주문을_생성함()
        self._사용자가_크레딧을_충전함(100000)

        # when
        res = self.client.post(
            path=f"/api/order/payments",
            data={
                "order_id": {order.id}
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()

        order.refresh_from_db()
        self.assertEquals(order.order_transaction.status, "PAID")

    def _사용자가_주문을_생성함(self) -> Order:
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
        self.assertEquals(res.status_code, 201)

        data = res.json()

        return Order.objects.get(pk=data['id'])

    def _사용자가_크레딧을_충전함(self, amount: int):
        res = self.client.post(
            path="/api/member/users/credit",
            data={
                "charge_amount": amount,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 200)
