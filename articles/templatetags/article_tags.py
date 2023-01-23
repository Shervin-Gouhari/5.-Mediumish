from django import template
from ..models import Article
from datetime import datetime

register = template.Library()

@register.simple_tag
def total_article_num():
    return Article.published.count()

# created_date and today are both strings, thereby we need to convert them into datetime objects in order to subtract
# string from time = strftime
# string points to time = strptime
@register.filter(name="isnew")
def new_article(value):
    created_date = value.strftime("%d %m %y")
    today = datetime.now().strftime("%d %m %y")
    created_date_prime = datetime.strptime(created_date, "%d %m %y")
    today_prime = datetime.strptime(today, "%d %m %y")
    return (today_prime - created_date_prime).days < 7