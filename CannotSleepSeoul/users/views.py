import jwt, requests
from datetime     import datetime, timedelta

from django.views import View
from django.http  import JsonResponse

from users.models import User
from CannotSleepSeoul.settings import SECRET_KEY, ALGORITHM

class KakaoSignIn(View):
    def post(self, request):
        try:
            access_token     = request.headers.get('Authorization')
            kakao_user_api   = 'https://kapi.kakao.com/v2/user/me'
            headers          = {'Authorization':f'Bearer ${access_token}'}
            response         = requests.get(kakao_user_api,headers=headers, timeout=5)
            user_information = response.json()
            kakao_id         = user_information['id']
            nickname         = user_information['properties']['nickname']
            profile_image    = user_information['properties']['profile_image']
            
            if not User.objects.filter(kakao_id=kakao_id).exists():
                user = User.objects.create(
                    kakao_id          = kakao_id,
                    name              = nickname,
                    profile_image_url = profile_image
                )
            else:
                user = User.objects.get(kakao_id=kakao_id)

            access_token = jwt.encode({'id': user.id, 'exp':datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'access_token' : access_token, "name" : nickname, "profile_image" : profile_image})
        except KeyError:
            return JsonResponse({'message':'keyerror'},status=400)
        except requests.exceptions.Timeout:
            return JsonResponse({'message':'timeout error'},status=408)

