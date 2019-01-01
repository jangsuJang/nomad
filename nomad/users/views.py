# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers,models

class ExplorerUsers(APIView):

    def get(self, request,format=None):
        #최근 가입한 유저 5명을 불러오기

        #최근 순으로 정렬하기 위하여 order_by('-date_joined')를 사용 마이너스 필수!!
        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
class FollowUser(APIView):
    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.add(user_to_follow)
        user.save()
        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):
    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.remove(user_to_follow)
        user.save()
        return Response(status=status.HTTP_200_OK)

class UserProfile(APIView):
    def get(self, request, username, format=None):
        try:
            found_user = models.User.objects.get(username = username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.UserProfileSerializer(found_user)
        return Response(data = serializer.data,status=status.HTTP_200_OK)

    pass

class UserFollowers(APIView):
    def get(self, request, username, format=None):
        try:
            found_user = models.User.objects.get(username = request.user)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(user_followers,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)






# User = get_user_model()


# class UserDetailView(LoginRequiredMixin, DetailView):

#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"


# user_detail_view = UserDetailView.as_view()


# class UserListView(LoginRequiredMixin, ListView):

#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"


# user_list_view = UserListView.as_view()


# class UserUpdateView(LoginRequiredMixin, UpdateView):

#     model = User
#     fields = ["name"]

#     def get_success_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})

#     def get_object(self):
#         return User.objects.get(username=self.request.user.username)


# user_update_view = UserUpdateView.as_view()


# class UserRedirectView(LoginRequiredMixin, RedirectView):

#     permanent = False

#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})


# user_redirect_view = UserRedirectView.as_view()
