import re

from . import models

#  models에서 type의 인스턴스이고, Model을 상속 받았으면서 제외 대상이 아닌 모델 이름 목록
model_names = [n for n, o in models.__dict__.items() if isinstance(o, type) \
    and issubclass(o, models.models.Model) and n not in models.exclude_model_name]

camel_to_snake = lambda s: re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
