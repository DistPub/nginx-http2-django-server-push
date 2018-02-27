import re
from django.conf import settings


class AddLinkHeaderMiddleware(object):
    def process_response(self, request, response):
        if not settings.ENABLE_SERVER_PUSH:
            return response

        if 'text/html' not in response['content-type']:
            return response

        content = str(response.content)
        links = re.findall(r'(<(link|script|img).+?/?>)', content)
        link_headers = []
        for link in links:
            if re.search(r'rel=.+preload.+', link[0]) and re.search(r'as=.+\w.+', link[0]):
                if link[1] != 'link':
                    href = re.search(r'src=[\'"](.+?)[\'"]', link[0]).group(1)
                else:
                    href = re.search(r'href=[\'"](.+?)[\'"]', link[0]).group(1)
                as_value = re.search(r'as=[\'"](.+?)[\'"]', link[0]).group(1)
                link_headers.append('<{}>; as={}; rel=preload'.format(href, as_value))
        response['Link'] = ','.join(link_headers)
        return response
