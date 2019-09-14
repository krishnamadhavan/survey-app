from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from questionnaire import models


class SurveyResource(resources.ModelResource):
    class Meta:
        model = models.Survey
        fields = [field.name for field in models.Survey._meta.fields]


class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource
    list_display = [field.name for field in models.Survey._meta.fields]


class FamilyDetailsResource(resources.ModelResource):
    class Meta:
        model = models.FamilyDetails
        fields = [field.name for field in models.FamilyDetails._meta.fields]


class FamilyDetailsAdmin(ImportExportModelAdmin):
    resource_class = FamilyDetailsResource
    list_display = [field.name for field in models.FamilyDetails._meta.fields]


admin.site.register(models.Survey, SurveyAdmin)
admin.site.register(models.FamilyDetails, FamilyDetailsAdmin)
