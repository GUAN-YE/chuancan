# coding: utf-8
import re
import os
import logging
import simplejson as json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 读取数据库配置文件
config_file = os.path.join(BASE_DIR, '.env')
with open(config_file) as f:
    config = f.read()
    DATABASES_CONFIG = json.loads(config)

DEBUG = True if DATABASES_CONFIG["DEBUG"] == 'True' else False
ALLOWED_HOSTS = ["*"]

DB_ENGINE = 'django.db.backends.mysql'
DB_WAIT_TIMEOUT = 29  # 单个连接最长维持时间
DB_POOL_SIZE = 8  # 连接池最大连接数

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_com',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],  # Set to empty string for default. Not used with sqlite3.
    },
    'slave': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_com',
        'USER': DATABASES_CONFIG['DB_USER_USER'],  # Not used with sqlite3.
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],  # Not used with sqlite3.
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],
    },
    'user': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_user',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],  # Set to empty string for default. Not used with sqlite3.
    },
    'user_slave': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_user',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],  # Set to empty string for default. Not used with sqlite3.
    },
    'ketang': {
        'NAME': 'tbkt_ketang',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],
    },
    'ketang_slave': {
        'NAME': 'tbkt_ketang',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],
    },
    'ziyuan': {
        'NAME': 'ziyuan_new',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_ZIYUAN_USER'],  # Not used with sqlite3.
        'PASSWORD': DATABASES_CONFIG['DB_ZIYUAN_PASSWORD'],  # Not used with sqlite3.
        'HOST': DATABASES_CONFIG['DB_ZIYUAN_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_ZIYUAN_MASTER_PORT'],
    },
    'ziyuan_slave': {
        'NAME': 'ziyuan_new',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_ZIYUAN_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_ZIYUAN_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_ZIYUAN_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_ZIYUAN_SLAVE_PORT'],
    },
    'shuxue': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_shuxue',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],
    },
    'shuxue_slave': {
        'NAME': 'tbkt_shuxue',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],
    },
    'yy': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_yingyu',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],
    },
    'yy_slave': {
        'NAME': 'tbkt_yingyu',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],
    },
    'yuwen': {
        'ENGINE': DB_ENGINE,
        'NAME': 'tbkt_yuwen',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_MASTER_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_MASTER_PORT'],
    },
    'yuwen_slave': {
        'NAME': 'tbkt_yuwen',
        'ENGINE': DB_ENGINE,
        'USER': DATABASES_CONFIG['DB_USER_USER'],
        'PASSWORD': DATABASES_CONFIG['DB_USER_PASSWORD'],
        'HOST': DATABASES_CONFIG['DB_USER_SLAVE_HOST'],
        'PORT': DATABASES_CONFIG['DB_USER_SLAVE_PORT'],
    },
}

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Etc/GMT-8'
USE_I18N = True
USE_L10N = True

APIDOC_DIR = os.path.join(BASE_DIR, 'apidoc/')
#
# # 文件上传密钥
# FILE_UPLOAD_SECRET = DATABASES_CONFIG['FILE_UPLOAD_KEY']
# # 文件上传服务器(只保留两天以内的文件)
# FILE_UPLOAD_URLROOT = DATABASES_CONFIG['FILE_UPLOAD_URLROOT']
# # 永久文件服务器(两天以后同步到CDN)
# FILE_URLROOT = DATABASES_CONFIG['FILE_URLROOT']

# 文件上传密钥
FILE_UPLOAD_SECRET = DATABASES_CONFIG['FILE_UPLOAD_KEY']

# # 文件上传服务器(只保留两天以内的文件)
FILE_UPLOAD_URLROOT = DATABASES_CONFIG['FILE_UPLOAD_URLROOT']

# 两天内的文件服务器地址
FILE_VIEW_URLROOT = DATABASES_CONFIG['FILE_VIEW_URLROOT']

# 两天以后文件服务器的地址:
FILE_VIEW2_URLROOT = DATABASES_CONFIG['FILE_VIEW2_URLROOT']

# 本站地址
URLROOT = DATABASES_CONFIG['DOMAIN_API_COM_API_DJ_URLROOT']
# 接口URLROOT字典
API_URLROOT = {}
for k, v in DATABASES_CONFIG.iteritems():
    m = re.match(r'DOMAIN_API_(\w+)_API_DJ_URLROOT', k)
    if m:
        alias = m.groups()[0].lower()
        API_URLROOT[alias] = v

    m = re.match(r'DOMAIN_GO_(\w+)_URLROOT', k)
    if m:
        alias = m.groups()[0].lower()
        API_URLROOT[alias] = v

# go 接口域名
GO_URLROOT = {}
for k, v in DATABASES_CONFIG.iteritems():
    m = re.match(r'DOMAIN_GO_(\w+)_URLROOT', k)
    if m:
        alias = m.groups()[0].lower()
        GO_URLROOT[alias] = v

# vue 域名
VUE_URLROOT = {}
for k, v in DATABASES_CONFIG.iteritems():
    m = re.match(r'DOMAIN_VUE_(\w+)_URLROOT', k)
    if m:
        alias = m.groups()[0].lower()
        VUE_URLROOT[alias] = v

# web 域名
WEB_URLROOT = {}
for k, v in DATABASES_CONFIG.iteritems():
    m = re.match(r'DOMAIN_WEB_(\w+)_WEB_DJ_URLROOT', k)
    if m:
        alias = m.groups()[0].lower()
        WEB_URLROOT[alias] = v

TBKT_HOST = DATABASES_CONFIG["TBKT_COM_INNER_HOST"]

# MEDIA_URLROOT = DATABASES_CONFIG["FILE_URLROOT"]

FILE_TBKT_SCHOOL_MEDIA_URLROOT = DATABASES_CONFIG["FILE_MEDIA_URLROOT"]

FILE_MEDIA_URLROOT = DATABASES_CONFIG["FILE_MEDIA_URLROOT"]

# 同步课堂自制cookie
SESSION_COOKIE_NAME = 'tbkt_token'
SECRET_KEY = '240897'
SESSION_COOKIE_AGE = int(DATABASES_CONFIG["TBKT_COM_SESSION_COOKIE_AGE"])
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_DOMAIN = None

MIDDLEWARE_CLASSES = (
    'tbkt.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
)

ROOT_URLCONF = 'tbkt.urls'

REDIS_HOST = DATABASES_CONFIG['REDIS_HOST']
REDIS_PORT = DATABASES_CONFIG['REDIS_PORT']
REDIS_PASSWORD = DATABASES_CONFIG['REDIS_PASSWORD']
REDIS_DB = DATABASES_CONFIG['REDIS_DB']

# 缓存配置(公共接口不要禁用缓存)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ["%s:%s" % (DATABASES_CONFIG['CACHE_MEM_HOST'], DATABASES_CONFIG['CACHE_MEM_PORT'])],
    }
}

# 公共缓存key统一管理
CACHE_KEYS = {}
for k, v in DATABASES_CONFIG.items():
    if k.startswith('CACHE_KEY_COM_'):
        # print k
        try:
            alias = k[14:].lower()
            rows = v.split('|')
            realkey = rows[0]
            timeout = int(rows[1])
            CACHE_KEYS[alias] = {'realkey': realkey, 'timeout': timeout}
        except:
            pass
# print CACHE_KEYS


# 默认使用哪种密码哈希算法
PASSWORD_ALGORITHM = 'sha1'  # pbkdf2

# 日志写到标准输出
logging.basicConfig(level=logging.WARNING,
                    format='APP: %(asctime)s %(name)s %(levelname)s %(filename)s[line:%(lineno)d func:%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')
