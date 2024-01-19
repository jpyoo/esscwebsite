from django.shortcuts import render
from .models import Post, Event, Announcement, About, Home1, Home2, Home3, Member, ArchiveBanners
from django.http import HttpResponse
from django.apps import apps
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact  # Import your ContactEntry model
from django.contrib.auth.decorators import user_passes_test
from .utils import get_instagram_posts

# Define a function to check if the user is an admin
def is_admin(user):
    return user.is_superuser

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')[:3],
        'events': Event.objects.all().order_by('-date_posted'),
        'announcements': Announcement.objects.all().order_by('-date_posted')[:3],
        'about': About.objects.all().order_by('-date_posted')[:3],
        'home1': Home1.objects.all().order_by('-date_posted')[:3],
        'home2': Home2.objects.all().order_by('-date_posted')[:3],
        'home3': Home3.objects.all().order_by('-date_posted')[:3],
        'members': Member.objects.all(),
        'form': ContactForm(),
        # 'instagram_posts': get_instagram_posts(),
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Write to database
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            context['success'] = True

    return render(request, 'index.html', context)

@user_passes_test(is_admin)
def contact(request):
    context = {
        'contacts': Contact.objects.all().order_by('-date_posted'),
        'home2': Home2.objects.all().order_by('-date_posted')[:3],
    }
    return render(request, 'contacts.html', context)

def archive(request):
    context = {
        'members': Member.objects.all(),
        'home2': ArchiveBanners.objects.all().order_by('-date_posted')[:3],
    }
    return render(request, 'archive.html', context)

def serve_image(request, model_name, image_id):
    model = apps.get_model('homepage', model_name)
    
    try:
        instance = get_object_or_404(model, pk=image_id)
        image_data = instance.image.read()
        response = HttpResponse(image_data, content_type='image/jpeg')  # Adjust content_type based on your image format
        return response
    except model.DoesNotExist:
        return HttpResponse(status=404)
    
