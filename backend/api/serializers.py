# from django.contrib.auth.models import User
# from rest_framework import serializers
# from .models import Note
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=["id","username","password"]
#         extra_kwargs={"password": {"write_only":True}}
#     def create(self,validated_data):
#         user =User.objects.create_user(**validated_data)
#         return user
    
# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Note
#         fields=["id","title","content","created_at","author"]
#         extra_kwargs={"author":{"read_only":True}}


from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

    def create(self, validated_data):
        # Automatically set the author from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)
