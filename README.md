# Shopify Summer Internship Coding Challenge 2018
[![Build Status](https://travis-ci.com/apoorvkk/Shopify-Software-Engineering-Challenge.svg?token=7za4HVGA8yu8XhiNzTJy&branch=feature-menu-validator)](https://travis-ci.com/apoorvkk/Shopify-Software-Engineering-Challenge)
## Summary

TODO: add web application photos here.

[Shopify's Sofware Engineering Challenge](https://backend-challenge-summer-2018.herokuapp.com/) required me to create a program that will aggregate a list of given related products into valid and invalid menus. Invalid menus were those that has cyclic references between products (an item on a menu) or a menu that has a max depth greater than 4. This project will allow merchants who have different products to easily present the products via organised, valid and clean menus.

### Assumptions Made
There were a number of assumptions that had to be made during development:
1. The outputted `children` array for each outputted menu can have any order.
2. The depth of a node is ***the number of edges from the node to the tree's root node***. A root node will have a depth of 0.
3. The `root_id` will only be included in the `children` array for each outputted menu ***if there is a cyclic reference to the root node***.
4. The `per_page` attribute inside `pagination` in the response from Shopify's backend system will remain constant.
5. `id` and `page` will only be `int`.

TODO: Add photos of different cases.

## Project Approach
I have produced two versions of this project. The first is a `Python` program that can be run in the terminal ([Command Line Interface Version](#command-line-interface-version)).

As I made the first program very modular, I was able to ***port the first program*** into a web application ([Web Application Version](#web-application-version)). The web application is hosted on Heroku (see: TODO).

Both project versions have been outlined below. I have documented how to install both projects locally, how to run the unit tests and how to run the actual programs locally.

## Common Installation and Setup
**Note**: This installation works best on Mac/Linux environments.

Requirements:

- `git`
- `python3.6.4`, `pip`
- `virtualenv` - `pip install virtualenv`

### STEP ONE - Setting Up Virtual Environment

Open up your terminal and go into an empty directory of choice. Run the command below to create a virtual environment:
```
virtualenv -p python3 ShopifyEnv
```

From here, run the two commands below to activate the newly created virtual environment:
```
cd ShopifyEnv
source bin/activate
```

The virtual environment has now been activated and all dependencies will be installed inside here.

**Note**: You can exit the virtual environment by using the `deactivate` command.

### STEP TWO - Import Project Source Code

Now that we have the virtual environment activated, run the command below to load the project:
```
git clone https://github.com/apoorvkk/Shopify-Software-Engineering-Challenge.git
```

### STEP THREE - Install Python Packages
Run the command below to locate the `python` dependencies file `requirements.txt`:
```
cd Shopify-Software-Engineering-Challenge/
```

There should be a file called `requirements.txt` here. Run the command below to install the Python dependency packages within the virtual environment:
```
pip install -r requirements.txt
```
**Note**: If `pip` does not work, please try `pip3`.
## Command Line Interface Version
### Running the Application
Locate yourself inside the root of `Shopify-Software-Engineering-Challenge/` `git` repository if not done already. Ensure you are inside your virtual environment (see [Common Installation and Setup](#common-installation-and-setup)).

Run the commands below:
```
cd MenuValidator/cli/
python main.py
```
**Note:** You might need to use `python3` command if `python` does not work.

You will be prompted to provide the `problem id` so input the selected problem of choice. As it stands from `09/01/18`, there are currently two different problems (`id=1` for the standard challenge and `id=2` for the extra challenge).

### Testing the Application
Locate yourself inside the root of `Shopify-Software-Engineering-Challenge/` `git` repository if not done already. Ensure you are inside your virtual environment (see [Common Installation and Setup](#common-installation-and-setup)).

Run the commands below:
```
cd MenuValidator/cli/
python -m unittest discover menus/
```
**Note:** You might need to use `python3` command if `python` does not work.

### Linting the Application
Locate yourself inside the root of `Shopify-Software-Engineering-Challenge/` `git` repository if not done already. Ensure you are inside your virtual environment (see [Common Installation and Setup](#common-installation-and-setup)).

The application follows the PEP8 standard. Please run the commands below:
```
cd MenuValidator/cli/
flake8
```

## Web Application Version
TODO.

## Architectural Design
TODO.
### Stack and Tools Used (include testing frameworks)
#### Application Specific
TODO.
#### Backend
TODO.
#### Frontend
TODO.
#### Misc
- github
- Travis CI
- Heroku

### Application Specific Design (Menu Validation)
TODO.
