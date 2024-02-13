from mail.models import UserActiveMail
from member.models import User
from member.models.credit import Credit


class TestFixture:

    def __init__(self):
        # Member
        self.non_active_user = User(id=1, username='user1', password='user1user1', is_active=False)
        self.active_user = User(id=2, username='active_user', password='active_useractive_user', is_active=True)
        self.other_user = User(id=3, username='other_user', password='other_userother_user', is_active=True)

        # Credit
        self.credit = Credit(user=self.active_user)

        # Mail
        self.active_mail = UserActiveMail(id=1, user_id=self.non_active_user.id, active_code="active_code")
