# rabbitmq-docker


**Running a Project from the command line only** 
`This is Working 100%` if the `docker-compose.yaml` file is not working you can use this command to run a project
Note: no need to create the docker compose file
```
docker run -d --hostname rebbitmq --name rebbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Default Username : `guest`
Default Password : `guest`

Go To --> `http://localhost:15672`
