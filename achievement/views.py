from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from achievement.models import *
# Create your views here.

def contrib_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'contribution')
	if achieve_obj:
		contrib_obj = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			c_obj = get_object_or_404(Contribution, achievement_id = achieve_id)
			if c_obj:	
				contrib_obj.append(c_obj)
		return render_to_response('achievement/contrib_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'contrib_obj':contrib_obj}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Contribution'}, RequestContext(request))

def article_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'article')
	if achieve_obj:
		article_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			article_obj = get_object_or_404(Article, achievement_id = achieve_id)
			if article_obj:	
				article_list.append(article_obj)
		return render_to_response('achievement/article_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'article_list':article_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Article'}, RequestContext(request))


def gsoc_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'gsoc')
	if achieve_obj:
		gsoc_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			gsoc_obj = get_object_or_404(Gsoc, achievement_id = achieve_id)
			if gsoc_obj:	
				gsoc_list.append(gsoc_obj)
		return render_to_response('achievement/gsoc_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'gsoc_list':gsoc_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Gsoc'}, RequestContext(request))


