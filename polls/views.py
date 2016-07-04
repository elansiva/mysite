from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#
def detail(request, question_id):
	return	HttpResponse("You are looking at Question %s." % question_id)


def results(request,question_id):
	response = "You are looking at the results of the question %s"
	return HttpResponse(response % question_id)


def vote(request, question_id):
	response ("You are voting on question %s.")
	return HttpResponse(response % question_id)