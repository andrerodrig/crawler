# crawler

Crawler that collect data of locations and CEPs (zip codes) ranges
from correios web site. The output is a .jsonl file.

## Prerequisites
For running this package successfully, you must have installed the following softwares:
* Firefox browser
* Selenium Webdriver for Firefox - [geckodriver](https://github.com/mozilla/geckodriver/releases).
---
## Installation
First, verify if you have **Python 3.7** or a higher version.

Follow the steps bellow:
* Create a virtual environment with the command: `$ python -m venv venv`
* Linux:
    + Switch to venv: `$ source venv/bin/activate`
* Windows:
    + Switch to venv: `.\venv\Scripts\activate.bat`
* Enter the directory and install the package: `$ pip install -e .`

## Running the programm
In the virtualenv, execute the project with the command:
`$ crawler`

## Testing the project
For to be able to test the package, you must have installed the **pytest** package.

### If you use bash
So install that:
* Enter the venv and run: `pip install -e .[test]`

### If you use zsh
So install as follows:
* Enter the venv and run: `pip install -e ."[test]"`

With pytest installed, just make sure you are in the project directory, and run:
`$ pytest`


## Developer mode
If you want to use the developer mode, install as the following command:
`pip install -e .[dev]` (bash)

or

`pip install -e ."[dev]"` (zsh)
