from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from django.conf import settings

from django.shortcuts import render


def custom_404(request):
    return render(request, '404.html', {}, status=404)

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

def exception_handler(exc, context):
    if not settings.DEBUG:
        request = context.get('request')
        exception_handled = (Http404,)

        if isinstance(exc,exception_handled):
            status_code = status.HTTP_404_NOT_FOUND
        else:
            status_code = getattr(exc,'status_code',status.HTTP_500_INTERNAL_SERVER_ERROR)
        request_urlconf = getattr(request,'urlconf','vkmobile.urls')
        root_urlconf = __import__(request_urlconf,fromlist=1)
        handler = getattr(root_urlconf,'handler%s' %status_code,None)
        cls = getattr(handler,'cls',type('clsview',(),{'template_name':'404.html'}))
        if not isinstance(context.get('view'),cls) and callable(handler):
            response = handler(request)
        else:
            response = render(request,cls.template_name,locals(),status=status.HTTP_501_NOT_IMPLEMENTED)
        return response

