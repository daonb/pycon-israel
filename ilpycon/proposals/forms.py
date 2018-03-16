from django import forms

from .models import TalkProposal, TutorialProposal


class ProposalForm(forms.ModelForm):

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
        fields = [
            "title",
            "audience_level",
            "duration",
            "language",
            "second_language",
            "description",
            "abstract",
            "additional_notes",
            "target_audience",
            "target_audience_other",
            "specific_props",
            "recording_release",
        ]


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "audience_level",
            "duration",
            "language",
            "second_language",
            "description",
            "abstract",
            "additional_notes",
            "target_audience",
            "target_audience_other",
            "specific_props",
            "recording_release",
        ]
