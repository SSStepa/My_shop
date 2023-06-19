from django.core.exceptions import PermissionDenied

from shop.models import (
    BlockedIPModel,
    URLFromModel,
)


class BlockingIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = BlockedIPModel.objects.all()
        ip = request.META.get("REMOTE_ADDR")
        if ip in blocked_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response


class RecordingURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_from = request.META.get("HTTP_REFERER")
        now_url = request.META.get("HTTP_HOST")
        if url_from is not None and now_url is not None:
            info = URLFromModel(url_from=url_from, now_url=now_url)
            info.save()
        response = self.get_response(request)
        return response
