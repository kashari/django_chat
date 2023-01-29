# django_chat
Channels and Redis based chat application using Django Rest Framework.

## install redis using docker
After installing docker engine use the two following commands to set up a docker container with redis in port **6379**
1. `docker pull redis`
2. `docker run --name=django_chat -p 6379:6379/tcp --restart=always -d redis`

# run the project
 1. run pip `install -r requirements.txt`
 2. comment out these lines in `chat/models.py`

    ```
    import django
    
    django.setup()
    ```
    commenting these will allow you to use the default settings and use the `migrate` command
 3. run `python manage.py migrate`
 4. undo step 2
 5. to start the ASGI server run `daphne ChatAPI.asgi:application --port 8001`

### That is all required to have the async chat server up and running to connect via websockets 

First hit this endpoint to start a conversation: `http://localhost:8001/chat/start/`

*It requires the username of the user you are chatting as follows: *

```
    {
        "username": "username"
    } 
```

Via URL: `ws://localhost:8001/ws/chat/{id}/`.


The required payload for this is a json format as follows: 
```
    {
        "message": "Text message goes here."
    } 
```
Additionally, the message accepts even attachment, see the code in chat/moddels.py for more.

To view all of the users notifications hit this endpoint after authentication: `http://localhost:8001/notifications/list_notifications`


*The returned payload is a list as follows: *

```
[
    {
        "to": {
            "id": id,
            "email": "mail@domain.com",
            "username": "username",
            "bio": "Something meaningful..."
        },
        "message": "Hello username. Your account was saved successfully.",
        "opened": false,
        "since": "2 h"
    }
]
```

