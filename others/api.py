from .serializers import PostRequestSerializer, FeedbackSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from .util import get_client_ip
from rest_framework.response import Response

class PostRequestAPIView(generics.CreateAPIView):
    serializer_class = PostRequestSerializer
    permission_classes = [ AllowAny, ]

    def post(self, request, *args, **kwargs):
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': secret_key,
            'response': request.data['responseG'],
            'remoteip': get_client_ip(self.request),
        }
        )

    if r.json()['success']:
        return self.create(request, *args, **kwargs)
        return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)



class FeedbackAPIView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [ AllowAny, ]