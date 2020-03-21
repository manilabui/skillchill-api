from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from skillchillapi.models import Post
from .skill import SkillsSerializer

# TODO: need to show the moderator + all members
class PostsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializers
    """
    skill = SkillsSerializer()
    post_type = serializers.CharField(source='get_post_type_display')

    class Meta:
        model = Post
        url = serializers.HyperlinkedIdentityField(
            view_name='post',
            lookup_field='id'
        )
        fields = ('id', 'skill', 'post_type', 'is_public',
                  'created_at', 'modified_at')
        depth = 2

    def get_post_type(self, obj):
        return obj.get_post_type_display()


class Posts(ViewSet):
    """Skills in Skillchill"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized postinstance
        """
        new_post = Post()
        new_post.skillager_id = request.auth.user.skillager.id
        new_post.skill_id = request.data['skill_id']
        new_post.post_type = request.data['post_type']
        new_post.is_public = request.data['is_public']
        new_post.save()

        serializer = PostsSerializer(
            new_post,
            context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post instance
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostsSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to posts resource

        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all()
        skillager_id = request.auth.user.skillager.id

        # filter by posts of the logged in user
        skillager = self.request.query_params.get('skillager', False)
        if skillager == 'true':
            posts = posts.filter(skillager__id=skillager_id)

        # filter by skill
        skill = self.request.query_params.get('skill', False)
        if skill == 'true':
            posts = posts.filter(skill__id=skill_id)

        serializer = PostsSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests for an post

        Returns:
            Response -- Empty body with 204 status code
        """
        post = Post.objects.get(pk=pk)
        post.is_public = request.data["is_public"]
        post.modified_at = request.data["modified_at"]
        post.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single post

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.arg[0]},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
