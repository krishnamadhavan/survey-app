from rest_framework import generics, permissions

from questionnaire import serializers


class CreateSurveyView(generics.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.CreateSurveySerializer
