# CarbonShare
Introducing CarbonShare – the app that helps you save on commuting but also rewards you for reducing your carbon footprint! Powered by onTime Carpool, CarbonShare is an innovative way to commute that benefits everyone. By using onTime Carpool and earning CST rewards, you not only reduce your carbon footprint but also become part of a community that cares about the environment. Companies can also join the cause by purchasing CST and offsetting their carbon footprint. With CarbonShare, reducing your carbon footprint has never been easier or more rewarding.


# Mobile Ware Carbon Sharing Add-on Feature
This application is an add-on feature for Mobile Ware, a carpool application. The purpose of this feature is to allow users to leave a trace on the system after completing a carpool ride. The trace is stored in a MongoDB database and triggers a Block Chain micro-server to update and issue an ERC20 token to represent Carbon Sharing.

# Code Structure
The application is built using the following technologies:

## Frontend: Angular 15
Backend: Flask (Python 2.7)
Database: MongoDB
ERC20 for registering the CarbonShare Token

### Usage
Frontend
To use the frontend portion of the application:

Download the package and run npm i.
If you experience any issues with missing dependencies, try running npm install and --save to the system.

## Backend
To use the backend portion of the application:

Install the required packages listed in the requirements.txt file.
Make sure to use Python 2.7 to run the system.

## Micro Services
### smartContractMicroServices
Python script that checks for updates in the database and send transactions to the smart contract hosted in the EVM. 
Solidity source files and truffle components to help deploy the smart contract.

### databaseGeneration
Database Mock Data Generation files

# Contributing
We welcome contributions from the community. Please feel free to open a pull request or submit an issue if you encounter any problems or have any suggestions for improvement.

# License
This project is licensed under the MIT License.
