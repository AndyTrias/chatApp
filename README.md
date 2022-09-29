![ChatApp](https://i.ibb.co/Km0H7wW/ChatApp.png)

ChatApp is a simple chat application that allows users to communicate in real-time using socketIO and upload messages to a database.

The project uses an SMS Authentication with Twilio

It was made as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/)


# Setup 

1. Create a [Twilio](https://www.twilio.com/es-mx/) account<br/>

- There is a 50 $USD bonus with the [GitHub Student Developer Pack](https://education.github.com/pack)

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
```TWILIO_ACCOUNT_SID```, ```TWILIO_AUTH_TOKEN```, and  ```TWILIO_PHONE_NUMBER``` as an [environmental variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
- All of them can be found in your [Twilio settings](https://console.twilio.com/?frameUrl=/console)

6. Run the server
```
python app.py
```

# Description
As said, the project uses an MVC architecture pattern

## Models
For the data model, 4 entities are used
![Entities](https://i.ibb.co/S3p8w1F/Captura-de-pantalla-2022-09-28-204939.png)

- ```User``` Whose phone is used for authentication and a name is stored.
- ```Contact``` Each user can have multiple contacts
- ```Message``` To store content, time, and a sender(User) 
- ```MessageRecipient``` To hold the map between message and recipient since the recipient is also a User

In addition, there is a baseClass used for polymorphism to create a register in each table

## Views
On the one hand, for the authentication part, there are register, log, and verify as well as a startPage to used for redirection. On the other hand, for the chatApp there are add, delete, index, and chat

### Authentication
Both register and log have the task of either creating a new ```User``` or verifying if there is already a ```User``` in the Database using only the phone as input. After that, a message is sent to the user's phone which will have to authenticate in Verify

### Main
- Delete contact shows a dropdown list in which each element is a form containing the ```contact_id``` as a hidden value as a hidden value actually to delete them from the database

- Add contact only check that the user exists and is not already a contact

- The index shows a dropdown list with all the contact similarly to delete in the way that both of them have a form with the ```contact_id``` as a hidden value which is then used to redirect to chat

- Chat queries the database looking for all messages associated between the user and his contact and sends it to the client 

## Events
Uses Flask-socketIO for bidirectional communication between client and server<br/> 

Each time the user sends a message by pressing a button, a socket is sent from JS to the server without having to restart the page

In Flask, the message is uploaded to the database and sent to the receiver client using sockets.

## Helpers
- Only used to send messages with Twilio


