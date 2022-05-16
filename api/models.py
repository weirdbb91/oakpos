from django.db import models

# Create your models here.

exclude_model_name = ["TimestampedModel"]


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 시각")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 시각")
    
    class Meta:
        abstract = True


class Member(TimestampedModel):
    name = models.CharField(null=False, max_length=255, verbose_name="이름")
    is_guest = models.BooleanField(null=False, default=True, verbose_name="손님 여부")
    
    class Meta:
        ordering = ["is_guest", "id"]
        verbose_name = "멤버"
        verbose_name_plural = "멤버 리스트"
    
    def __str__(self):
        return self.name
