from mail.models import UserActiveMail
from member.models import User


class TestFixture:

    def __init__(self):
        # Member
        self.non_active_user = User(id=1, username='user1', password='user1user1', is_active=False)
        self.active_user = User(id=2, username='user1', password='user1user1', is_active=True)

        # Mail
        self.active_mail = UserActiveMail(id=1, user_id=self.non_active_user.id, active_code="active_code")
