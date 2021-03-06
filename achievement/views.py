from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from achievement.models import *
# Create your views here.

def achieve_viewall(request):
	is_loggedin = False
        username = ''
	contrib_list = []
	article_list = []
	gsoc_list = []
	speaker_list = []
	intern_list = []
	contest_participant_list = []
	icpc_participant_list = []
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
        contrib_list = Contribution.objects.all()[:5]
	article_list = Article.objects.all()[:5]
        gsoc_list = Gsoc.objects.all()[:5]
        speaker_list = Speaker.objects.all()[:5]
        intern_list = Intern.objects.all()[:5]
	contest_list = Contest_won.objects.all()[:5]
	if contest_list:	
		contest_participant_list = []
		for contest_won_obj in contest_list:	
			c_id = contest_won_obj.contest_id
			c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
			contest_participant_list.extend(c_p_objs)
	icpc_list = ACM_ICPC_detail.objects.all().order_by('yr_of_participation')[:5]
	if icpc_list:
		for icpc_obj in icpc_list:
			team = icpc_obj.team_name
			i_p_objs = ACM_ICPC_Participant.objects.filter(team_name = team)
			icpc_participant_list.extend(i_p_objs)
		
	return render_to_response('achievement/achievement_viewall.html',{'username':username, 'is_loggedin':is_loggedin, 'contrib_list':contrib_list, 'article_list':article_list, 'gsoc_list':gsoc_list, 'speaker_list':speaker_list,'intern_list':intern_list, 'contest_list':contest_list, 'contest_participant_list':contest_participant_list, 'icpc_list':icpc_list, 'icpc_participant_list':icpc_participant_list},RequestContext(request))

def contrib_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	contrib_list = Contribution.objects.all()
	if contrib_list:
		return render_to_response('achievement/contrib_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'contrib_list':contrib_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Contribution'}, RequestContext(request))

def article_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	article_list = Article.objects.all()
	if article_list:
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
	gsoc_list = Gsoc.objects.all()
	if gsoc_list:
		return render_to_response('achievement/gsoc_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'gsoc_list':gsoc_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Gsoc'}, RequestContext(request))


def speaker_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	speaker_list = Speaker.objects.all()
	if speaker_list:
		return render_to_response('achievement/speaker_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'speaker_list':speaker_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Speaker'}, RequestContext(request))

def intern_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	intern_list = Intern.objects.all()
	if intern_list:
		return render_to_response('achievement/intern_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'intern_list':intern_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Internship'}, RequestContext(request))

def contest_won_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	contest_list = Contest_won.objects.all()
	if contest_list:	
		contest_participant_list = []
		for contest_won_obj in contest_list:	
			c_id = contest_won_obj.contest_id
			c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
			contest_participant_list.extend(c_p_objs)
		return render_to_response('achievement/contest_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'contest_list':contest_list, 'contest_participant_list':contest_participant_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Contest\'s won'}, RequestContext(request))

def icpc_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	icpc_list = ACM_ICPC_detail.objects.all().order_by('yr_of_participation')
	if icpc_list:
		icpc_participant_list = []
		for icpc_obj in icpc_list:
			team = icpc_obj.team_name
			i_p_objs = ACM_ICPC_Participant.objects.filter(team_name = team)
			icpc_participant_list.extend(i_p_objs)
		return render_to_response('achievement/icpc_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'icpc_list':icpc_list, 'icpc_participant_list':icpc_participant_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'ACM ICPC Contest'}, RequestContext(request))


