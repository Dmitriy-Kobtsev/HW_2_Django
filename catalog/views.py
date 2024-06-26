from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog import services
from catalog.forms import ProductForm, VersionForm, ProductDescriptionForm
from catalog.models import Product, Version, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     if not self.request.user.is_superuser or not self.request.user.has_perm('catalog.set_published'):
    #         queryset = queryset.filter(is_published=True)
    #         return queryset
    #     return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(version_current=True).first()
        return context_data


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    login_url = reverse_lazy('users:login')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    # def get_form_class(self):
    #     if self.request.user.has_perm("catalog.set_published") and not self.request.user.is_superuser:
    #         return ProductModeratorForm
    #     return ProductForm

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super(ProductUpdateView, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductDescriptionForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_info', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'

    def get_queryset(self):
        queryset = services.get_category()
        return queryset