from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from skillchillapi.models import Skillager


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for users

    Arguments:
        serializers
    """
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields = ('id', 'username', 'last_name',
                  'first_name', 'email', 'last_login')


class SkillagersSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for skillagers

    Arguments:
        serializers
    """
    user = UsersSerializer()

    class Meta:
        model = Skillager
        url = serializers.HyperlinkedIdentityField(
            view_name='skillager',
            lookup_field='id'
        )
        depth = 2
        fields = ('id', 'url', 'user', 'avatar')


class Users(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user instance
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UsersSerializer(
                user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class Skillagers(ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single skillager

        Returns:
            Response -- JSON serialized user instance
        """
        try:
            skillager = Skillager.objects.get(pk=pk)
            serializer = SkillagersSerializer(
                skillager, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to skillagers resource
        Returns:
            Response -- JSON serialized list of skillagers
        """
        skillagers = Skillager.objects.filter(id=request.auth.user.customer.id)
        skillager = self.request.query_params.get('skillager', None)

        if skillager is not None:
            skillagers = skillagers.filter(id=skillager)

        serializer = SkillagerSerializer(
            skillagers, many=True, context={'request': request})

        return Response(serializer.data)
