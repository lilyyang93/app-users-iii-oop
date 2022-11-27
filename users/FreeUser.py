from users.User import User

class FreeUser(User):
    def create_post(self, post):
        if len(self.user_post_storage) < 2:
            self.user_post = {}
            self.post = post
            self.user_post[self.username] = post
            self.user_post_storage.append(self.user_post)
            self.all_posts.append(self.user_post)
        else:
            return print('You have reached your maximum number of posts. Please delete a post or consider upgrading to a Premium account.')
