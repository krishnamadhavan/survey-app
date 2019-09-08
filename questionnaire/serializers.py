from django.db import transaction
from rest_framework import serializers

from questionnaire import models


class CreateFamilyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FamilyDetails
        exclude = ('survey',)


class CreateSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survey
        exclude = ('user',)

    @transaction.atomic()
    def create(self, validated_data):
        members = self.context['request'].data['family_details']

        validated_data['user'] = self.context['request'].user
        instance = self.Meta.model.objects.create(**validated_data)

        for index, member in enumerate(members):
            s_no = index + 1
            models.FamilyDetails.objects.create(survey=instance, s_no=s_no, **member)

        return instance
