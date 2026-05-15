from django import forms

from .models import ContactSubmission, NewsletterSubscriber

INPUT_CLASSES = (
    "mt-2 w-full rounded-none border-0 border-b-2 border-line bg-transparent px-0 py-3 text-sm "
    "font-normal text-ink placeholder:text-muted/50 focus:border-gold focus:outline-none focus:ring-0"
)
TEXTAREA_CLASSES = INPUT_CLASSES + " min-h-40"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Enter your full name"}),
            "email": forms.EmailInput(attrs={"class": INPUT_CLASSES, "placeholder": "Enter your email"}),
            "phone": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Enter phone number"}),
            "subject": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Enter your subject"}),
            "message": forms.Textarea(
                attrs={"class": TEXTAREA_CLASSES, "placeholder": "Enter your message", "rows": 6}
            ),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": INPUT_CLASSES, "placeholder": "Enter your email"}),
        }
