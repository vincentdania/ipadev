import logging

from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import ContactForm, NewsletterForm
from .recaptcha import verify_recaptcha
from .tasks import send_contact_notification

logger = logging.getLogger(__name__)


class ContactView(FormView):
    template_name = "engagement/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
        return context

    def form_valid(self, form):
        token = self.request.POST.get("g-recaptcha-response", "")
        if not verify_recaptcha(token, self._client_ip()):
            form.add_error(None, "Please complete the reCAPTCHA verification.")
            return self.form_invalid(form)

        submission = form.save()
        try:
            send_contact_notification.delay(submission.id)
        except Exception:
            logger.warning("Unable to queue contact notification for submission %s", submission.id)
        messages.success(self.request, "Thank you for contacting IPADEV. We will respond soon.")
        return super().form_valid(form)

    def _client_ip(self):
        forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if forwarded_for:
            return forwarded_for.split(",")[0].strip()
        return self.request.META.get("REMOTE_ADDR")


def newsletter_signup(request):
    if request.method != "POST":
        return redirect("home")

    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        if request.headers.get("HX-Request"):
            return HttpResponse("<p class='text-sm text-emerald-700'>Thank you for subscribing.</p>")
        messages.success(request, "Thank you for subscribing.")
    else:
        if request.headers.get("HX-Request"):
            return render(request, "engagement/_newsletter_form.html", {"newsletter_form": form})
        messages.error(request, "Please enter a valid email address.")
    return redirect(request.META.get("HTTP_REFERER", "/"))
