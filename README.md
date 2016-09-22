# turtlenotes-project
---------
http://www.cpturtlenotes.com

temporary username: johndoe

temporary password: qwerty123 

(this particular username/password will be active until 01-01-2017)

#### Overview
This website was designed to allow programmers from the University of Maryland to collaboratively edit and post lecture notes, answer student questions, and allow the programming community to interact with one another. Post functional capabilities of the site are set to launch in Spring 2017. The site is currently active to register, and contact the superuser for any inquiries or participate in the project.

I created this project using the following technologies:

- **Python**: Logic for the web framework guidelines
- **Django**: Web framework using the Model-View-Template (MVT) pattern
- **SQLite3**: Database to store all registration information, uploads, and posts
- **HTML**: Layout for the site
- **CSS**: *Responsive* and *fluid* structure for mobile usage (columns are based on percentages of screen width, and stack vertically on smaller devices)
- **Javascript**: Dynamic creation of the table rows to display results
- **Jquery**: Data validations to ensure clean user input
- **Git**: Version control system
- **GitHub**: Source code hosting for the git repository
- **Heroku**: Production web server to host the site

#### More Information
Their are no fees for registration and we do not work with the UMD Computer Science Program in any way. This is purely an open-source and non-profit project designed to help CS students share information. We currently have a few students who are graciously giving us their notes at the end of the semester. If you wish to contribute your notes or want to join us in future software development projects, let us know by sending us a message!

We do not condone cheating in anyway. Please omit from posting exam material, homeworks, classwork, or any other related material that may violate the UMD Code of Academic Integrity. We are not liable for any consequences that may result from cheating. The University of Maryland, College Park has a nationally recognized Code of Academic Integrity, administered by the Student Honor Council.B This code sets standards for academic integrity at Maryland for all undergraduate and graduate students. As a student you are responsible for upholding these standards for this course. It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit the SHC Website.

#### Instructions to Deploy Local Site

Feel free to copy this repository if you like my site! Here are some instructions in case you need help getting started.
If you have further questions, feel free to contact me.

- Run a virtualenv (Python2.7) 
- Make a directory for your Github clone of this repository
- pip install -r requirements.txt
- python manage.py collectstatic
- remove existing db.sqlite3 database and create a new one with python manage.py migrate 
- python manage.py createsuperuser (I hid my info from the repository > src.settings so make sure you put your info)
- Note: Prior to beginning deployment on heroku, I was using old_settings.py. You will have to change the file name back to settings.py
  if you wish to run it locally prior to deployment. The new file currently under my repository labeled "settings.py" is my deployment settings file. In other words run python manage.py runserver --settings=src.old_settings for your local site to run properly
- Open up a browser to 127.0.0.1:8000 and you should be up and running!

I deployed my site on Heroku and used the Heroku CDI which comes with git. I'm still somewhat new to Heroku so I will not be able to give in depth instructions. I have linked the site though and their instructions are pretty straightforward.
https://devcenter.heroku.com/articles/getting-started-with-python#introduction
