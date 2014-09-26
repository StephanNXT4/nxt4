from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'nxt4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'email_registration.views.landingpage', name='landingpage'),
    url(r'^email_registration/', include('email_registration.urls', namespace='email_registration')),
]
