from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from kapai_django.classes import KapaiContext
from kapai_django.index.models import NewsItem
from kapai_django.gallery.models import Gallery, GalleryItem

def redirect(request):
	if request.path.startswith("/apply"):
		return HttpResponseRedirect("/forums/viewforum.php?f=7")

        if request.path.startswith("/guide"):
                return HttpResponseRedirect("/forums/viewtopic.php?f=4&t=4038")

        if request.path.startswith("/charter"):
                return HttpResponseRedirect("/forums/viewtopic.php?f=3&t=3")

def forum_redir(request):
	return HttpResponseRedirect("/forums" + request.get_full_path())

def index(request):
	news_items = NewsItem.objects.all().order_by('-when_published').filter(active=True)
	gallery_items = GalleryItem.objects.filter(gallery__slug='kills', active=True).order_by('ordering', '-uploaded_date')[:3]
	return render_to_response('index/index.html', {'news_items': news_items, 'gallery_items': gallery_items, 'show_side_progression': True, 'show_side_recruitment': True}, context_instance=KapaiContext(request))
