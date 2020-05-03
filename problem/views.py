from django.shortcuts import render,redirect,get_object_or_404
from . import models 
from . import tasks
from django.views.generic import (ListView,
                                DetailView,
                                CreateView)
# Create your views here.

class ProblemListView(ListView):
    model = models.Problem
    template_name = 'problem/problem_list.html'


class ProblemDetailView(DetailView):
    model = models.Problem
    template_name = 'problem/problem_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_test_cases'] = self.object.testcases.filter(is_sample=True).all()
        return context


class SubmitView(CreateView):
    model = models.Submission
    fields = ['problem','code','language']
    template_name = 'problem/submission_form.html'

    def get_form(self):
        form = super(SubmitView,self).get_form()
        initial_base = self.get_initial() 

        if(not 'pid' in self.kwargs) :
            return form 
        
        initial_base['problem'] = get_object_or_404(models.Problem,id=self.kwargs['pid'])
        form.initial = initial_base
        #form.fields['name'].widget = forms.widgets.Textarea()
        return form

    def form_valid(self, form):
        submission = form.save(commit=False)
        submission.save()
        
        tasks.submission_evaluate(submission.pk)
        # function call 

        return redirect(submission.get_absolute_url())


class SubmissionListView(ListView):
    model = models.Submission
    template_name = 'problem/submission_list.html'

    def get_queryset(self):
        return models.Submission.objects.order_by('-time')