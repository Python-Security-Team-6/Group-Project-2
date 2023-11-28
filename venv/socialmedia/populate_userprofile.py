import os
import django
from faker import Faker
from django.core.wsgi import get_wsgi_application
from PIL import Image


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialmedia.settings")


django.setup()
application = get_wsgi_application()

from django.contrib.auth.models import User
from follow_unfollow.models import UserProfile

fake = Faker()

def populate_userprofile(num_profiles=15):
    for entry in range(num_profiles):
        #  User instance
        user = User.objects.create(username=fake.user_name())
        
        # UserProfile instance associated with the User
        profile_pic = populate_profile_pic()
        UserProfile.objects.create(user=user, profile_pic=profile_pic)

def populate_profile_pic():
    # a random image file
    image = Image.new('RGB', (100, 100))
    image.save('mystaticfiles/profile_pics/temp_image.jpg')
    return 'mystaticfiles/profile_pics/temp_image.jpg'

if __name__ == "__main__":
    populate_userprofile()
