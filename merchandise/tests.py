from django.test import TestCase

from member.models import User
from merchandise.models import Merchandise
from utils.test.fixtures import TestFixture


class MerchandiseViewTestCase(TestCase):

    def setUp(self):
        self.사용자: User = TestFixture().active_user
        self.사용자.save()
        self.기타_사용자: User = TestFixture().other_user
        self.기타_사용자.save()

    def test_사용자가_상품을_등록할_수_있다(self) -> Merchandise:
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

        return Merchandise.objects.get(pk=data['id'])

    def test_사용자가_상품_목록을_조회할_수_있다(self):
        self._사용자가_상품을_등록함(self.사용자)
        self._사용자가_상품을_등록함(self.사용자)
        self.client.force_login(self.사용자)

        res = self.client.get(path="/api/merchandise/merchandises")
        self.assertEquals(res.status_code, 200)

        data = res.json()

        self.assertEquals(len(data), 2)

    def test_사용자가_자신이_등록한_상품_목록만_조회할_수_있다(self):
        # given
        self._사용자가_상품을_등록함(self.사용자)
        self._사용자가_상품을_등록함(self.기타_사용자)
        self.client.force_login(self.사용자)

        # when
        res = self.client.get(path="/api/merchandise/merchandises?filter_type=own")

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(len(data), 1)

    def test_기타_사용자가_사용자가_등록한_상품_목록을_조회할_수_있다(self):
        # given
        self._사용자가_상품을_등록함(self.사용자)
        self._사용자가_상품을_등록함(self.기타_사용자)
        self.client.force_login(self.기타_사용자)

        # when
        res = self.client.get(f"/api/merchandise/merchandises?filter_type=user&username={self.사용자.username}")

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(len(data), 1)

    def test_사용자가_자신이_등록한_상품_상세_정보를_조회할_수_있다(self):
        merchandise: Merchandise = self.test_사용자가_상품을_등록할_수_있다()

        res = self.client.get(path=f"/api/merchandise/merchandises/{merchandise.id}")
        self.assertEquals(res.status_code, 200)

        data = res.json()

        self.assertEquals(data['name'], merchandise.name)

    def test_사용자가_기타_사용자가_등록한_상품_상세_정보를_조회할_수_있다(self):
        merchandise: Merchandise = self._사용자가_상품을_등록함(self.사용자)
        self.client.force_login(self.사용자)

        res = self.client.get(path=f"/api/merchandise/merchandises/{merchandise.id}")
        self.assertEquals(res.status_code, 200)

        data = res.json()

        self.assertEquals(data['name'], merchandise.name)

    def test_사용자가_자신이_등록한_상품의_정보를_수정할_수_있다(self):
        merchandise: Merchandise = self.test_사용자가_상품을_등록할_수_있다()

        res = self.client.patch(
            path=f"/api/merchandise/merchandises/{merchandise.id}",
            data={
                "name": "수정된 상품 이름",
                "description": "수정된 상품 설명",
                "price": 5000,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 200)

        data = res.json()
        merchandise.refresh_from_db()

        self.assertEquals(merchandise.name, "수정된 상품 이름")

    def test_기타_사용자는_사용자가_등록한_상품의_정보를_수정할_수_없다(self):
        merchandise: Merchandise = self.test_사용자가_상품을_등록할_수_있다()
        self.client.force_login(self.기타_사용자)

        res = self.client.patch(
            path=f"/api/merchandise/merchandises/{merchandise.id}",
            data={
                "name": "수정된 상품 이름",
                "description": "수정된 상품 설명",
                "price": 5000,
            },
            content_type="application/json",
        )
        self.assertEquals(res.status_code, 403)

    def test_사용자가_자신이_등록한_상품을_삭제할_수_있다(self):
        merchandise: Merchandise = self.test_사용자가_상품을_등록할_수_있다()

        res = self.client.delete(path=f"/api/merchandise/merchandises/{merchandise.id}")
        self.assertEquals(res.status_code, 204)

        self.assertTrue(Merchandise.objects.get(pk=merchandise.id).is_deleted)

    def test_기타_사용자는_사용자가_등록한_상품을_삭제할_수_없다(self):
        merchandise: Merchandise = self.test_사용자가_상품을_등록할_수_있다()
        self.client.force_login(self.기타_사용자)

        res = self.client.delete(path=f"/api/merchandise/merchandises/{merchandise.id}")
        self.assertEquals(res.status_code, 403)

    def test_사용자가_상품_이름으로_상품을_검색할_수_있다(self):
        # given
        self._사용자가_상품을_등록함(self.사용자)
        self._사용자가_상품을_등록함(self.기타_사용자)
        self.client.force_login(self.사용자)

        # when
        res = self.client.get(path="/api/merchandise/merchandises?q=상품")

        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(len(data), 1)
        self.assertIn("상품", [x['name'] for x in data])
        
    def test_사용자가_상품_재고를_조회할_수_있다(self):
        # given
        merchandise: Merchandise = self._사용자가_상품을_등록함(self.사용자)

        # when
        res = self.client.get(path=f"/api/merchandise/merchandises/{merchandise.id}/stock")
    
        # then
        self.assertEquals(res.status_code, 200)

        data = res.json()
        self.assertEquals(data['count'], 0)

    def test_사용자가_상품_재고를_수정할_수_있다(self):
        # given
        merchandise: Merchandise = self._사용자가_상품을_등록함(self.사용자)

        # when
        res = self.client.patch(
            path=f"/api/merchandise/merchandises/{merchandise.id}/stock",
            data={
                'count': 10
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 200)

        merchandise.refresh_from_db()
        self.assertEquals(merchandise.stock.count, 10)

    def test_기타_사용자는_사용자가_등록한_상품의_재고를_수정할_수_없다(self):
        # given
        merchandise: Merchandise = self._사용자가_상품을_등록함(self.사용자)
        self.client.force_login(self.기타_사용자)

        # when
        res = self.client.patch(
            path=f"/api/merchandise/merchandises/{merchandise.id}/stock",
            data={
                'count': 10
            },
            content_type="application/json",
        )

        # then
        self.assertEquals(res.status_code, 403)

    def _사용자가_상품을_등록함(self, user: User) -> Merchandise:
        self.client.force_login(user)

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
        return Merchandise.objects.get(pk=data["id"])
