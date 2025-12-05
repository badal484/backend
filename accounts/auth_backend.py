from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserDocument
from rest_framework import exceptions

class MongoJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):
        """
        Overrides JWTAuthentication to fetch user from MongoDB
        """
        try:
            user_id = validated_token.get("user_id")
            user = UserDocument.objects(id=user_id).first()
            if user is None:
                raise exceptions.AuthenticationFailed("User not found")
            return user
        except Exception:
            raise exceptions.AuthenticationFailed("Invalid token")
