# django_chat
Channels and Redis based chat application using Django Rest Framework.

## install redis using docker
After installing docker engine use the two following commands to set up a docker container with redis in port **6379**
1. `docker pull redis`
2. `docker run --name=django_chat -p 6379:6379/tcp --restart=always -d redis`

# run the project
 1. run pip `install -r requirements.txt`
 2. to start the ASGI server run `daphne ChatAPI.asgi:application --port 8001`

### That is all required to have the async chat server up and running to connect via websockets [ws://localhost:8001/ws/chat/1/](ws://localhost:8001/ws/chat/1/)
The required payload for this is a json format as follows: 
```
    {
        "message": "Text message goes here."
    } 
```
Additionally, the message accepts even attachment, see the code in chat/moddels.py for more.
