from django.core.exceptions import PermissionDenied

from shop.models import (
    BlockedIPModel,
    URLFromModel,
)


class BlockingIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if BlockedIPModel.objects.filter(ip_name=ip).exists():
            raise PermissionDenied
        response = self.get_response(request)
        return response


class RecordingURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_from = request.META.get("HTTP_REFERER")
        url_to = request.META.get("HTTP_HOST")
        if url_from is not None and url_to is not None:
            info = URLFromModel(url_from=url_from, url_to=url_to)
            info.save()
        response = self.get_response(request)
        return response
