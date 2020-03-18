from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from skillchillapi.models import Comment


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for comments

    Arguments:
        serializers
    """
    class Meta:
        model = Comment
        url = serializers.HyperlinkedIdentityField(
            view_name='postpage',
            lookup_field='id'
        )
        fields = ('id', 'skillager', 'post', 'content',
                  'created_at', 'modified_at')


class Comments(ViewSet):
    """Skills in Skillchill"""
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized comment instance
        """
        new_comment = Comment()
        new_comment.skillager_id = request.auth.user.skillager.id
        new_comment.post_id = request.data['post_id']
        new_comment.content = request.data['content']
        new_comment.save()
        serializer = CommentsSerializer(
            new_comment,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment page

        Returns:
            Response -- JSON serialized comment instance
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentsSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to the comment pages resource 
        that grabs all the comment pages associated with

        Returns:
            Response -- JSON serialized list of comments
        """
        post_id = self.request.query_params.get('post', None)
        comments = Comment.objects.filter(post__id=post_id)
        serializer = CommentsSerializer(
            comments,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests for an comment

        Returns:
            Response -- Empty body with 204 status code
        """
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        comment.modified_at = request.data["modified_at"]
        comment.save()
        serializer = CommentsSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single comment

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.arg[0]},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
