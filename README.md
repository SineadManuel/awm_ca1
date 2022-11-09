# AWM CA 1

Name: Sinead Manuel

Student Number: C19336081

### Aim of Project
The objective of this assignment was to create, build and deploy a location-based web application to a cloud-facing server in a secure manner.

To complete this assignment, I used Django to create a web application and docker to depoly the images to the cloud.

### Location Based Services App

This application consists of 4 pages: Home, Register, Login and Map

#### Home
There are two different versions of the home page. If the user is visting the web app for the first time, they will be prompted to login. Otherwise, if the user logs in with their credentials, the home page will display a welcome message with their username. They will also have the option to view the map.

#### Login & Register
For the login and register pages, I used Django's built in authentication service. This gave me a premade form which had all the necessary error checking.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/71662080/200960047-6c36cb1f-13b4-4479-be98-c9afebd7d49c.png">

<img width="960" alt="image" src="https://user-images.githubusercontent.com/71662080/200957346-7a188ea3-27aa-4b05-a259-0c7d82a0bfa4.png">

#### Map
The map page displays a world map. Once the user allows for their location to be used, the map zooms into the area that the user is located and displays a marker to show the exact point location of the user. Unfortunately, I was unable to create a popup which would show the user's latitude and longitude. I was also unable to update the database with the user's location.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/71662080/200956043-b52890c5-d32f-4208-98e9-e72832d11e71.png">

### Deployment
Unfortunately I was unable to deploy my web application to http://sineadmanuel.online/

I have managed to create a Digital Ocean droplet and retrieve a domain name for my web application.
<img width="764" alt="image" src="https://user-images.githubusercontent.com/71662080/200961790-b6fe4115-15ff-4ee5-b695-5b4b93fe8bac.png">

I also unfortunately could not get NGINX to run and I was unable to push any images or containers to Docker Hub.
