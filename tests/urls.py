from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from drfpasswordlesskvn.settings import api_settings
from drfpasswordlesskvn.views import (ObtainEmailCallbackToken,
                                   ObtainMobileCallbackToken,
                                   ObtainAuthTokenFromCallbackToken,
                                   VerifyAliasFromCallbackToken,
                                   ObtainEmailVerificationCallbackToken,
                                   ObtainMobileVerificationCallbackToken, )

app_name = 'drfpasswordlesskvn'

urlpatterns = [
    path('', include('drfpasswordlesskvn.urls')),
]

format_suffix_patterns(urlpatterns)
