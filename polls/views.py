from uuid import UUID
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

from .service import QuestionApplicationService, ChoiceApplicationService
from .forms import QuestionForm, ChoiceFormset


class IndexView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_entities = QuestionApplicationService.get_latest_list(5)
        context.update({
            'latest_question_list': question_entities
        })
        return context


class RegisterView(generic.FormView):
    template_name = 'polls/register.html'
    success_url = reverse_lazy('polls:index')

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs.update({
            'question_form': QuestionForm(),
            'choice_formset': ChoiceFormset(prefix='choice'),
        })
        return kwargs

    def post(self, request, *args, **kwargs):
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormset(request.POST, prefix='choice')
        if question_form.is_valid() and choice_formset.is_valid():
            return self.form_valid(question_form, choice_formset)
        else:
            return self.form_invalid(question_form, choice_formset)

    def form_valid(self, question_form, choice_formset):
        choice_cleaned_data_list = [form for form in choice_formset.cleaned_data if form and form["DELETE"] is False]
        QuestionApplicationService.create_question_choice_set(
            question_data=question_form.cleaned_data,
            choice_data_list=choice_cleaned_data_list
        )
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, question_form, choice_formset):
        return self.render_to_response(self.get_context_data())


class DetailView(TemplateView):
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = kwargs.get("question_id", None)
        if question_id is None:
            raise Http404("Question does not exist")
        choice_entities = ChoiceApplicationService.get_relate_list(question_id)
        context.update({
            "question_id": question_id,
            "choice_entities": choice_entities
        })
        return context


class ResultsView(TemplateView):
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = kwargs.get("question_id", None)
        if question_id is None:
            raise Http404("Question does not exist")
        question_entity = QuestionApplicationService.get(question_id)
        choice_entities = ChoiceApplicationService.get_relate_list(question_id)
        context.update({
            "question": question_entity,
            "choice_entities": choice_entities
        })
        return context


def vote(request, question_id):
    choice_entities = ChoiceApplicationService.get_relate_list(question_id)
    if not choice_entities:
        raise Http404("Question does not exist")
    if UUID(request.POST['choice']) is None:
        return render(request, 'polls/detail.html', {
            'question_id': question_id,
            "choice_entities": choice_entities,
            'error_message': "You didn't select a choice.",
        })

    ChoiceApplicationService.add_vote(UUID(request.POST['choice']))

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
