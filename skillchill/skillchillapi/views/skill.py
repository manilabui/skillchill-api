from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from skillchillapi.models import Skill


# TODO: need to show the moderator + all members
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

        fields = ('id', 'url', 'name', 'avatar', 'created_at')


class Skills(ViewSet):
    """Skills in Skillchill"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized skill instance
        """
        new_skill = Skill()
        new_skill.name = request.data['name']
        new_skill.avatar = request.data['avatar']
        new_skill.save()

        serializer = SkillSerializer(
            new_skill,
            context={'request': request}
        )

        return Response(serializer.data)

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
        """Handle GET requests to skills resource

        Returns:
            Response -- JSON serialized list of skills
        """
        skills = Skill.objects.all()
        serializer = SkillSerializer(
            skills,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for an skill

        Returns:
            Response -- Empty body with 204 status code
        """
        skill = Skill.objects.get(pk=pk)
        skill.avatar = request.data["avatar"]
        skill.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single skill

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            skill = Skill.objects.get(pk=pk)
            skill.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Skill.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.arg[0]},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
