from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from skillchillapi.models import PostPage


class PostPagesSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializers
    """
    class Meta:
        model = PostPage
        url = serializers.HyperlinkedIdentityField(
            view_name='postpage',
            lookup_field='id'
        )
        fields = ('id', 'post', 'content', 'caption',
                  'page_num', 'created_at', 'modified_at')


class PostPages(ViewSet):
    """Skills in Skillchill"""
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized postinstance
        """
        new_post_page = PostPage()
        new_post_page.post_id = request.data['post_id']
        new_post_page.content = request.data['content']
        new_post_page.caption = request.data['caption']
        new_post_page.page_num = request.data['page_num']
        new_post_page.save()
        serializer = PostPagesSerializer(
            new_post_page,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single post page

        Returns:
            Response -- JSON serialized post instance
        """
        try:
            post_page = PostPage.objects.get(pk=pk)
            serializer = PostPagesSerializer(post_page, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to the post pages resource 
        that grabs all the post pages associated with

        Returns:
            Response -- JSON serialized list of posts
        """
        post_id = self.request.query_params.get('post', None)
        post_pages = PostPage.objects.filter(post__id=post_id)
        serializer = PostPagesSerializer(
            post_pages,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests for an post

        Returns:
            Response -- Empty body with 204 status code
        """
        post_page = PostPage.objects.get(pk=pk)
        post_page.caption = request.data["caption"]
        post_page.modified_at = request.data["modified_at"]
        post_page.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single post

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            post_page = PostPage.objects.get(pk=pk)
            post_page.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except PostPage.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.arg[0]},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
