from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from blog import forms
from blog.forms import CommentForm
from blog.models import Blog, Comment


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 1


class BlogDetailView(generic.View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        blog.view += 1
        blog.save()
        form = CommentForm()
        return render(request, 'blog/blog_detail.html', {'object': blog, 'form': form})

    def post(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(description=form.cleaned_data.get('description'), user=self.request.user,
                                   blog=blog, pattern_id=form.cleaned_data.get('pattern'))
        return render(request, 'blog/blog_detail.html', {'object': blog, 'form': form})

# class BlogDetailView(FormMixin, generic.DetailView):
#     model = Blog
#     form_class = forms.CommentForm
#
#     def get_success_url(self):
#         return reverse('blog:detail_blog', kwargs={'slug': self.object.slug})
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#
#     def form_valid(self, form):
#         Comment.objects.create(description=form.cleaned_data.get('description'), user=self.request.user,
#                                blog=self.object, pattern_id=form.cleaned_data.get('pattern'))
#         return super(BlogDetailView, self).form_valid(form)
