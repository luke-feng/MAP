# SHINE
> a collaborative system for sharing information and economic impacts of cyberattacks

## Table of Contents

   * [SHINE](#SHINE)
      * [Introduction](#SHINE)
   * [Front End](#front-end)
      * [miner](#miner)
      * [api](#api)
      * [ddosgrid](#ddosgrid)
   * [Production deployment](#production-deployment)
      * [frontend](#frontend-1)
      * [API](#api-1)

## SHINE

This project consist of two parts:
* The `Front End` is mainly inherited from DDoSGrid project, which used Vue.js as their developing language, and containts three parts, the `miner`, the `api` and the `frontend`.
	* The `miner` subproject is a packet decoder and feature extractor that produces output as JSON files and communicates over stdout or an IPC channel if available.
	* The `api` is a RESTful api based on Express.js which orchestrates the `miner` package if required.
	* The `frontend` is a Vue.js based SPA that renders visualizations obtained from the api.
* The `Back End` is responsible for data processing, data management, and applications communication. Our Back End system is based on Django. There are ...

# Front End

Clone the project from github:
```
git clone git@github.com:luke-feng/MAP.git
```

## miner
Enter the `miner` subproject and install the necessary dependencies. Make sure you are running Node.JS version 10 and that you lave libpcap installed.
```bash
cd miner
npm i
```
After that the miner package can be imported as an NPM module or it can be run manually through the shell. 
For details of this part, please refer to the DDoSGrid project. (https://github.com/ddosgrid/ddosgrid-v2)

## api
Setting up the api is straightforward simply fetch the dependencies and start the main javascript file. Make sure that you have previously installed the dependencies of the miner!
```bash
cd miner; npm i; cd ..;
cd api; npm i
```
Now simply run it and optionally pass the port where it should listen:
```bash
node index.js
```
or
```bash
export PORT=1234; node index.js
```
or by using the scripts(recommended)
```bash
./scripts/start_dev_server.sh
```
It will automaticly listen on `8000` port. And you can change the technical details in `api/scripts/start_dev_server.sh`, like the `port` and `CLIENT_APP_ORIGIN`.


## ddosgrid
Enter the `ddosgird` subproject and run it after fetching its dependencies
```bash
npm i
```
This will automatically rebuild the project if a file changes. 
To use the application you will need to let it connect to an api instance.
To connect it with our `Back End`, you can run the build commend

```bash
npm run build
```
It will packet the frontend project, and connect with Django backend.

# Back End