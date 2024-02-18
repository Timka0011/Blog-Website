from .models import News


def NewsProcessor(request):
    news_processor = News.objects.all().order_by("-id")
    return {"news_processor": news_processor}
