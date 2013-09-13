import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django import forms
from kapai_django.classes import KapaiContext, ImageProcessor
from kapai_django.gallery.models import Gallery, GalleryItem

def index(request):
	return render_to_response('gallery/index.html', {'show_side_recruitment': True}, context_instance=KapaiContext(request))

def viewgallery(request, slug=''):
	view_gallery = get_object_or_404(Gallery, slug=slug)
	return render_to_response('gallery/viewgallery.html', {'show_side_recruitment': True, 'view_gallery': view_gallery}, context_instance=KapaiContext(request))


class ImageUploadForm(forms.Form):
	gallery = forms.ModelChoiceField(queryset=Gallery.objects.all(), required=True)
	name = forms.CharField(max_length=50, required=True)
	description = forms.CharField(max_length=500)
	image = forms.ImageField(required=True)

def upload(request):
	if not request.user.is_authenticated():
		raise Http404
		return
	
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			proc = ImageProcessor()
			filename = proc.save_file_upload(form.cleaned_data['image'])
			sized_filename = proc.resize_image(filename, 650, 600)
			thumb_filename = proc.resize_image(filename, 100, 80)
			img = GalleryItem(gallery=form.cleaned_data['gallery'], name=form.cleaned_data['name'], uploaded_date=datetime.date.today(), large_url=filename, image_url=sized_filename, thumb_url=thumb_filename, description=form.cleaned_data['description'])
			img.save()

	uploadform = ImageUploadForm()
	return render_to_response('gallery/upload.html', {'show_side_recruitment': False, 'uploadform': uploadform}, context_instance=KapaiContext(request))