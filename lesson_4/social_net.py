from datetime import datetime
import re


class Authorization:
    allUsers = {'Don': {'password': 'adsg3324', 'date': '2020-11-15 19:56:22', 'is_admin': '1'},
                'Folk': {'password': '2h45h425h', 'date': '2020-11-15 19:56:22', 'is_admin': '0'}}

    def registration(self, login, password, is_admin):
        if self.check_uniqueness_of_login(login):
            if self.check_password(password):
                date_ = datetime.today()
                Authorization.allUsers[login] = {'password': f'{password}', 'date': f'{date_}'[:-7],
                                                 'is_admin': is_admin}
                print('> Your account had been created')
                return True
            else:
                print('> Incorrect password ')
                return False
        else:
            print('> Login is already in use')
            return False

    def authorization_(self, login, password):
        if login in Authorization.allUsers:
            if Authorization.allUsers.get(login).get('password') == password:
                print('> Successfully')
                return True
            else:
                print('> Incorrect password or login')
                return False
        else:
            print('> Incorrect password or login')
            return False

    def check_password(self, password):
        len_password = len(password)
        return False if len(re.findall(r'[a-zA-Z0-9]', password)) != len_password \
                        or len_password < 8 else True

    def check_uniqueness_of_login(self, login):
        return False if login in Authorization.allUsers else True


class User(Authorization):

    def __init__(self, log, passw, is_admin='0'):
        self.log = log
        self.passw = passw
        self.is_admin = is_admin

    def create_post(self, post_content):
        date_post = datetime.today()
        Post(self.log, post_content, f'{date_post}'[:-7])

    def show_info_about_users(self):
        if Authorization.allUsers[self.log]['is_admin'] == '1':
            for i in Authorization.allUsers:
                print('**' * 30)
                date_ = Authorization.allUsers[i]['date']
                post_of_user = Post.All_posts.get(i)
                print(f'User: {i}, date of registration: {date_}\nPosts: {post_of_user}')
                print('**' * 30)
        else:
            print('No permission')


class Post:
    All_posts = {'Don': [['Hello world!', '2020-11-16 11:00:22']]}

    def __init__(self, log, post_content, date_post):
        self.log = log
        self.post_content = post_content
        self.date_post = date_post
        self.store_post()

    def store_post(self):
        if self.log not in Post.All_posts:
            Post.All_posts[self.log] = []
        Post.All_posts[self.log].append([self.post_content, self.date_post])
        print('> Post had been created')


def func_of_users(users_):
    while True:
        next_action = input('> Enter 0 - create new post, 1 - show info about users, 2 - exit: ')
        if next_action == '0':
            post = input('> Enter content of new post: ')
            users_.create_post(post)
        elif next_action == '1':
            users_.show_info_about_users()
        elif next_action == '2':
            print('Logout of account ...')
            break


while True:
    print('::' * 30)
    choose_func = input('> Enter 0 - registration, 1 - authorization: ')
    if choose_func == '0':
        print('--' * 20, '\nRegistration')
        login_ = input('Enter login: ')
        password_ = input('Enter password: ')
        repeat_password = input('Enter password: ')
        admin_or_user = input('0 - user, 1 - admin: ')
        if password_ != repeat_password:
            print('Not the same passwords')
        else:
            user = User(login_, password_, admin_or_user)
            if user.registration(login_, password_, admin_or_user):
                func_of_users(user)
    elif choose_func == '1':
        print('--' * 20, '\nAuthorization')
        login_ = input('Enter login: ')
        password_ = input('Enter password: ')
        user = User(login_, password_)
        if user.authorization_(login_, password_):
            func_of_users(user)
