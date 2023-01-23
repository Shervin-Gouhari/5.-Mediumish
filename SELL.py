from articles.models import Article
from django.contrib.auth.models import User

users = User.objects.all()
users[0]
# or
user = User.objects.get(username="admin")
user

articles = Article.objects.all()
article = Article(title="this is title from shell", content="this is content from shell", author=user)
article.save()
articles

post = Article.objects.all()[0]
post
post.title = "new title from shell"
post.save()
post

articles = Article.objects.filter(author__username="admin", status="checking").exclude(title__startswith="new", content__icontains="|")
articles
articles = Article.objects.filter(author=1) # id
articles
articles = Article.objects.filter(author__username="admin", status="checking").order_by("title") # or ("-title")
articles

article = Article.objects.all()[0]
article.delete()