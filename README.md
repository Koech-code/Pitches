## PITCHES APP 

### Description
> This is a web application where you can view the pitches that other people have written.
  You can also upvote or downvote on the pitches, but first you have to sign up to the application or login if you already have an account.

## Author

👤 **Author**
- Nixon Kipkorir Koech

- GitHub: [@Koech-code](https://github.com/Koech-code)

## Technologies Used

- HTML
- CSS
- PYTHON `3.6`
- PYTHON SHELL 
- FLASK
- FLASK_BOOTSTRAP
- HEROKU

### User Stories
As a user I would like to;

- see the pitches that other people have posted. 
- vote on the pitch I like and give it a downvote or upvote. 
- be signed in so that I can leave a comment.
- receive a welcoming email once I sign up. 
- view the pitches I have created in my profile page. 
- comment on the different pitches and leave feedback. 
- submit a pitch in any category. 
- view the different pitch categories.


## Behavior Driven Development (BDD):
These are the actions the user will do, inputs required and their outputs on the page. 

  | Action    | Input                                      | Output                        |
  | ----------|:-------------                              | :------                       |
  | Load page | On page load                               | Displays the homepage         |
  | Sign up   | email, username, password, confirm password| Redirected to login page page |
  | Login     | username, password                         | Redirect to homepage          |
  | Select Comment| a comment                              | Your comment displayed        |
  |           |                                            |                               |
## Live Demo

[Live Demo Link]( https://koechpitchesapp.herokuapp.com/)


### Installation Process

- Clone the repository using the link below

```
$ git clone https://github.com/Koech-code/Pitches.git

```

- Create a directory and install the requirements

  ```
  cd Pitches
  pip install -r requirements.txt
  ```
- Export configurations
  ```
  Database URL
  Secrete Key
  Mail_username
  Mail_password
  ```
- Run the application using;
  ```
  python3.6 manage.py server
  ```
- Test it if its working using;
  ```
  python3.6 manage.py test
  ```
- Open the application on your browser , preferably `chrome` using port `127.0.0.1:5000`


## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- I would like to acknowledge Moringa school for giving me this opportunity to learn software development.
- Appreciations to  my TM `Nancy Umutoniwase` for the support she gives me.

## 📝 License

This project is [MIT](LICENCE) licensed.