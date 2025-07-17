from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    """
    Display the latest five published questions.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'index.html' template with latest questions in context
    :rtype: HttpResponse
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    """
    Display details for a specific question.

    :param request: HTTP request object
    :type request: HttpRequest
    :param question_id: ID of the question to retrieve
    :type question_id: int
    :return: Rendered 'detail.html' template with the question object
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    """
    Display results for a specific question.

    :param request: HTTP request object
    :type request: HttpRequest
    :param question_id: ID of the question to retrieve
    :type question_id: int
    :return: Rendered 'results.html' template with the question object
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    """
    Handle voting on a specific question's choice.

    :param request: HTTP request object
    :type request: HttpRequest
    :param question_id: ID of the question to vote on
    :type question_id: int
    :raises KeyError: If no choice is selected in POST data
    :raises Choice.DoesNotExist: If selected choice does not exist
    :return: Redirects to the results page if successful; redisplays voting form with error otherwise
    :rtype: HttpResponseRedirect or HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect after POST to prevent resubmission on back button
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
