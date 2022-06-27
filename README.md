# TracTgt-gRPC
A CSC3004 Lab Assessment to create a client-server SafeEntry system using the gRPC protocol

## Running the Program

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

## MOH Client Showcase
![image](https://user-images.githubusercontent.com/73775846/175868097-80c94542-3869-435a-94b6-e4e22f9557d0.png)

## Client Showcase
![Screenshot 2022-06-27 025921](https://user-images.githubusercontent.com/73775846/175830119-848beb67-a521-4c18-92ee-47a5d031fb70.png)

## Concurrency Showcase
![Screenshot 2022-06-27 030231](https://user-images.githubusercontent.com/73775846/175830128-cc744c52-10f8-4127-9b8c-cb1bec9e3f07.png)

## Testing Scenarios
|S/n   	|Has the location been declared as a Covid-19 location?    	|Has the user visited the declared Covid-19 location before and is within the 14 days (inclusive)?   	|User to receive notification?|
|---	|---	|---	|---	|
|1   	|No  	|No  	|No   	|
|2   	|Yes   	|No   	|No   	| 
|3   	|Yes   	|Yes   	|Yes   	|

Below are the procedure and test cases for the testing of the decision table (Scenario 1 and 3). For groups wise, any acceptable NRIC could be used for evaluation.
Objective: 
- To perform the first check-in and check-out of a location.
- Subsequently declaring the location as Covid-19 visited location.
- Receiving notification. 

| S/N 	|                                   Procedures                                   	| Test Case Description                                                                     	| Expected result                                                                                                	| Actual Result                                                                                                  	|
|-----	|:------------------------------------------------------------------------------:	|-------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------------	|
| 1   	| Select 2 when prompted, are you a MOH Officer.                                 	| Enter NRIC: **_S1111111A_**                                                               	| No notification. Display user menu                                                                             	| No notification. Display user menu                                                                             	|
| 2   	| Perform an individual check-in.                                                	| Enter Name: **_Andy_** Enter Location:**_SIT_**                                           	| Check-in success message shown                                                                                 	| Check-in success message shown                                                                                 	|
| 3   	| (Optional) Perform an individual check-out.                                    	| -                                                                                         	| Check-out success message shown                                                                                	| Check-out success message shown                                                                                	|
| 4   	| Select 0 to exit the user menu  Select 1 when prompted, are you a MOH Officer? 	| Enter MOH ID: **_12345_**                                                                 	| Display MOH Officer menu                                                                                       	| Display MOH Officer menu                                                                                       	|
| 5   	| Perform a declaration of COVID-19 visited location.                            	| Enter Location: **_SIT_** Enter Date: "**_Today Date_**" Enter Time: "**_present time_**" 	| Location declared as COVID-19 visited successful                                                               	| Location declared as COVID-19 visited successful                                                               	|
| 6   	| Return to user menu                                                            	| Enter NRIC: **_S1111111A_**                                                               	| Notification on potential exposure with the affected location, check-in and check-out time. Displays user menu 	| Notification on potential exposure with the affected location, check-in and check-out time. Displays user menu 	|

For the testing of Scenario 2, existing NRIC of ‘S9618780G’ could be used. Figure 4 displays all the SafeEntry records that the user had performed. Whereas for Figure 5 it displays all the locations with the number of days it had been declared as Covid-19 visited location. Notice that even though the user had checked-in to the location of ‘ÁMK HUB’, however, the checked-in date does not fall within the 14 days and hence, the notification does not state potential exposure at the location ‘ÁMK HUB’. If not for the matching of other potential Covid-19 exposure locations, the user would not had received any notification. 

![Screenshot 2022-06-27 215557](https://user-images.githubusercontent.com/73775846/175958874-a104d83f-2158-4eea-b722-32b3470de8e9.png)

![Screenshot 2022-06-27 215608](https://user-images.githubusercontent.com/73775846/175958929-d1aa8b1f-e19d-4e5e-b6fa-2556335e76fc.png)
