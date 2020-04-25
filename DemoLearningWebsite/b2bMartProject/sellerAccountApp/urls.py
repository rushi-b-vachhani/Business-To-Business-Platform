from django.conf.urls import url
from . import views

app_name = 'sellerAccountUrls'

urlpatterns = [
	url(r'^$', views.register_seller, name='RegisterSeller'),
	url(r'^sellerBusinessUpdate$', views.register_business_details, name='sellerBusinessUpdate'),
	url(r'^sellerAddProducts$', views.register_products, name='sellerAddProducts$'),
	url(r'^sellerBusinessAddress$', views.register_seller_address, name='sellerBusinessAddress$'),
	# url(r'^fromPage/(?P<var_from_page>[\s\w-]*)/$', views.signin_view, name='fromPage'),
	# url(r'^ProfileDetail/$', views.create_profile_view, name='ProfileDetail'),
	# url(r'^SignUp/$', views.signup_view, name='SignUp'),
	# url(r'^Logout/$', views.logout_view, name='Logout'),
]
