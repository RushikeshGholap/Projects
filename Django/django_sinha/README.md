Django notes - 

django-admin startproject imagepred

python manage.py

python manage.py startapp core


#Write main function in view.py of the core app
#Then in the urls.py add the path for views.py (and import from core)
#Add core in the installed apps in settings.py


#templates folder in the core, which contains all htmls
#static folder in core, which contains js, css etc

# in views.py return render(request, 'index.html')


# for upload images.files, first add the html code to add the upload button in index.html
# next you need a place to save / retrieve the files from, create a folder called media, outside the core folder
# next, in the settings.py add the URLs for the media folder (MEDIA_ROOT, for upload) (MEDIA_URL, for download)
# next, in the urls.py, after urlpatterns, add + static(upload path variable, download path variable)

