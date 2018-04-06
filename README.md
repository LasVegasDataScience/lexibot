# lexibot

Framework for building your own Amazon Lex (Alexa engine) interface to Slack

## QuickStart

### Initial Installation

```
# download this source
$ git clone https://github.com/LasVegasDataScience/lexibot.git

# move into the new directory
$ cd lexibot

# create a virtual environment for this directory
$ python3 -m venv venv

# activate your new virtual environment
$ source venv/bin/activate

# install base packages
$ pip install -r requirements

# install our scripts into your new environment
$ pip install .

# edit your configuration files (use your favorite text editor)
$ vi config/slack.ini config/lex.ini

# run your bot
$ bin/lexibot.py
```

### Subsequent Returns

```
# move to new directory
$ cd lexibot

# activate virtual environment
$ source venv/bin/activate

# run your bot
$ bin/lexibot.py
```

## How to Contribute

Find any typos? Does our documenation resemble lies? Heaven forbid, a bug or what some consider a feature? Contributions are welcome!

First, fork this repository.

![fork icon](https://github.com/lasvegasdatascience/lexibot/blob/master/images/fork-icon.png)

Next, clone this repository to your desktop to make changes.

```
$ git clone {YOUR_REPOSITORY_CLONE_URL}
$ cd lexibot
```

Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

![pull request icon](https://github.com/lasvegasdatascience/lexibot/blob/master/images/pull-request-icon.png)


## License

The contents of this repository are covered under the [MIT License](https://github.com/lasvegasdatascience/lexibot/blob/master/LICENSE).

