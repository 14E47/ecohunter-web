from oscar.apps.catalogue.views import ProductCategoryView as CoreProductCategoryView

class ProductCategoryView(CoreProductCategoryView):
    def get_context_data(self, **kwargs):
        params = self.request.GET.dict()
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        context.update(search_context)

        # attribute_menu_option = self.request.GET.dict().values()
        # attribute_menu_option_products = []
        # if attribute_menu_option:
        #     for product in context['products']:
        #         if attribute_menu_option[0] in product.attribute_summary:
        #             attribute_menu_option_products.append(product)
        #     context['products'] = attribute_menu_option_products
        return context
