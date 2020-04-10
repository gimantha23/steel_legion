from django.db.models import Q
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(type__icontains=query)
            return Product.objects.filter(lookups)
        return Product.objects.none()
