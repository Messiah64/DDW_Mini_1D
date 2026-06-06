# Mini Project 1: Sorting App

## Quick Run

The main Streamlit app file is `Home.py`.

```shell
streamlit run Home.py
```

## Learning Objectives
In this mini project, you will develop a web app to sort numbers using Streamlit. By the end of this assignment, you should be able to:
- Create a simple web app using Streamlit.
- Create Streamlit widgets such as button and text input.
- Display data on web page using Streamlit.

## Expected Output

[View video of expected output](https://sutdapac-my.sharepoint.com/:v:/g/personal/oka_kurniawan_sutd_edu_sg/EapXBAA9sTxPmNeCkg78RoQBdDZACI9U4qtBW12NcXxirg?e=J5advy).

### Project Structure

Once you have downloaded the repository, you can go to the repository and to the folder for this mini project. The commands below assume you are working from Github Codespace. Check the guide to launch Github Codespace. If you work from your local computer, the path might be different depending on where you download the mini project directory.

Assuming you are at `root` folder of your project in Codespace, list down all the files.


```shell
ls
```

The last command should output the following:

```shell
README.md		
Home.py
Pipfile
library.py
pages
```

Notes:
- This handout can be found in the file `README.md`.
- `Home.py` is the main Python script that gives us the main home page for the Streamlit application. 
- `Pipfile` is a text file that describes the packages you need to create the virtual environment.
- `library.py` is the Python file for you to do your exercises.
- `pages` is a folder containing two files which you need to modify for Exercise 1 and Exercise 2.

### Creating a Virtual Environment

> A **virtual environment** is a collection of packages that you separate out for specific projects. For example, this project requires Streamlit and runs on Python 3.10. Since we do not want conflict with our default system Python, we install the packages we need into a different space and activate that space (the _environment_) when we run our project. (It is _virtual_ because all your environments are still on the same physical machine.)

In the following steps, we will only display the Unix/Linux commands which you can do in Vocareum. If you want to work locally, see the [appendix](#appendix-setup-for-local-machine).

Go to the root folder of mini project 1 template.

```shell
$ cd /workspaces/10-020-data-driven-world-summer-2026-1d-mini-project-1-mini-project-1-template-xxx
```

First make sure that you have installed `pipenv` package. If not, run the following command in the terminal.

```shell
python -m pip install --user pipenv
```

<a id="local"></a>
We will call `mini-project-1-template` the **root** folder of our application. 

From the root folder, install the packages specified in the `Pipfile`.
```shell
python -m pipenv install
```

The above steps will install Streamlit.


To activate the virtualenv, run
```shell
python -m pipenv shell
```

Alternatively, you can choose every time you run a command to prepend that command with the following:
```shell
python -m pipenv run
```

Ok, so let's enter into the shell by typing:
```shell
python -m pipenv shell
```

You should see the word `(mini-project-1-template)` in your prompt something like:

```shell
(mini-project-1-template) user $
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
exit
```

All the subsequent exercises assumes you are in the virtualenv shell. 


## Brief Overview of Streamlit Application

We are using Streamlit framework to create this web app. The first file you may notice is `Home.py` in the root folder. Open that file using a text editor. You should see the following:

```python
import streamlit as st
st.set_page_config(
    page_title="Home"
)


st.header("Welcome to Mini Project 1")

st.write("In this project, you will generate some random number and sort them using one of the sorting function you learnt in class.")
st.write("Click the exercise at the sidebar to go to each exercise.")
```

Note:
- The first line imports the `streamlit` package and name it as `st` for subsequent use in the code.
- We rename the page title to "Home" using `set_page_config()` function.
- We display a text with Header format using `st.header()`.
- We can write text into the page using `st.write()`.

You can create multipage apps using `pages/` directory in your project structure. See [documentation](https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory) for more details. The steps are simple. You just need to have a directory or folder called `pages` in your root folder and put Python files inside this directory. 

If you list the files under `pages` directory, you will see we have two files. These will create two sub pages in Streamlit app.

```shell
ls pages
```

This will output the following:
```shell
1_Exercise_1.py	
2_Exercise_2.py
```

You will need to modify these two files for Exercises 1 and 2. Additionally, you have to create a new file `Exercise_3.py` for the open ended part.

## Running Streamlit Application

We can try running the web app. In order to do that, make sure you are inside the virtual environment by typing the following command.
```shell
python -m pipenv shell
```

To run the web app, type the following in the terminal.
```shell
streamlit run Home.py
```

The output looks like the following:

```shell
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.12.48:8501
  External URL: http://207.46.224.91:8501
```

Streamlit will attempt to open a web browser at `localhost:8051`. Do a `CTRL-click` on the `Local URL` link in Codespace and it will open the web page for you. You should be able to see the Home page with a sidebar menu. If you click Exercise 1 or 2 pages, you will see some errors for now. The reason is that you have not completed these exercises.

To stop the web app, type `CTRL+C` in the terminal. 

## Exercise 0

To start, you need to copy some code from your cohort problem which we will use in the subsequent exercises. 

First, copy the function `gen_random_int()` from Week 1 cohort problem into `library.py`. To do this, edit `library.py` using your preferred text editor. You should see the following code.

```python
import random

def gen_random_int(number: int, seed: int) -> list[int]:
    pass

def my_sort(array):
    pass
    
def create_string(array: list[int]) -> str:
    pass

```

Remove the keyword `pass` under `gen_random_int()` function and replace it with the code from your cohort problem set. 

Next, choose one of the sorting function that you do in Week 1 cohort or homework. This can either be Bubble Sort or Insertion Sort function. Paste the sorting algorithm under `my_sort()` function. 

Lastly, create a function called `create_string()` that takes in a list of integer and convert this list into  single string separated by comma. You can see some example of the expected input and output from the test file inside `test_library.py`.

To make sure everything works fine before you proceed, run the following code.

```shell
pytest
```

Check the output and make sure all the three tests pass.

```shell
====================== test session starts ======================
platform darwin -- Python 3.12.8, pytest-8.3.5, pluggy-1.5.0
rootdir: mini-project-1-folder-location
collected 3 items                                               

test_library.py ...                                       [100%]

======================= 3 passed in 0.01s =======================
```

## Exercise 1

Open and edit the file `pages/1_Exercise_1.py`.

### Task 1: Generating Random Integers 


We have two buttons. The first button is to generate 10 random numbers. We will bind the event `on_click` of this button to the function `generate()` in your `1_Exercise_1.py`. Fill in this function to do the following:

- generate 10 random integers by calling the function `gen_random_int()` from your `library.py` and store it a variable called `array`. Assign the `seed` for the `gen_random_int()` to the current time. You can use `datetime.now().timestamp()` as your seed.
- create a single string from the list of numbers using the function `create_string()` inside your `library.py`. 
- store this string into the session state called `numbers`. 

Questions:

- Which line of the code creates the Generate button?
- How does Streamlit bind the on-click event to the function `generate()`?
- Which line that displays the generated numbers?
- What is `session_state` and how is it used?

## Task 2: Sorting Numbers

The second button on this first exercise is to sort the generated list of numbers. Write a function handler when the Sort button is clicked. Fill in the function `sort_generated_numbers()` to do the following:

- Get the list of numbers as a single string from the session state.
- Write a code to convert that single list to a list of integers.
- Sort the list using `my_sort()` function.
- Convert the list back to a single string by calling `create_string()` function.
- Store the resulting string into the session state.

Questions to ponder:

- What is the name of the session state key used to store the generated numbers?
- What is the name of the session state key used to store the sorted numbers?

## Task 3: Creating Streamlit Widget

In this task, you will add new Streamlit Widget. Refer to the following documentations on how to create some of these widgets:

- [Button](https://docs.streamlit.io/develop/api-reference/widgets/st.button)
- [Write and Magic](https://docs.streamlit.io/develop/api-reference/write-magic)

Fill in the Task 3 part at the end of `1_Exercise 1.py` file to do the following:

- Write a code to create a button called `Sort` and bind it to the function `sort_generated_numbers()`.
- Write a code to display the sorted numbers in the following format: `Sorted Numbers: 1, 2, 3, ... .`. 


## Exercise 2

In this exercise, you will apply what you have learnt in Exercise 1 to create a similar page where user can enter their own numbers and sort it. Open the file `2_Exercise 2.py` and edit accordingly.

Question to answer before attempting Task 1:

- Which line of the code create a Text Input widget for the user to enter the list of numbers?
- What is the session state key name where these numbers are stored?
- What is the data type stored inside this session state key?

### Task 1

Fill in the code inside `sort_numbers()` function to do the following:

- Read the numbers entered by the user from the session state.
- Convert the data into a list of integers.
- Call `my_sort()` function to sort the list.
- Convert back to a single string by calling `my_sort()` function.
- Store the resulting string into the session state.

Questions to ponder:

- What is the name of the session state where the resulting sorted numbers are stored?
- What are the advantages of calling functions like `my_sort()` and `create_string()` instead of copy pasting the code?
    
### Task 2

In this task, we will complete the page by creating the rest of the widgets.

- Create a button which sort the list of numbers when the user clicks it. 
- Display the sorted numbers as a text.
- Create a button that clears the Text Input and the displayed sorted numbers when the user clicks it.

## Exercise 3

This is an open ended part of your mini project. Create a new page by creating a new file called `3_Exercise_3.py`. You are free to design what you want to do for this page as long as it satisfies the following constraints.

- You should use a new sorting algorithm that is not taught in class, cohort problem set and homework problem sets. You have to implement this new sorting algorithm from scratch without using any built-in function in Python or any other third-party library.
- Your page should make use of the sorting algorithm to sort **non-numeric** data. You are allowed to sort numeric data if it is a component of another collection data type such as a tuple, dictionary with a numeric keys, etc.

Follow the guides below to complete your task:

1. Brainstorm on the data used by various apps, websites, or any information systems. List down all the various data that you see that may require sorting algorithm.
1. Choose one that you would like to simulate on your Exercise 3 page. Use the above constraints in your consideration as well as the complexity of **inputting** and **displaying** the data.
1. Choose one sorting algorithm which you would like to learn and implement.
1. Implement the new sorting algorithm and put it inside `library.py`.
1. Import the sort function inside your `3_Exercise_3.py`.
1. Design the User Interface (UI) to input the data and display the data.
1. Create two buttons. The first button is to sort the data and the second button is to clear the data to the original state.

During your checkoff you need to present the following for Exercise 3.

* Your brainstorming of your ideation for the data. Show the inspiration from the various apps, websites, or any other information systems that you use during your brainstorming sessions. Do document your brainstorming either on Miro, FigJam or other tools.
* Present your criteria for your selection using Pugh Chart.
* Do the same for your algorithm brainstorming and selection. Present your case why you choose this particular algorithm to implement using Pugh Chart.
* Present your UI design using either Miro or Figma. You need to have more than one single design and one single iteration. You need to be able to share your design choice that leads you to your final UI design.
* Demo and present your working app and implementation.
* Explain the algorithm that you choose and be prepared to do ["whiteboard coding"](https://coderpad.io/resources/learn/whiteboard-for-programmers/) with the instructors.

## Appendix: Setup for Local Machine

You can choose to do the mini project on your local machine first before submitting to Vocareum. 

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:

- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)
- Unix: [Git for Unix](https://git-scm.com/downloads/linux)

### Accepting an Assignment from Github Classroom

Find the link to accept the Github Classroom assignment from eDimension for the respective week. When you accept the Github Classroom assignments, it will create a private repository of the project in your Github account. 

If you do the project with more than one person, add your teammates when accepting the assignment in Github classroom. This allows your teammates to have access to the repository as well. 

Once you have your own student copy of the repository, you can clone the repository to your local machine.

### Downloading Repository

Clone the mini project repository from Github. On your local computer's terminal or Git Bash, type the following:

```shell
cd /path/to/your/projects/folder  # change this
git clone https://your-mini-project-1-repo-url
```

**Replace the URL** with your mini project 1 URL from the Github repository page, then follow all the Virtual Environment steps above.

### Installing Environment Locally

The `Pipfile` was tested in Vocareum with Python 3.12. Some packages may break if you use a different Python version -- welcome to software engineering dependency hell! We recommend using Miniconda just for this course and create a separate environment for it.

[Download Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install), then open Anaconda Prompt (Windows) or Terminal (Mac/Linux). Run

```shell
conda create -n ddw python=3.12 pipenv
conda activate ddw 
```
This will create a new environment called `ddw` with Python 3.12 and Pipenv installed, and activate it.

Then follow the steps [above](#local). You can directly use `pipenv` for all commands instead of `python -m pipenv`.

### Submission

When you are done with local changes, do this to get all your updates into Github:

```shell
cd /path/to/your/projects/folder/mini-project-1  # change this
git add .
git commit -m "Completed version"  # or some update message
git push  # follow the instructions
```

You need to connect your Github account to Gradescope for submission. See the instruction in eDimension for this. You only need to do this once. After connecting your Github account, you can choose your repository to submit to Gradescope submission for your 1D Mini Project assignment.
