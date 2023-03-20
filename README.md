# RestaurantOne
Restaurant management application developed using Flask, react and Postgresql

## status
[![CodeQL](https://github.com/michaelgobz/RestaurantOne/actions/workflows/codeql.yml/badge.svg)](https://github.com/michaelgobz/RestaurantOne/actions/workflows/codeql.yml)[![Pylint](https://github.com/michaelgobz/RestaurantOne/actions/workflows/pylint.yml/badge.svg)](https://github.com/michaelgobz/RestaurantOne/actions/workflows/pylint.yml)[![.github/workflows/DeployToAzure.yml](https://github.com/michaelgobz/RestaurantOne/actions/workflows/DeployToAzure.yml/badge.svg)](https://github.com/michaelgobz/RestaurantOne/actions/workflows/DeployToAzure.yml)[![Deploy the Flask Api](https://github.com/michaelgobz/RestaurantOne/actions/workflows/azure-webapps-python.yml/badge.svg)](https://github.com/michaelgobz/RestaurantOne/actions/workflows/azure-webapps-python.yml)



## Installation
The project uses a monorepo structure where the ui and the backend are hosted on the same repository.<br />
For starters, there are 2 directories to watch out for the root that houses the backend and ```ui``` directory that house the ui components that are built on [react](https://reactjs.org). <br />
The ui needs ```nodejs v18``` to build the react components and use the ```@material-ui``` ui took kit<br />

This backend uses python 3.9.12 as the runtime on the [flask](https://flask.palletsprojects.com/en/2.2.x/) web framework and [postgresql](https://www.postgresql.org/docs/) database. we start with cloning off github

**server setup**

```bash
git clone https://github.com/michaelgobz/RestaurantOne
```
Then ```cd``` into the RestaurantOne folder and create virtual environment to setup the server dependencies

```bash
cd RestaurantOne
py -3 -m venv venv
venv\Scripts\activate
```
Then the with ```RestaurantOne``` as your working directory 
install the dependencies using pip or using poetry<br />
**NOTE:** with poetry make sure the python version is 3.9.12

```bash
pip install -r requirements.txt
```
or

```bash
poetry install
```

**UI** **Setup** <br />

To setup the ui you will need to ```cd``` into ```client``` directory then run <br />
```bash
npm install
```
or using yarn 

```bash
yarn install
```
to install the required dependencies, when its done then you can run <br />

```bash
npm run start server
npm run migrate 
npm run populateDb
npm build 
npm start
```
which will start the api server, migrate the database, populate it build and start client then you can interact with the ui via the loopback host <br />

**Documentations**

**Architecture**

**Authors**<br />
[Michael Goboola](https://github.com/michaelgobz/)<br />
[Jed Bahena](https://github.com/Jed-hub)
