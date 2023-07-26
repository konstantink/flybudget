# coding=UTF-8


from datetime import timedelta


__author__ = 'Konstantin Kolesnikov'


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'KEY_PREFIX': 'dev',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTIONS_POOL_KWARGS': {'max_connections': 100},
            'SERIALIZER': 'django_redis.serializers.json.JSONSerializer'
        }
    },
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=5),
}
