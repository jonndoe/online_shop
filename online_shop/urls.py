"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path("rosetta/", include("rosetta.urls")),
    path(_("payment/"), include("online_shop.payment.urls", namespace="payment")),
    path(_("admin/"), admin.site.urls),
    path(
        _("orders/"), include("online_shop.orders.urls", namespace="online_shop.orders")
    ),
    path(_("cart/"), include("online_shop.cart.urls", namespace="online_shop.cart")),
    path(_("coupons/"), include("online_shop.coupons.urls", namespace="coupons")),
    path("", include("online_shop.shop.urls", namespace="online_shop.shop")),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
