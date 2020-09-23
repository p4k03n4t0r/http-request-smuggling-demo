from mitmproxy import http
import re


def request(flow):
    if 'flag' in flow.request.url:
        flow.response = http.HTTPResponse.make(403, b"Forbidden, but nice try ;)\n")
