

def test_register_random_user(app, data_users):
    user = data_users
    app.user.sign_up(user)
    app.user.logout()
    app.user.login(user)
    app.user.logout()
