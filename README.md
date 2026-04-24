# LearnFlask
A repository for learning web development using Flask - HTML w/Jinja, CSS and JS

## Lesson 1. Clock
### Assignments:
----
- Javascript colours every selected timezone red. Make it highlight only the selected timezone
- Now, make the non-selected timezones disapper and display only the one that is selected
- Make the list display its values in two columns instead of one
- Add 5 more valid timezones to the list
- Make the time display not only in the ISO format, but also, next to it, in HH:MM:SS format
- Add to each timezones of the list a number, e.g. UTC, being first should become "1. UTC" - this should happen in the html template

## How to setup?
### 1. Select lesson from the tag list
----
<img width="330" height="237" alt="grafik" src="https://github.com/user-attachments/assets/ba03b306-6221-40fa-9e07-c1d354abc472" />

### 2. Clone the repository
----
Use `git clone -b 'tagName' --single-branch --depth 1 https://github.com/MAKiTsCharity/LearnFlask.git`, where tagName is the name of the selected tag (you can check it in the website url).

### 3. Create a python virtualenv
----
Refer to [Python docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments) on creating venv.

### 4. Install requirements.txt
----
```sh
pip install -r requirements.txt
```
### 5. Run the flask app
----
```sh
flask run --debug
```

### 6. Access at `127.0.0.1:5000`
----
That is where you can see the website you are developing.
