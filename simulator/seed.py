import random

from entities import NotificationIdentifier, NotificationWrite

users = [
    'alex',
    'bob',
    'carol',
    'dan',
]

message_content = [
    "how's it hanging?",
    "good evening",
    "good morning",
    "what's happening?",
    "greetings",
    "what's the haps?",
    "what's up?",
    "sup",
    "what's happening?",
    "what's the haps?"
]

notification_types = [
    NotificationIdentifier.MESSAGE,
    NotificationIdentifier.PROFILE_SETUP,
    NotificationIdentifier.SUBSCRIPTION_EXPIRY
]

new_message_title = 'New Message Received'
subscription_expiry_title = 'Subscription Expiring Soon'
profile_complete_title = 'Profile Setup Complete'
profile_complete_description = 'Congratulations on completing your profile setup!'


def get_random_notification() -> NotificationWrite:
    n_type = random.choice(notification_types)
    if n_type == NotificationIdentifier.MESSAGE:
        title = new_message_title
        description = random.choice(message_content)
    if n_type == NotificationIdentifier.PROFILE_SETUP:
        title = profile_complete_title
        description = profile_complete_description
    if n_type == NotificationIdentifier.SUBSCRIPTION_EXPIRY:
        title = subscription_expiry_title
        random_days = random.choice(range(1, 30))
        description = f'You subscription ends in {random_days} days'
    receiver_user_id = random.choice(users)
    return NotificationWrite(title=title, description=description, receiver_user_id=receiver_user_id, identifier=n_type)
