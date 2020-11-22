from django.http import JsonResponse
import requests
import requests_cache
import json
from ratelimit.decorators import ratelimit
from django.core.paginator import Paginator
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from . import serializer

requests_cache.install_cache('stackapi_cache', backend='sqlite', expire_after=240)

class StackSearchAPI(APIView):
    serializer_class = serializer.StackSearchSerializer
    def get(self, request, format=None):
        an_view = [
            'User Post function to search.'
        ]

        return Response({'message': 'Advansearch API', 'an_apiview': an_view})

    @ratelimit(key='user_or_ip', rate='5/m')
    @ratelimit(key='user_or_ip', rate='100/d')
    def post(self, request, format=None):
        page = request.data["page"]
        pagesize = request.data["pagesize"]
        fromdate = request.data["fromdate"]
        todate = request.data["todate"]
        min = request.data["min"]
        order = request.data["order"]
        sort = request.data["sort"]
        q = request.data["q"]
        max = request.data["max"]
        accepted = request.data["accepted"]
        wiki = request.data["wiki"]
        views = request.data["views"]
        url = request.data["url"]
        user = request.data["user"]
        title = request.data["title"]
        tagged = request.data["tagged"]
        nottagged = request.data["nottagged"]
        notice = request.data["notice"]
        migrated = request.data["migrated"]
        closed = request.data["closed"]
        body = request.data["body"]
        answers = request.data["answers"]
        
        endpoint = 'https://api.stackexchange.com/2.2/search/advanced'
        payload = {"page": page ,
                   "pagesize": pagesize	,
                   "fromdate": fromdate	,
                   "todate": todate,
                   "min": min,
                   "max": max,
                   "order": order,
                   "sort": sort,
                   "q": q,
                   "accepted": accepted,
                   "answers": answers	,
                   "body": body,
                   "closed": closed,
                   "migrated": migrated,
                   "notice": notice,
                   "nottagged": nottagged,
                   "tagged": tagged,
                   "title": title,
                   "user": user,
                   "url": url,
                   "views": views,
                   "wiki": wiki,
                    "site": "stackoverflow",
                }
        response = requests.get(url=endpoint, params=payload)
        print(response.url)
        return Response(response.json())