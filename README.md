# rabbitmq-docker


**Running a Project from the command line only** 
Note: no need to create the docker compose file
```
docker run -d --hostname rebbitmq --name rebbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Default Username : `guest`
Default Password : `guest`