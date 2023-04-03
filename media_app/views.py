from django.shortcuts import render,redirect
from .models import Images
from .forms import ImageForm
from django.views import View
from django.contrib import messages



# Create your views here.

class Homepage(View):
   
   def get(self, request, id=None):
      imgs = Images.objects.all()
      context = {
         'all_imgs': imgs
      }
      return render(request, 'media_app/homepage.html', context)
      

class AddImagesView(View):
   
   def get(self, request):
      print('\n \n here 1')
      form = ImageForm()
      print('\n \n here 1')
      
      context = {
         
         'form': form,
      }
      
      return render(request, 'media_app/add_images.html', context)
   
   
   def post(self, request):
      form = ImageForm(request.POST, request.FILES)
      
      if form.is_valid():
         form.save()
         messages.success(request, 'Congrats! Image Successfuly Uploaded')
         return redirect('homepage')
      else:
         
         context = {
            'form': form,
         }
      return render(request, 'media_app/add_images.html', context)
   
         


class UpdateImage(View):
   
   def get(self, request,id=None):
      if id: 
         try:
            img = Images.objects.get(pk=id)
         except:
            return redirect('homepage')
         else:
            
            form = ImageForm(instance=img)
      
            context = {
               
               'form': form,
            }
            
            return render(request, 'media_app/update_imgs.html', context)
      return redirect('homepage')
   
   
   def post(self, request,id=None):
      if id: 
         try:
            img = Images.objects.get(pk=id)
         except:
            return redirect('homepage')
         else:
            
            form = ImageForm(request.POST, request.FILES, instance=img)
            
            if form.is_valid():
               form.save()
               messages.success(request, 'Congrats Data Successfuly Updated!')
               return redirect('homepage')
            
      
            context = {
               
               'form': form,
            }
            
            return render(request, 'media_app/update_imgs.html', context)
      return redirect('homepage')
      
   
   
