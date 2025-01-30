from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Contact, Video, Image
from .forms import ContactForm, VideoForm, ImageUploadForm, CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'app/Home.html'


class AboutPageView(TemplateView):
    template_name = 'app/About.html'


class WikiDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/Wiki.html'


class WikiListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/Wiki_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_posts = Post.objects.filter(title__icontains=query)
        else:
            filtered_posts = Post.objects.all()
        context['posts'] = filtered_posts
        context['total_posts'] = Post.objects.count()
        context['total_users'] = User.objects.count()
        return context


class WikiCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/Wiki_create.html'
    success_url = reverse_lazy('Add')

class WikiUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/Wiki_update.html'
    success_url = reverse_lazy('Add')


class WikiDeleteView(DeleteView):
    model = Post
    template_name = 'app/Wiki_delete.html'
    success_url = reverse_lazy('Add')


class ContactPageView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'app/Contact.html'
    success_url = reverse_lazy('Contact')

    def form_valid(self, form):
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)


class VideoListView(ListView):
    model = Video
    template_name = 'app/video_list.html'
    context_object_name = 'videos'


class VideoUploadView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'app/Video.html'
    success_url = reverse_lazy('Video_list')


class VideoDetailView(DetailView):
    model = Video
    template_name = 'app/Video_comment.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = self.object
            comment.save()
            return redirect('Video_comment', pk=self.object.pk)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class ImageUploadView(CreateView):
    model = Image
    form_class = ImageUploadForm
    template_name = 'app/Image_upload.html'
    success_url = reverse_lazy('Image_gallery')


class ImageGalleryView(ListView):
    model = Image
    template_name = 'app/Image_gallery.html'
    context_object_name = 'images'
