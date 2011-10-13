
from django.conf.urls.defaults import *

import powerdb2.backend.views

proxy_conf = {
    'destination' : 'http://local.cs.berkeley.edu:8079',
    'prefix' : 'backend'
    }

urlpatterns = patterns('',
    (r'^.*$', 'revproxy.proxy_request', proxy_conf)
)
