from generator.user import UserGenerator


def get_random_user():
    return UserGenerator().generate_user()

user = get_random_user()

testdata = [user]
