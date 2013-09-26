# -*- coding: utf-8 *-*
from gs.group.member.invite.csv.create_users_from_csv import \
    CreateUsersInviteForm
from edem.profile.signup.base.utils import fn_to_nickname
import logging
log = logging.getLogger('edem.group.member.invite.csv')


class EDemCreateUsersForm(CreateUsersInviteForm):

    def __init__(self, context, request):
        super(EDemCreateUsersForm, self).__init__(context, request)

    def create_user(self, fields):
        userInfo = CreateUsersInviteForm.create_user(self, fields)
        if userInfo.nickname == userInfo.id:
            m = 'Adding nickname to %s (%s)' % (userInfo.name, userInfo.id)
            log.info(m)
            nickname = fn_to_nickname(self.context, userInfo.name)
            userInfo.user.add_nickname(nickname)
        return userInfo
