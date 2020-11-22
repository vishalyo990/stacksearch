from rest_framework import serializers
from .models import StackSearchModel

class StackSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackSearchModel
        fields = ('page', 
                    'pagesize', 
                    "fromdate",
                    "todate",
                    "min",
                    "max",
                    "order",
                    "sort",
                    "q",
                    "accepted",
                    "answers",
                    "body",
                    "closed",
                    "migrated",
                    "notice",
                    "nottagged",
                    "tagged",
                    "title",
                    "user",
                    "url",
                    "views",
                    "wiki",)