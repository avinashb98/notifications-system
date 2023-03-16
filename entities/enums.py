from enum import Enum


class NotificationReadStatus(Enum):
    UNREAD = 'unread'
    READ = 'read'


class NotificationIdentifier(Enum):
    MESSAGE = 'MESSAGE'
    SUBSCRIPTION_EXPIRY = 'SUBSCRIPTION_EXPIRY'
    PROFILE_SETUP = 'PROFILE_SETUP'
