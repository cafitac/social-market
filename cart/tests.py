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
        self.기타_사용자: User = fixture.other_user
        self.기타_사용자.save()
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
                "amount": 1,
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
        # given
        cart: Cart = self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)

        # when
        res = self.client.patch(
            path=f"/api/cart/carts/{cart.id}",
            data={
                "amount": 3,
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 200)

        cart.refresh_from_db()
        self.assertEquals(cart.amount, 3)
        
    def test_기타_사용자는_사용자의_장바구니_상품_수를_수정할_수_없다(self):
        # given
        cart: Cart = self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)
        self.client.force_login(self.기타_사용자)

        # when
        res = self.client.patch(
            path=f"/api/cart/carts/{cart.id}",
            data={
                "amount": 3,
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 403)

    def test_사용자가_장바구니에_있는_상품을_제거할_수_있다(self):
        # given
        cart: Cart = self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)

        # when
        res = self.client.delete(path=f"/api/cart/carts/{cart.id}")
    
        # then
        self.assertEquals(res.status_code, 204)

        cart.refresh_from_db()
        self.assertTrue(cart.is_deleted)

    def test_기타_사용자는_사용자의_장바구니_상품을_제거할_수_없다(self):
        # given
        cart: Cart = self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)
        self.client.force_login(self.기타_사용자)

        # when
        res = self.client.delete(path=f"/api/cart/carts/{cart.id}")

        # then
        self.assertEquals(res.status_code, 403)
        
    def test_상품이_삭제되면_상품을_담은_장바구니에서도_삭제된_것으로_나타난다(self):
        # given
        cart: Cart = self._사용자가_장바구니에_상품을_추가함(self.상품_1.id)

        # when
        self._사용자가_상품을_삭제함(self.상품_1.id)

        # then
        cart.refresh_from_db()

        self.assertTrue(cart.merchandise_is_deleted)

    def _사용자가_장바구니에_상품을_추가함(self, merchandise_id: int) -> Cart:
        res = self.client.post(
            path="/api/cart/carts",
            data={
                "merchandise_id": merchandise_id,
                "amount": 1,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 201)

        data = res.json()
        return Cart.objects.get(pk=data['id'])

    def _사용자가_상품을_삭제함(self, merchandise_id: int):
        res = self.client.delete(path=f"/api/merchandise/merchandises/{merchandise_id}")
        self.assertEquals(res.status_code, 204)
