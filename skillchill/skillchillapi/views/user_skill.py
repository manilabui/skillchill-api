from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from skillchillapi.models import UserSkill
from .skillager import SkillagersSerializer
from .skill import SkillsSerializer


class UserSkillsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for user skills

    Arguments:
        serializers
    """
    skillager = SkillagersSerializer()
    skill = SkillsSerializer()

    class Meta:
        model = UserSkill
        url = serializers.HyperlinkedIdentityField(
            view_name='userskill',
            lookup_field='id'
        )
        depth = 2
        fields = ('id', 'skillager', 'skill', 'is_moderator')


class UserSkills(ViewSet):
    """UserSkills in Skillchill"""
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized userskill instance
        """
        new_user_skill= UserSkill()
        new_user_skill.skillager_id = request.auth.user.skillager.id
        new_user_skill.skill_id = request.data['skill_id']
        new_user_skill.is_moderator = request.data['is_moderator']
        new_user_skill.save()
        serializer = UserSkillsSerializer(
            new_user_skill,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single userskill

        Returns:
            Response -- JSON serialized userskill instance
        """
        try:
            user_skill = UserSkill.objects.get(pk=pk)
            serializer = UserSkillsSerializer(user_skill, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to the user skill pages resource
        that grabs all the user skills associated with

        Returns:
            Response -- JSON serialized list of user skills
        """
        skillager_id = self.request.query_params.get('skillager_id', None)
        skill_id = self.request.query_params.get('skill_id', None)
        user_skills = UserSkill.objects.all()

        if skillager_id is not None:
            user_skills = user_skills.filter(skillager_id=skillager_id)

        if skill_id is not None:
            user_skills = user_skills.filter(skill_id=skill_id)

        serializer = UserSkillsSerializer(
            user_skills,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests for a user skill

        Returns:
            Response -- Empty body with 204 status code
        """
        user_skill = UserSkill.objects.get(pk=pk)
        user_skill.is_moderator = request.data["is_moderator"]
        user_skill.save()
        serializer = UserSkillsSerializer(user_skill, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single user skill

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            user_skill = UserSkill.objects.get(pk=pk)
            user_skill.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except UserSkill.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.arg[0]},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
