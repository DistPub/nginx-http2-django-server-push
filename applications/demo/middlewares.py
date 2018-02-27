from django.conf import settings


class AddLinkHeaderMiddleware(object):
    def process_response(self, request, response):
        if not settings.ENABLE_SERVER_PUSH:
            return response

        response['Link'] = '</static/styles/index.css>; as=style; rel=preload'
        return response
