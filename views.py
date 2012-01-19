from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#Home page
def home(request):
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)

def test(request):
	t = get_template('test.html')
	html = t.render(Context())
	return HttpResponse(html)
	
#Resume page
def resume(request):
	t = get_template('resume.html')
	html = t.render(Context())
	return HttpResponse(html)
	
#Projects section
def projects_past(request):
	t = get_template('projects/past.html')
	html = t.render(Context())
	return HttpResponse(html)
	
def projects_current(request):
	t = get_template('projects/current.html')
	html = t.render(Context())
	return HttpResponse(html)
	
def projects_future(request):
	t = get_template('projects/future.html')
	html = t.render(Context())
	return HttpResponse(html)
	
#Photography page
def photography(request):
	t = get_template('photography.html')
	html = t.render(Context())
	return HttpResponse(html)
	
