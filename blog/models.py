from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #models.을 넣으므로써 Post 클래스가 장고 모델임을 의미. -> Post가 데이터베이스에 저장되어야 한다고 알게 된다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자수가 제한된 텍스트 정의할 때 사용
    text = models.TextField() # 글자수에 제한이 없는 긴 텍스트를 위한 속성 
    created_date = models.DateTimeField( # 날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # 원한다면 이름 변경 가능.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title