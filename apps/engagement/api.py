from rest_framework import mixins, serializers, viewsets

from .models import ContactSubmission, NewsletterSubscriber


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "phone", "subject", "message", "created_at"]
        read_only_fields = ["id", "created_at"]


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ["id", "email", "created_at"]
        read_only_fields = ["id", "created_at"]


class ContactSubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSubmissionSerializer
    queryset = ContactSubmission.objects.all()


class NewsletterSubscriberViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsletterSubscriberSerializer
    queryset = NewsletterSubscriber.objects.all()
