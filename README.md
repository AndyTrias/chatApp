![ChatApp](https://i.ibb.co/Km0H7wW/ChatApp.png)

ChatApp is a simple chat application that allows users to communicate in real-time using socketIO and upload messages to a database. 

The project uses an SMS Authentication with Twilio

It was a made as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/)




# Setup 

1. Create a [Twilio](https://www.twilio.com/es-mx/) account<br/>

- There is a 50 $USD bonus with the [Github Student Developer Pack](https://education.github.com/pack)

2. Get a phone number <br/>

 - All the information is [Here](https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1). 
 - If the number is from a development account, you will need to [verify](https://www.google.com/search?q=verify+caller+id+twilio&ei=OzMyY6yqMZ_e1sQP4LmueA&oq=verify+caller+id+&gs_lcp=Cgdnd3Mtd2l6EAMYADIECAAQEzIECAAQEzIICAAQHhAWEBMyCAgAEB4QFhATMggIABAeEBYQEzIICAAQHhAWEBMyCAgAEB4QFhATMggIABAeEBYQEzIICAAQHhAWEBMyCAgAEB4QFhATOgoIABBHENYEELADSgQIQRgASgQIRhgAUIUBWIUBYIYIaAFwAXgAgAF-iAF-kgEDMC4xmAEAoAEByAEIwAEB&sclient=gws-wiz) each number to be able to send them a message


3. Clone this repository
``` 
git clone "https://github.com/AndyTrias/chatApp.git" 
``` 

4. ```cd``` to the directory and install the required dependencies
```sh
cd chatapp
pip install -r requirements.txt
```

5. Configure Twilio Tokens 
- To allow SMS verification, you will need to configure your
```TWILIO_ACCOUNT_SID```, ```TWILIO_AUTH_TOKEN``` and  ```TWILIO_PHONE_NUMBER``` as an [environmental variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
- All of them can be found in your [Twilio settings](https://console.twilio.com/?frameUrl=/console)


# Description
As said, the project uses an MVC arhitecture pattern

## Models
For the data model, 4 entities are used

- ```User``` Whose phone is used for authentication and a name is stored as well.
- ```Contact``` Each user can have multiple contacts
- ```Message``` To store content, time and a sender(User) 
- ```MessageRecipient``` To hold the map between message and recipient since the recipient is also a User
