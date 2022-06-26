# TracTgt-gRPC
A CSC3004 Lab Assessment to create a client-server SafeEntry system using the gRPC protocol

### Running the Program

#### How to build docker image
type the following commands under the working directory with the `dockerfile`

```
docker compose build
```

#### Running the dockerized image
```
docker compose up
```
once the container is running successfully, run the client script within the docker shell to access the menu
```
docker exec -it tracetogether_service bash
python login.py
```

#### Stopping the Docker image
```
docker compose down
```
### Functionalities of the programe

Under the login.py app, you can choose to access a regular `client` or a `MOH client`

#### MOH Client
In this client, you can do the following: (ID:12345)
- [1] Declare COVID-19 visited locations
- [2] Display all details of COVID-19 visited locations
- [3] Remove COVID-19 visited locations

#### Regular Client
In this client, you can do the following:
- [1] Individual Check In
- [2] Individual Check Out
- [3] Group Check In
- [4] Group Check Out
- [5] Retrieve Check In/Out History
- [6] View Covid19 Declared Locations

#### Show case

#### Concurrency showcase


