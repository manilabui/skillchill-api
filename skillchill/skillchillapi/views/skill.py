from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from skillchillapi.models import Skill


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for skills

    Arguments:
        serializers
    """

    # skillager = SkillagerSerializer(many=True)

    class Meta:
        model = Skill
        url = serializers.HyperlinkedIdentityField(
            view_name='skill',
            lookup_field='id'
        )

        fields = ('id', 'name', 'avatar', 'created_at')
        depth = 2


class Skills(ViewSet):
    """Skills in Skillchill"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single skill

        Returns:
            Response -- JSON serialized skill instance
        """
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        skills = Skill.objects.all()
        serializer = SkillSerializer(
            skills,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
