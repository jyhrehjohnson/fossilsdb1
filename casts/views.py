from django.views import generic
from .models import Fossil, Primate


class FossilListView(generic.ListView):
    #  model = Fossil
    context_object_name = 'fossil'

    def get_queryset(self):
        """Return a list of fossils """
        fossil = Fossil.objects.filter(classification_status='accepted')
        return fossil


class PrimateListView(generic.ListView):
    #  model = Primate
    context_object_name = 'primate'

    def get_queryset(self):
        """Return a list of primates """
        primate = Primate.objects.filter(classification_status='accepted')
        return primate


class FossilDetailView(generic.DetailView):
    model = Fossil


class PrimateDetailView(generic.DetailView):
    model = Primate
