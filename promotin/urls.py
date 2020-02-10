from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, signup_influencer, signup_umkm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/umkm/', signup_umkm, name='signup_umkm'),
    path('accounts/signup/influencer/', signup_influencer, name='signup_influencer'),    

    path('', index, name='index'),

    path('project/', include('core.urls')),
    # path('project/detail/', include('core.urls', namespace='project-detail')),

    path('influencer/all/', include('core.urls', namespace='influencers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)