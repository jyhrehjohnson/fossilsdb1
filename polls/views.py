#  from django.http import HttpResponseRedirect
#  from django.shortcuts import get_object_or_404, render
#  from django.urls import reverse
#  from django.views import generic
#  from .models import Fossil
#  from .models import Fossil


#class IndexView(generic.ListView):
    #template_name = 'casts/index.html'
    #  context_object_name = 'latest_question_list'

    #def get_queryset(self):
        # """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]


#class DetailView(generic.DetailView):
    #model = Fossil, Primate
    #template_name = 'casts/fossil_detail.html'


#class ResultsView(generic.DetailView):
    #model = Fossil, Primate
    #template_name = 'casts/results.html'

    # def vote(request, question_id):
    ...  # same as above, no changes needed.
