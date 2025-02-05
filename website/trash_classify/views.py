from django.shortcuts import render
from django.http import HttpResponseForbidden, FileResponse, HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
import os

from .forms import ImgUploadForm
from django.utils import timezone
from .models import HisData
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found
from django.conf import settings
from django.core.exceptions import PermissionDenied

# Create your views here.
import requests
def home(request):
    result = None  # Initialize result to None

    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.image:
                instance.label = None
                instance.add_date = timezone.now()
                instance.save()

                image_path = instance.image.path
                # trimmed_result = image_path[:]
                # instance.label_name = trimmed_result
                # instance.save()

                # # Store the result in session for the next GET request
                # request.session['result'] = trimmed_result
                # print(f"Storing result in session: {trimmed_result}")  # Debugging line

                result_json={}
                url = "http://model:8188/predict/"
                response = requests.get(url+"?img_path={}".format(os.path.abspath(image_path)))

                if response.status_code == 200:
                    result_json = response.json()  # or response.text depending on your API response
                    instance.label = result_json['label']
                    instance.label_name = result_json['label_name']
                    instance.save()
                else:
                    return {'label':-1, 'label_name':'ERROR'}

                # return redirect(reverse(upload_image))  # Redirect to clear POST data
                return render(request, 'home.html', {'form': ImgUploadForm(), 'result': f"{instance.label_name}"})

    else:
        form = ImgUploadForm()
        if 'result' in request.session:
            result = request.session['result']
            print(f"Retrieved result from session: {result}")  # Debugging line
            del request.session['result']  # Explicitly clear after retrieving

    return render(request, 'home.html', {'form': form, 'result': result})

def about(request):
    try:
        return FileResponse(open(os.path.join(settings.BASE_DIR, 'static', 'Trash Classify.pdf'), 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return page_not_found(request, exception=None)
    # return render(request, 'about.html')

def serve_picture(request, filename):
    # print('!!!!1')
    # raise PermissionDenied
    # return permission_denied(request)
    # Check if the user is in the STAFF_MEMBERS group
    if not request.user.is_staff:
        # return HttpResponseNotFound("<!DOCTYPE html><html lang=\"en\"><head><title>Not Found</title></head><body><h1>Not Found</h1><p>The requested resource was not found on this server.</p></body></html>")
        # return HttpResponseForbidden("Access forbidden: The URL you requested is not allowed.")
        return page_not_found(request, exception=None)

    # Define the path to your 'pics/' directory
    # pics_path = os.path.join(settings.BASE_DIR, 'images')
    pics_path = os.path.join(settings.UPLOAD_ROOT, 'images')

    # Build the full file path
    file_path = os.path.join(pics_path, filename)

    # Ensure the file exists
    if not os.path.exists(file_path):
        return HttpResponseForbidden("File not found.")

    # Serve the file
    return FileResponse(open(file_path, 'rb'))


# def upload_image(request):
#     result = None  # To store the trimmed result for display

#     if request.method == 'POST':
#         form = ImgUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Save the form instance but add extra fields
#             instance = form.save(commit=False)  # Do not save yet, to modify fields

#             if instance.image:
#                 # Automatically handle label, label_name, and add_date
#                 instance.label = None  # Or any logic you need to set for 'label'
#                 instance.label_name = None  # Or any logic you need to set for 'label_name'
#                 instance.add_date = timezone.now()  # Set the current time for 'add_date'
    
#                 instance.save()  # Now save the object to the database
#                 # return redirect('success')  # Redirect to a success page after upload

#                 image_path = instance.image.path
#                 trimmed_result = image_path[:]  # Last 10 characters of the path

#                 # Update the label_name with the trimmed result
#                 instance.label_name = trimmed_result
#                 instance.save()  # Save the updated instance

#                 # Set result to return to the user
#                 result = trimmed_result
#                 # form = ImgUploadForm()
#     else:
#         form = ImgUploadForm()  # Show empty form for GET request
    
#     return render(request, 'upload.html', {'form': form, 'result': result})

# def upload_success(request):
#     return render(request, 'success.html')


@login_required
def display(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Access forbidden: The URL you requested is not allowed.")
    latest_data = HisData.objects.order_by('-add_date').first()
    context = {
        'latest_data': latest_data
    }
    return render(request, 'display.html', context)

@login_required
def latest_image_data(request):
    if not request.user.is_staff:
        return JsonResponse({'ERROR': 'Access Forbidden'})
    # Get the latest image and its label data
    latest_data = HisData.objects.order_by('-add_date').first()
    if latest_data:
        response_data = {
            'image_url': latest_data.image.url,
            'label_name': latest_data.label_name,
            'label': latest_data.label,
        }
    else:
        response_data = {}

    return JsonResponse(response_data)

@login_required
def load_older_images(request):
    if not request.user.is_staff:
        return JsonResponse({'ERROR': 'Access Forbidden'})
    
    page = int(request.GET.get('page', 1))
    images_per_page = 1  # Number of images to preload

    # Retrieve older images based on pagination
    images = HisData.objects.order_by('-add_date')[images_per_page * page : images_per_page * (page + 1)]
    
    image_data = []
    for image in images:
        image_data.append({
            'image_url': image.image.url,
            'label_name': image.label_name,
            'label': image.label
        })
    
    return JsonResponse({'images': image_data})

def test(request):
    result = None  # Initialize result to None

    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.image:
                instance.label = None
                instance.add_date = timezone.now()
                instance.save()

                image_path = instance.image.path
                # trimmed_result = image_path[:]
                # instance.label_name = trimmed_result
                # instance.save()

                # # Store the result in session for the next GET request
                # request.session['result'] = trimmed_result
                # print(f"Storing result in session: {trimmed_result}")  # Debugging line

                result_json={}
                url = "http://model:8188/predict/"
                response = requests.get(url+"?img_path={}".format(os.path.abspath(image_path)))

                if response.status_code == 200:
                    result_json = response.json()  # or response.text depending on your API response
                    instance.label = result_json['label']
                    instance.label_name = result_json['label_name']
                    instance.save()
                else:
                    return {'label':-1, 'label_name':'ERROR'}

                # return redirect(reverse(upload_image))  # Redirect to clear POST data
                return render(request, 'test.html', {'form': ImgUploadForm(), 'result': f"{instance.label_name}"})

    else:
        form = ImgUploadForm()
        if 'result' in request.session:
            result = request.session['result']
            print(f"Retrieved result from session: {result}")  # Debugging line
            del request.session['result']  # Explicitly clear after retrieving

    return render(request, 'test.html', {'form': form, 'result': result})
