# Nginx docker hello world example
This repo demonstrates how to use nginx as a revert proxy for deploying apps with docker-compose.

## The apps
Four instances of a simple python app are deployed. The apps read out environment variables providing their own name and the address of the other instance to connect to. On port 80 both apps return their names and try to obtain the name from the other instance by calling der /name API GET method.

## Setup
You only need docker-compose on your machine. Then, call docker-compose up -d and wait until the images are build/downloaded. You can now call the apps in your browser via localhost/app1, localhost/app2, localhost/app3 or localhost/app4.
