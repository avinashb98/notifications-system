## Notifications Service

### Requirements
- The system allows firing notifications to a particular user from anywhere in the codebase.
- The notifications contain a title, description, and an optional identifier to categorize them.
- The system will store the notifications in mongodb for future retrieval.
- Additionally, the system should has a WebSocket endpoint where the user can receive real-time notifications.
- The system will also have a feature to mark notifications as read.

## Expected Behaviour and Use cases
- When a user receives a message from another user, the system
fires a notification with the title "New Message Received" and
the message's content as the description. The notification should
have an identifier `MESSAGE` to categorize it. 
- When a user is close to the end of their subscription period, the
system should fire a notification with the title "Subscription Expiring
Soon" and the description containing the expiration date. The
notification should have an identifier `SUBSCRIPTION_EXPIRY` to
categorize it.
- When a user completes their profile setup, the system should fire a
notification with the title `Profile Setup Complete` and a description
congratulating the user. The notification should have an identifier
`PROFILE_SETUP` to categorize it.
- The functionality for generating events that trigger notifications, such as sending messages or completing user profiles, is mocked and not implemented in this project.

### Installation
#### Prerequisites
1. `docker`
2. `docker-compose`

#### Installation Steps
1. `git clone https://github.com/avinashb98/notifications-system`
2. `cd notifications-system`
3. `docker-compose build`
4. `docker-compose -f docker-compose.yml up`

### Testing
#### REST API
Head over to [swagger api docs](http://localhost:8000/docs). The same doc can be used to interact with the implemented rest apis.

#### Websocket
A websocket client like [Postman](https://www.postman.com/) is required to interact with the websocket server of the app.
1. connect to the endpoint `localhost:8000/ws/v1/notifications/{user_id}`.
2. Pick one user out of the seed user ids (alex, bob, carol, dan) inorder to receive real-time notifications, e.g. `localhost:8000/ws/v1/notifications/alex`.

### Folder Structure and Details
```text
/api
    /routers
        notification.py             # notifications router

/config
    vars.py                         # app variables and settings

/database
    mongo.py                        # connects to mongodb

/entities
    enums.py                        # notification property enums
    notification.py                 # notification types, dto

/repositories
    /notification
        /base
            repository.py           # interface for crud over a datasource
    
        mongo_repository.py         # mongodb implementation of interface

/services
    /notification
        /base
            service.py              # interface for notification service over a repository
        v1.py                       # implementation of notification service
    
    /notifier
        notifier.py                 # sends notification to a user over websocket
    
    /ws
        manager.py                  # maintains users' websocket connections in the app

/simulator
    seed.py                         # generates random notifications from a fixed dataset
```

