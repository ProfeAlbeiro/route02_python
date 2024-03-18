from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Reporter, Article

def create(request):
    rep = Reporter(first_name="Edwin", last_name="Villamil", email="earamos42@misena.edu.co")
    rep.save()
    
    art1 = Article(headline="Lorem ipsum dolot", pub_date=date(2022,5,5), reporter=rep)
    art1.save()
    art2 = Article(headline="Lorem set aimet", pub_date=date(2022,3,7), reporter=rep)
    art2.save()
    art3 = Article(headline="dolot ipsum lorem", pub_date=date(2022,4,9), reporter=rep)
    art3.save()

    # result = art1.reporter.first_name
    # result = rep.article_set.all()
    # result = rep.article_set.filter(headline="dolot ipsum lorem")
    result = rep.article_set.count()

    return HttpResponse(result)