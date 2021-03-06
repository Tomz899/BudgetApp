# BudgetApp - track your expenses

> My very first app made in django for comparing expanses within given budget.

## Table of contents

- [General info](#general-information)
- [Demo](#demo)
- [Technologies](#technologies-used)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [ToDo/Bugs](#todo-bugs)
- [Contact](#contact)

## General Information

This is my first application made in django, where you can provide your income and expanses and compare them. I used definition based views and tried to make it as simple as i could. For frontend i have used Bootstrap framework. Application have user registration and authentication system, so user can see only his data.

## Demo

Soon

## Technologies Used

- Django 3.2.9
- Python 3.8
- Bootstrap 3.4.1
- django-crispy-forms

## Screenshots

![alt text](https://github.com/Tomz899/BudgetApp/blob/main/img/screen_demo.png?raw=true)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tomz899/BudgetApp.git
$ cd BudgetApp
```

Create a virtual environment to install dependencies and activate it:

```sh
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:

```sh
(venv)$ cd project_name
(venv)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/budget/`.

## ToDo Bugs

- **{todo}** Find a way to solve double request POST issue for income and expanse form - at this moment there is workaround that input names in template are the same = "expanse".
- **{todo}** In views.py make budget definiton more simple, maybe split for more definitions.
- **{todo}** Add calendar and connect it with list of expenses, incomes for filtering options.
- **{todo}** Add some simple chart.
- **{todo}** Add ability for users to maintain their income data (similar to expanses).
- ~~**{bug}** Solve NonType issue for amount_left calculation.~~

## Contact

Created by [@me](mailto:tomek.nowak@aol.pl) - if you have any questions, just contact me!
