from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadImageForm
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dface import opencv_dface

def first_view(request): #Homepage
  return render(request, 'face_detection/first_view.html', {})

def uimage(request): #Simple Image upload template
  if request.method == 'POST':
      form = UploadImageForm(request.POST, request.FILES)
      if form.is_valid():
          myfile = request.FILES['image']
          fs = FileSystemStorage()
          filename = fs.save(myfile.name, myfile)
          uploaded_file_url = fs.url(filename)
      return render(request, 'face_detection/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
  
  else:
      form = UploadImageForm()
      return render(request, 'face_detection/uimage.html', {'form': form})


def dface(request): #Face detection app
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
 
            imageURL = settings.MEDIA_URL + form.instance.image.name
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)
 
            return render(request, 'face_detection/dface.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'face_detection/dface.html',{'form':form})