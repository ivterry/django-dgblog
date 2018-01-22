from django.conf.urls import url
from . import views  #importing all of our views located in /blog


# We are assigning a view called "post_list" to the ^$ url.
# The ^$ regex will match ^ (a begining) followed by $ (an end) -
# so only an empty string will match.
# That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/'
# is not part of the URL.  This pattern will tell Djago that views.post_list
# is the right place to go if someone enters your website at the 
# 'http://127.0.0.1:8000/' address.
#
# The last part, name='post_list', is the name of the URL that will be used
# to identify the view.
urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
]


