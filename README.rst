ical
====

.. image:: https://travis-ci.org/AlEmerich/ical.png
   :target: https://travis-ci.org/AlEmerich/ical
   :alt: Latest Travis CI build status

Icalendar utilities. The `main.py` file offers a way to get event(s) of
a specified in the calendar, or the events in the next day presents in it.

Usage
-----

::

   usage: 
      main.py [-h] [-path PATH] [-y Y] [-m M] [-d D]

   positional arguments:
      -h, --help  show this help message and exit
      -path The path of the icalendar file, url of disk path
      -y the year of the date to search
      -m the month of the date to search
      -d the date of the date ot search

Launch test with tox.

::

    pip install tox && tox

Requirements
^^^^^^^^^^^^

- Icalendar_ 4.0.2
- Tox_ 3.4.0

.. _Icalendar: https://pypi.org/project/icalendar/
.. _Tox: https://pypi.org/project/tox/

Authors
-------

`ical` was written by `Alan Guitard  <alan.guitard.pro@gmail.com>`_.
