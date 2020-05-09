from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['isAerobicallyDeficient'] = user.profile.isAerobicallyDeficient
        token['hrResting'] = user.profile.hrResting
        token['hrMax'] = user.profile.hrMax
        token['hrAerobicThreshold'] = user.profile.hrAerobicThreshold
        token['hrLactateThreshold'] = user.profile.hrLactateThreshold
        # ...

        return token


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['isAerobicallyDeficient'] = user.profile.isAerobicallyDeficient
        token['hrResting'] = user.profile.hrResting
        token['hrMax'] = user.profile.hrMax
        token['hrAerobicThreshold'] = user.profile.hrAerobicThreshold
        token['hrLactateThreshold'] = user.profile.hrLactateThreshold
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
