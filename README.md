# SHINE
> A collaborative system for sharing information and economic impacts of cyberattacks

[![SHINE](https://res.cloudinary.com/marcomontalbano/image/upload/v1620053813/video_to_markdown/images/youtube--xXJiNNBJznY-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=xXJiNNBJznY "SHINE")

## Table of Contents

   * [SHINE](#SHINE)
      * [Introduction](#SHINE)
   * [Front End](#front-end)
      * [miner](#miner)
      * [api](#api)
      * [frontend](#frontend)
   * [Back End](#Back-End)
      * [Installing required third-party packages](#Installing-required-third-party-packages)
      * [Configure the path](#Configure-the-path)
      * [Add IP address to the white list](#Add-IP-address-to-the-white-list)
      * [Start the server](#Start-the-server)
   * [Reference](#Reference)

## SHINE

This project consist of two parts:
* The `Front End` is mainly inherited from DDoSGrid project, which used Vue.js as their developing language, and containts three parts, the `miner`, the `api` and the `frontend`.
	* The `miner` subproject is a packet decoder and feature extractor that produces output as JSON files and communicates over stdout or an IPC channel if available.
	* The `api` is a RESTful api based on Express.js which orchestrates the `miner` package if required.
	* The `frontend` is a Vue.js based SPA that renders visualizations obtained from the api.
* The `Back End` is responsible for data processing, data management, and applications communication. Our Back End system is based on Django.  There are 10 applications functioning in the back-end. 
   * The `application` application is used to process the join in application of interested persons.
   * The `attack_feature` application is used to handle some data extracted from the PCAP files.
   * The `attack_information` application is responsible for process single incidents related data, such as the financial loss caused by the incident and the technical detail about the incident. This application also in charge of providing data for `Incident Statistic` part and `Ecomonic Impact` part of system.  
   * The `city_country` application provides the city and country options for users to choose.
   * The `information_sharing` application manages the options for technical related multiple choices and provide users with those options to choose from.
   * The `measure` application deals with the countermeasures set by users against cyberattacks.
   * The `measure_type` application manages the predefined countermeasures for users to select from.
   * The `organization` application is used to handle organization related data and provide users with options.
   * The `sector` application is used to handle sector related information and provide options as well.
   * The `user_info` application is used to process the user related information.

   And within each application, there are six python files been used to make sure the system functioning as designed.
   
   * `admin.py` is related to the settings of Django admin site.
   * `app.py` is where the application configuration metadata for an application being stored.
   * `model.py` is the place where data models are defined matching with the tables in the database.
   * `serializers.py` is the place to define serializers for data models which are reponsible for data validation and conversion.
   * `urls.py` is where the URLs configurations being set to dispatch requests to appropriate methods for processing.
   * `views.py` is where all the `views` belong to, and each `view` contains concrete implementations of methods to handle requests.

The following shows the outline structure of the SHINE system.
   ```bash
      |—— api 
      |—— application
      |—— attack_features
      |—— attack_information 
      |—— city_country 
      |—— docker-compose.ysl 
      |—— Dockerfile 
      |—— Economic.db 
      |—— frontend 
      |—— information_sharing 
      |—— LICENSE 
      |—— manage.py 
      |—— measure 
      |—— measure_type 
      |—— miner 
      |—— models.py 
      |—— organization 
      |—— README.md 
      |—— sector 
      |—— SHINE 
      |—— user_info 
   ```

The following applications and programs must be installed on the target machine before the installation. 
```bash
      * Node.js
      * npm
      * git
      * Python, Version >= 3.6
      * pip
      * Django 3
      * libpcap
      * SSH Client
```

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
You may need to change  `CLIENT_APP_ORIGIN `, ` OAUTH2_SUCCESS_FORWARD`, `OAUTH2_CALLBACK ` to your own IP and service port in the `api/scripts/start_dev_server.sh` script file.

It will automaticly listen on `8080` port. And you can change the technical details in `api/scripts/start_dev_server.sh`, like the `port` and `CLIENT_APP_ORIGIN`.


## frontend
Enter the `frontend` subproject and run it after fetching its dependencies
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
## Installing required third-party packages
With the `pip` being installed, you can use this command to install packages. Run the following commands to install required third-party packages for the SHINE system.
```bash
pip install djangorestframework
pip install django-filter
pip install django-smart-selects
pip install django-cors-headers
pip install django-unixtimestampfield
pip install geonamescache
```
If you would like to install other packages, please do not forget to add them to the `INSTALLED_APP` list inside the `settings.py` file.

## Configure the path
For this step, you need have your server IP address and the port number that provides service for the DDoSGrid system in hand. Fine the hidden file `.env.production`, open the file and locate yourself to the line that sets `VUE_APP_APIBASEURL` and `VUE_APP_SHINEBASEURL`, and modify it follow the following format.
```bash
VUE_APP_APIBASEURL = http://`your server IP address`:`DDoSGrid service port`
VUE_APP_SHINEBASEURL = http://`your server IP address`:`BackEnd service port`
```

## Add IP address to the white list
Before you can start run the service, you need to add the server IP address to the trusted white list. To do so, you need go find the file `settings.py` under the SHINE folder. Open the file and find the place where the `ALLOWED_HOSTS` and `CORS_ORIGIN_WHITELIST`, and append your server IP address to the end of the list.

## Start the server
To start the server, run the following command within the folder that stores the `manage.py` file.
```bash
python manage.py runsever
```
And the terminal will tell you the which port is currently carrying the service.

# Reference
* Chao Feng, Qiaowen Wang, Xianxiao Xu: SHINE: a Collaborative System for Sharing Insights and Information of Economic Impacts of Cyberattacks; Universität Zürich, Communication Systems Group, Department of Informatics, Zürich, Switzerland, May 2021, URL: https://files.ifi.uzh.ch/CSG/staff/franco/extern/theses/MAP-SHINE.pdf.
