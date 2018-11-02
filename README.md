# python-keyserver

This keyserver is built in Python leveraging Flask module to manage cryptographic keys. Keys are mapped to their unique identifiers and are stored in MySQL database.

There are four endpoint for working with this Keyserver. These endpoint require basic authentication i.e. username and password

1. Register new key:

   curl -s "Keyserver_URL:5000/register?$uid&$cryptokey"
   
2. Retriving the key:

   curl -s "Keyserver_URL:5000/getkey/$uid"
   
3. Updating the key:
  
    curl -s "Keyserver_URL:5000/updatekey?$uid&$cryptokey"
    
4. Show all keys (admin use):

    curl -s "Keyserver_URL:5000/showallkeys
    
    
# Get the docker image from Docker hub

This keyserver is packaged in the docker image with all the dependecies installed and available at DockerHub

docker pull lals1/keyserver:latest
  
# Running the keyserver

Prerequisite: latest docker and docker-compose installed.

Clone the repo or simply download the docker-compose.yml and run command:

 docker-compose up -d
 
The keyserver will be up and it will listen on port 5000 so it should be open.
    
# Turn off the keyserver

Simply run:

docker-compose down
