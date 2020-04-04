# Specsavers :eyeglasses:
_A Python wrapper around the Specsavers appointment booking API_

[![Build Status](https://travis-ci.org/alxwrd/specsavers.svg?branch=master)](https://travis-ci.org/alxwrd/specsavers)
[![Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://pypistats.org/api/packages/specsavers/recent?mirrors=false&label=downloads&query=$.data.last_month&suffix=/month)](https://pypistats.org/packages/specsavers)

> **IMPORTANT**: This project is NOT affiliated with Specsavers. Specsavers, nor this
library, should not be held responsible for any misinformation gained regarding
appointment information during the use of this library. 

> **NOTE**: Whilst this is a toy project, the endpoints it connects to are very real.
Please be responsible if you use this library: don't spam requests, and don't spam bookings.

## Example

```python
>>> import specsavers

# Find local stores
>>> stores = specsavers.locate(latitude=51.507879, longitude=0.087732)

# Closest / first store
>>> stores[0]
<Store name='londonwall'>

# Store by name
>>> stores["strand"]
<Store name='strand'>

# Lookup directly by name
>>>other_store = specsavers.find("nottingham")

>>> other_store.appointments() # Implies today
[<Appointment date='Jan 9', time='11:45'>, <Appointment date='Jan 9', time='15:00'>]

>>> other_store.appointments("tomorrow")[0]
<Appointment date='Jan 10', time='09:20'>
```

## What?

The Specsavers booking site is powered by a RESTful API. This library
aims to provide a simple, easy, and Pythonic interface to that service.


## Why?

I recently needed an eye test, and Specsavers has the ability to book online.
I needed an appointment fairly last minute (two days before), but fortunately,
there was _one_ slot left. I proceeded to make the appointment, but in the
time it had taken to fill in my details: it had already been taken.

I wanted to watch for new appointments to pop up, but frustratingly, every
time I refreshed the page, I was taken back to the first step of the process.

So I did some digging in the browsers dev tools. To my delight, I realised
that the Specsavers booking site is powered by a RESTful API. I wrote some
code to fetch appointments for the desired date; so I could watch to see if
another appointment became available.

In the end, I got an appointment for the day I wanted. I didn't want to let
my learnings about the API go to waste though, so I created this package!


## Using

### Installing

_Python 3.6+ only_

```shell
pip3 install specsavers
```


## Contributing

If you find any problems, you should open an
[issue](https://github.com/alxwrd/specsavers/issues).

If you can fix an issue you've found, or another issue, you should open
a [pull request](https://github.com/alxwrd/specsavers/pulls).

1. Fork this repository on GitHub to start making your changes to the master
branch (or branch off of it).
2. Write a test which shows that the bug was fixed or that the feature works as expected.
3. Send a pull request!

### Development setup

This project uses [poetry](https://python-poetry.org/docs/) to manage
dependencies, pytest [pytest](https://docs.pytest.org/en/latest/)
for tests, and [pycodestyle](https://github.com/PyCQA/pycodestyle) (formerly pep8)
for style checks.

```bash
# https://python-poetry.org/docs/#installation
# (If you haven't already)
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

git clone https://github.com/<yourname>/specsavers.git  # Clone the repo from your fork
cd specsavers
poetry install # Install all dependencies
poetry shell  # Start the new virtual enviroment

# Make changes

pytest tests  # Run tests
pycodestyle specsavers/ tests/  # Check style
```
