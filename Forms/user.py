from flask_login import UserMixin
from dao.people import peopledao


class User(UserMixin):

    def build_person_dict(self, row):
        profile = {}
        profile['fname'] = row[0]
        profile['lname'] = row[1]
        profile['Phone'] = row[2]
        profile['Address'] = row[3]
        profile['City'] = row[4]
        profile['Country'] = row[5]
        profile['District'] = row[6]
        profile['Zipcode'] = row[7]
        return profile

    def __init__(self, person_id=None, id=None, password=None,
                 address_id=None, account_id=None, profile_info=None,
                 user_type=None):
        self.person_id = person_id
        self.id = id
        self.password = password
        self.address_id = address_id
        self.account_id = account_id
        self.profile_info = profile_info
        self.user_type = user_type


    def get_profile(self, pid):
        dao = peopledao()
        userlist = dao.getUserProfile(pid)
        dubylist = self.build_person_dict(userlist)
        return dubylist

    def get_user(self, us): #using pId
        dao = peopledao()
        userlist = dao.getUserKeys(us)
        if userlist:
            usr = User()
            usr.__set_user(userlist)
            return usr
        return None

    def __set_user(self, plist):
        self.person_id=plist[0]
        self.address_id=plist[1]
        self.account_id=plist[2]
        self.id=plist[3]
        self.password=plist[4]
        self.user_type=plist[5]

    def set_user(self, us):
        dao = peopledao()
        userlist = dao.getUserKeys(us)
        if userlist:
            self.__set_user(userlist)
            return True
        else:
            return False
