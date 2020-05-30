# this script is run into django shell to get some test data
# for recommendations testing.


from online_shop.shop.models import Product

products = Product.objects.all()

for i in products:
    print(i, i.id)


black_tea = Product.objects.get(id=3)
chocolate = Product.objects.get(id=4)
green_tea = Product.objects.get(id=2)
tea = Product.objects.get(id=5)

from online_shop.shop.recommender import Recommender

r = Recommender()
r.products_bought([black_tea, green_tea])
r.products_bought([black_tea, tea])
r.products_bought([black_tea, chocolate])
r.products_bought([chocolate, black_tea])
r.products_bought([tea, green_tea])


# now test if suggestions work:
from django.utils.translation import activate
activate('en')
suggest = r.suggest_products_for([black_tea])
print(suggest)

exit()
