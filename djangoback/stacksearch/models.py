from django.db import models

order_choices = ( 
    ("desc", "desc"), 
    ("desc", "asc"), 
) 

sort_choices = ( 
    ("activity", "activity"), 
    ("votes", "votes"),
    ("creation", "creation"),
    ("relevance", "relevance"), 
) 

boolean_choices =  (
    ('', ''),
    ("True", "True"), 
    ("False", "False"), 
) 

class StackSearchModel(models.Model):
    page = models.IntegerField()
    pagesize = models.IntegerField()
    fromdate = models.DateField()
    todate = models.DateField()
    min = models.DateField()
    max = models.DateField()
    sort = models.CharField(max_length=999, choices=sort_choices, default = 'activity')
    order = models.CharField(max_length=999, choices=order_choices, default='desc')
    q = models.CharField(max_length=999)
    accepted = models.CharField(max_length=999, choices=boolean_choices)
    answers = models.IntegerField()
    body = models.CharField(max_length=999)
    closed = models.CharField(max_length=999, choices=boolean_choices, default='')
    migrated = models.CharField(max_length=999, choices=boolean_choices, default='')
    notice = models.CharField(max_length=999, choices=boolean_choices, default='')
    nottagged = models.CharField(max_length=999)
    tagged = models.CharField(max_length=999)
    title = models.CharField(max_length=999)
    user = models.IntegerField()
    url = models.CharField(max_length=999)
    views = models.IntegerField()
    wiki = models.CharField(max_length=999, choices=boolean_choices, default='')
