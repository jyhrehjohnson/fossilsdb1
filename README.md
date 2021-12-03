# fossilsdb1
BIO 382 Final Project
## Project Description
This final project set out to modify the Django admin interface to produce a new database/application cataloguing the hominin fossil and primate casts housed in the Anthropology Department. For the purpose of this final project and with the time constraints fo the semester, I will only be presenting the database administrative page and the source code associated with it. A further implication for this project is to set up and run a public facing page for departmental use. I will submit the full project with all the code I have created. Please draw your attention to the settings.py (fossilsdb1 directory), admin.py (casts directory), and models.py (casts directory)
## Instructions for Dr. Linder
-Download PyCharm

-Use the 'requirements' file to download the necessary packages to run my project

-Download the code from github

-Once you load the project into PyCharm click the green arrow at the top to Run

Once you run the server, you should see 

System check identified no issues (0 silenced).
December 02, 2021 - 19:26:37
Django version 3.2.7, using settings 'fossilsdb1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Click http://127.0.0.1:8000/ to open the database. 

-Once you have clicked the link, in the address, bar add /admin/ after the last forward slash. It should look like this: http://127.0.0.1:8000/admin/ this will bring you to the admin sign in page. 

-Please enter the following credentials to gain access:

-Username = rlinder 

-Password = Bio382_rl

-Under the 'Casts' header click 'Fossils'
-Once you have clicked 'Fossils' you will be brought to the admin page where you can input fossils

-I have provided an example input file for you to test the input function of the admin
-Use the export button to export the information presented in the admin
