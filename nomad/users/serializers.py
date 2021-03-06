from rest_framework import serializers
from . import models
from nomad.images import serializers as image_serializers



class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )

class UserProfileSerializer(serializers.ModelSerializer):

    images = image_serializers.CountImageSerializer(many=True,read_only=True)

    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            # 본인이 생성한 이미지를 가져옴 related_name
            # 그냥 images의 아이디만 가져오므로 디테일한 내용을 보기위해서 시리얼라이저를 생성해야함.
            'images',
        )

