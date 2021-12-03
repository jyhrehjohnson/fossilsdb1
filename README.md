# fossilsdb1
## BIO 382 Final Project
## Project Description
This final project set out to modify the Django admin interface to produce a new database/application cataloguing the hominin fossil and primate casts housed in the Anthropology Department. For the purpose of this final project and with the time constraints of the semester, I present the database administrative page and the source code associated with it. In this project, I present source code that allows the user to input data directly through the admin page or file import, code to export all input data, and create models for display. The source code for settings.py can be found in the fossilsdb1 directory, admin.py in the casts directory, and models.py in the casts directory. Through this project I learned how to use Django, PyCharm, and GitHub. A further implication for this project is to set up and run a public facing page for departmental use.
## Instructions for Dr. Linder
-Download PyCharm.

-Download the code from github.

-In your vitual environment, run the command "pip install -r requirements.txt" to download the packages needed to run the project from the 'requirements.txt' file.

-Once you load the project into PyCharm click the green arrow at the top to Run.

After you run the server, you should see: 

System check identified no issues (0 silenced).
December 02, 2021 - 19:26:37
Django version 3.2.7, using settings 'fossilsdb1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Click http://127.0.0.1:8000/ to open the database. 

-After you have clicked the link, in the address bar, add /admin/ after the last forward slash. 
It should look like this: http://127.0.0.1:8000/admin/ this will bring you to the admin sign-in page. 

-Enter the following credentials to gain access:

-Username = rlinder 

-Password = Bio382_rl

-Under the 'Casts' header click 'Fossils'

-Once you have clicked 'Fossils' you will be brought to the admin page where you can input fossils.

-I have provided an example input file for you to test the file import capabilities of the admin.

-Use the export button to export the information displayed in the admin.
