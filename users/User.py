class User:

    all_posts = []

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.user_post_storage = []
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail: {self.email}"
    
    def create_post(self, post):
        self.user_post = {}
        self.post = post
        self.user_post[self.username] = post
        self.user_post_storage.append(self.user_post)
        self.all_posts.append(self.user_post)

    def view_posts(self):
        return self.user_post_storage
    
    def delete_post(self, post):
        for p in self.user_post_storage:
            if p[self.username] == post: #this will access the value of the dictionary
                self.user_post_storage.remove(p)
        return self.user_post_storage
