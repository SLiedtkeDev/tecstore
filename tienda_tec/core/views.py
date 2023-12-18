from django.views.generic import RedirectView


class Home(RedirectView):
    pattern_name = 'store:product_list'
