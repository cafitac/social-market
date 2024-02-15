from django.test import TestCase

from cart.models.cart import Cart
from member.models import User
from merchandise.models import Merchandise
from utils.test.fixtures import TestFixture


class CartViewTestCase(TestCase):
    
    def setUp(self):
        fixture = TestFixture()
        self.사용자: User = fixture.active_user
        self.사용자.save()
        self.상품_1: Merchandise = fixture.merchandise_1
        self.상품_1.save()
        self.상품_2: Merchandise = fixture.merchandise_2
        self.상품_2.save()

        self.client.force_login(self.사용자)

    def test_사용자가_상품을_장바구니에_추가할_수_있다(self):
        # when
        res = self.client.post(
            path="/api/cart/carts",
            data={
                "merchandise_id": self.상품_1.id,
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 201)

        data = res.json()
        self.assertEquals(data['merchandise_id'], self.상품_1.id)

    def test_사용자가_장바구니의_상품들을_조회할_수_있다(self):
        # given
        self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)
        self._사용자가_장바구니에_상품을_추가함(self.상품_2.id)

        # when
        res = self.client.get("/api/cart/carts")
    
        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(len(data), 2)

    def test_사용자가_장바구니에_있는_상품의_수를_수정할_수_있다(self):
        pass
        # given
        
        # when
    
        # then
    
    def test_사용자가_장바구니에_있는_상품을_제거할_수_있다(self):
        pass
        # given
        
        # when
    
        # then

    def _사용자가_장바구니에_상품을_추가함(self, merchandise_id: int) -> Cart:
        res = self.client.post(
            path="/api/cart/carts/",
            data={
                "merchandise_id": merchandise_id,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 201)

        data = res.json()
        return Cart.objects.get(pk=data['id'])