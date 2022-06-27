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

## Client Showcase
![Screenshot 2022-06-27 025921](https://user-images.githubusercontent.com/73775846/175830119-848beb67-a521-4c18-92ee-47a5d031fb70.png)

## MOH Client Showcase
![image](https://user-images.githubusercontent.com/73775846/175868097-80c94542-3869-435a-94b6-e4e22f9557d0.png)

## Concurrency Showcase
![Screenshot 2022-06-27 030231](https://user-images.githubusercontent.com/73775846/175830128-cc744c52-10f8-4127-9b8c-cb1bec9e3f07.png)

