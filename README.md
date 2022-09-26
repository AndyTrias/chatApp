![ChatApp](https://i.ibb.co/Km0H7wW/ChatApp.png)

ChatApp is a simple chat application that allows users to communicate in real-time using socketIO and upload messages to a database. 

The project uses an SMS Authentication with Twilio


## Setup 
1. Create a twilio account

2 Clone this repository
``` 
git clone "https://github.com/AndyTrias/chatApp.git" 

``` 

3 cd to the directory and install the required dependencies
```sh
cd chatapp
pip install -r requirements.txt
```

4 To allow sms verification, you will need to configure your
```TWILIO_ACCOUNT_SID```, `TWILIO_AUTH_TOKEN``` and ```TWILIO_PHONE_NUMBER"``` as an environmental variable
