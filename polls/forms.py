from django import forms
from django.forms import BaseInlineFormSet
from polls.models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_text", "pub_date")
        widgets = {
            "pub_date": forms.SelectDateWidget
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("choice_text", "votes")


class BaseChoiceFormset(BaseInlineFormSet):
    def clean(self):
        choice_text_list = [form["choice_text"].value() for form in self.forms if form["DELETE"].value() is False]
        if len(choice_text_list) == 0 or not any(choice_text_list):
            raise forms.ValidationError("choice_textが全て空")


ChoiceFormset = forms.inlineformset_factory(Question, Choice, ChoiceForm, formset=BaseChoiceFormset, extra=3, max_num=3)
