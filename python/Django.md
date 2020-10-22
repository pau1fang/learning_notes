# 日志记录

### 1. 使用默认日志记录

配置LOGGING

### 2. 自定义日志记录

```python
from my_blog.settings import LOGGING
import logging

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('django.request')

def whatever(request):
	logger.warning('Something wrong!')
```



# 第三方登录

### 使用第三方库django-allauth

`安装 pip install django-allauth`
修改配置文件

添加url路径 `urlpatterns=[path('accounts/', include('allauth.urls')),]`

迁移数据库

申请相应的平台第三方登录GitHub OAuth应用地址为 `https://github.com/settings/applications/new`

### 