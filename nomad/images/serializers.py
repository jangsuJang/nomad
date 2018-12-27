from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):
#    image = ImageSerializer()
    class Meta:
        model = models.Comment
        fields = "__all__"
        
class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True)
    like_set = LikeSerializer(many=True)

    class Meta:
        model =  models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes'
        )
#        fields = "__all__"

