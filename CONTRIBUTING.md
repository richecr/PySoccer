# Contributing
> You can contribute at will, you will always be welcome. But we have some rules to be followed.

## Add/Update features:
## Adicionar/Atualizar funcionalidades

Did you look at the application and think about some functionality that should be added to the project ?:open_mouth:

***So, you have two options:***

- [Open an issue detailing your idea](#creating-an-issue)
- [You implementation the feature yourself](#contribute-to-implementation)

## Creating an issue

On the [project page](https://github.com/richecr/PySoccer), you can click in `Issue` button and a `new issue` will appear on the page, so just select and follow the next step:

- Select the type of your issue: `Bug` or `Feature`.
- Give your issue a good name.
- Detail very well the purpose of the issue.
- Finally, click on `Submit new issue`.

## Clone the repository

On the home page of the [repository](https://github.com/richecr/PySoccer) there is a `Fork` button. When you click, just wait to complete the fork. And then it will create the repository in your account. And now just clone your machine, like this:

```sh
git clone https://github.com/<name_user>/PySoccer
```

When finished, you will have the repository on your computer and then just open it in your preferred editor and make your changes.

When you're done with your modifications, you should throw up your changes, but first:

```sh
git add .
```

The above command will prepare all modified files to be committed, going through all the changes that were made by you where it will decide if the change will be added (you must be inside the project folder to use the command). Now just commit the changes:

```sh
git commit -m "<your_message>"
```

Finally, you will send the changes to the remote repository:

```sh
git push origin master
```

But that will only change in your fork, the official repository will not have your changes now what ? :confused:

Calm down, now that the `Pull Request` or` PR` comes in

## Contribute to implementation:

After you fork and clone the project, choose your favorite text editor, we love VSCode, but feel free to choose yours. So it's time to code.

But calm there, before anything, you must **choose an issue** that you intend to work on. If the issue that deals with the functionality does not exist, you must create and say that you are working on it, if it exists you should say there (if you do not already have someone) that you intend to work on the issue. And after that, now you are ready to **code**.

### How to run the application:

We use poetry to manage packages. So, first of all we need to install it.

- Install poetry:

    ~~~bash
    $ pip install --user poetry
    ~~~

- To enter a shell within your virtual environment:

    ~~~bash
    $ poetry shell
    ~~~

- Install the dependencies used in the project:

    ~~~bash
    $ poetry install
    ~~~

For more details on [poetry](https://python-poetry.org/docs/)

**NOTE:** Execute the above command inside the project folder.

- Now you are ready to implement your functionality/correction.

#### Tests:

**NOTE:** Not yet done.
For testing we chose to use `pytest`, as it is well accepted by the Python community and quite easy to use.

- Install poetry:

    ~~~bash
    $ pip install --user poetry
    ~~~

- To enter a shell within your virtual environment:

    ~~~bash
    $ poetry shell
    ~~~

- Install the dependencies used in the project:

    ~~~bash
    $ poetry install
    ~~~

**NOTE:** The two commands above are only necessary if you have not already done so.

- To test that everything works fine, type in the terminal:

    ~~~bash
    $ poetry run pytest --version
    ~~~

- If the output is the same as below (you can change the version) everything is correct:

    ~~~bash
    $ This is pytest version 5.2.0, imported from /home/rickecr/.local/lib/python3.6/site-packages/pytest.py
    ~~~

- To run the test suite, simply run:

    ~~~bash
    $ poetry run pytest
    ~~~

- For running tests in watch mode:

    ~~~bash
    $ poetry run ptw
    ~~~


And now just create your test class, if it doesn't exist for the class you made the functionality.
You should create the tests for your functionality (s), trying to catch all extreme cases, we know it is difficult too.

And your changes should ensure that the other tests continue to work, unless you have found a problem with the code, something that shouldn't happen.

And after performing the tests, you are ready to perform your [PR](https://github.com/richecr/PySoccer/blob/master/CONTRIBUTING.md#making-a-pull-request--pr) and be happy with the OpenSource world.


### Entering the standards:

We chose to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) standard. Therefore, your code must not violate any of its rules. To check this, we use `flake8`.

#### Code Style:

We use poetry to manage our facilities.

- First you need to install pipenv:

    ~~~bash
    $ pip install --user poetry
    ~~~

- To install the dependencies used in the project:

    ~~~bash
    $ poetry install
    ~~~

**NOTE:** The two commands above are only necessary if you have not already done so.

- Execute flake8:

    ~~~bash
    $ flake8
    ~~~

## Making a Pull Request - PR

A yellow message will appear on your fork page asking you to make a Pull Request to the original repository. Clicking will open a page for you to fill in information about your PR.

- Refer to the issue you are working on using `#<issue_number>`

- Describe your changes

- Wait for the evaluation of your PR, and we may ask for some changes to be made
