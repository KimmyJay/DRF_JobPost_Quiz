from rest_framework import serializers
from post.models import *

from datetime import datetime, timedelta
from django.utils import timezone


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        # fields = "__all__"
        fields = ["company_name", "business_area"]


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        # fields = "__all__"
        fields = ["id", "job_type", "company", "job_description", "salary"]


class JobPostSkillsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillset
        # fields = "__all__"
        fields = ["id", "skill_set", "job_post"]