from .models import Category


def categories_all(request):
    return {"categories_all": Category.objects.all()}
