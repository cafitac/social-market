from mail.models import UserActiveMail
from member.models import User
from member.models.credit import Credit
from merchandise.models import Merchandise, Stock


class TestFixture:

    def __init__(self):
        # Member
        self.non_active_user = User(
            id=1,
            username='user1',
            password='user1user1',
            email="user1@email.com",
            is_active=False
        )
        self.active_user = User(
            id=2,
            username='active_user',
            password='active_useractive_user',
            email="active_user@email.com",
            is_active=True
        )
        self.other_user = User(
            id=3,
            username='other_user',
            password='other_userother_user',
            email="other_user@email.com",
            is_active=True
        )

        # Credit
        self.credit = Credit(user=self.active_user)

        # Mail
        self.active_mail = UserActiveMail(id=1, user_id=self.non_active_user.id, active_code="active_code")

        # Merchandise
        self.merchandise_1 = Merchandise(id=1, username=self.active_user.username, name="상품1", price=10000)
        self.merchandise_2 = Merchandise(id=2, username=self.active_user.username, name="상품2", price=20000)

        # Stock
        self.stock_1 = Stock(merchandise_id=self.merchandise_1.id, count=10)
        self.stock_2 = Stock(merchandise_id=self.merchandise_2.id, count=10)
