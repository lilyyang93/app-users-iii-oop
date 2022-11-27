from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

user1 = User('Lily', 'Yang', 'lilyyang', 'lilyyang@email.com')
user2 = User('Alex', 'Song', 'alexsong', 'alexsong@email.com')
free_user1 = FreeUser('Mamba', 'Song', 'mambasong', 'mamba@dog.com')
premium_user1 = PremiumUser('Madam', 'Tasha', 'madamtasha', 'tasha@dog.com' )

user1.create_post('user 1 posting')
user2.create_post('user 2 posting')
user1.create_post('user 1 posting again')
free_user1.create_post('hi this is mamba')
free_user1.create_post('mamba\'s second post')
free_user1.create_post('mamba\'s third post')
premium_user1.create_post('hi this is tasha')

#print(User.all_posts)
#print(free_user1.view_posts())
#print(user1.view_posts())
#print(user1.delete_post('user 1 posting'))

