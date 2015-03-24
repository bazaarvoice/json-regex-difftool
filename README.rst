JSON to JSON diff tool
======================

|Build Status|

Found a bug? Need a new feature? Want to help out? Check out the
`Contributor’s guide`_

Introduction
------------

A python module for checking equivalence and difference of two JSONs
with regex support

This repository will treat two types of JSON necessary for our purpose:

#. Regular JSON where only data is stored

#. Model JSON which will treat all keys and values as regular
   expressions

   -  Models will be used for comparing JSON objects to A model for
      equivalence with regex matching
   -  As JSON can be in a non-deterministic order, this is harder
      than doing a straight string comparison

There are four modes of this module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Regular JSON comparison
#. JSON to Model comparison
#. Regular JSON diff
#. JSON to Model Diff

1. Regular JSON comparison
--------------------------

This simply tests whether two files contating json are the same

.. code-block:: bash

    ./json_diff.py path/to/file1.json path/to/file2.json

Returns True if equal or False otherwise.

.. code-block:: bash

    .json_diff.py path/to/file1.json path/to/json_directory/

Returns the filename of the first match if there is one, or False
otherwise.

2. JSON to Model comparison
---------------------------

This mode tests whether a given JSON file matches a model when regular
expressions are evaluated.

.. code-block:: bash

    ./json_diff.py --mode j2m path/to/pure.json path/to/model.json

Returns True if the JSON and model match, False otherwise.

.. code-block:: bash

    ./json_diff.py --mode j2m path/to/pure.json path/to/model_directory

Returns the filename of the first match if there is one, or False
otherwise.

3. Regular JSON diff
--------------------

This mode computes a file diff between two JSON files.

*The logic flow of this code is loosely based off of code found in
https://github.com/monsur/jsoncompare*

*Assuming*


old.json:

.. code-block:: json

    {
        "accounting" : [ {
            "firstName" : "John",
            "lastName"  : "Doe",
            "age"       : 23
        }, {
            "firstName" : "Mary",
            "lastName"  : "Smith",
            "age"       : 31
        } ],
        "sales" : [ {
            "firstName" : "Sally",
            "lastName"  : "Green",
            "age"       : 27
        }, {
            "firstName" : "Jim",
            "lastName"  : "Galley",
            "age"       : 41
        } ]
    }

and new.json:

.. code-block:: json

    {
        "accounting" : [ {
            "firstName" : true,
            "lastName"  : "Doe",
            "age"       : 23
        }, {
            "firstName" : "Susan",
            "lastName"  : "Smith",
            "age"       : 31
        } ],
        "sales" : [ {
            "firstName" : "Sally",
            "lastName"  : "Green",
            "size"       : 27
        }, {
            "firstName" : "Jim",
            "age"       : 41
        } ]
    }

Then

Should produce output like:

.. code:: bash

    2015-03-24 12:59:08,576 - jsondiff - INFO - TypeDifference : accounting[0].firstName - is bool: (True), but was unicode: (John)
    2015-03-24 12:59:08,576 - jsondiff - INFO - Changed: accounting[1].firstName to Susan from Mary
    2015-03-24 12:59:08,576 - jsondiff - INFO - +: sales[0].size =27
    2015-03-24 12:59:08,576 - jsondiff - INFO - -: sales[0].age=27
    2015-03-24 12:59:08,576 - jsondiff - INFO - -: sales[1].lastName=Galley

4. JSON to Model Diff
---------------------

This mode computes a file diff between a JSON file and a model with
regular expressions.

***Note: at this time, we only support regular expression matching on
singleton values (that is values that are NOT a list or dictionary)***

*Assuming*


new.json:

.. code-block:: json

    {
        "accounting" : [ {
            "firstName" : "John",
            "lastName"  : "Doe",
            "age"       : 23
        }, {
            "firstName" : "Mary",
            "lastName"  : "Smith",
            "age"       : 31
        } ],
        "sales" : [ {
            "firstName" : "Sally",
            "lastName"  : "Green",
            "age"       : 27
        }, {
            "firstName" : "Jim",
            "lastName"  : "Galley",
            "age"       : 41
        } ]
    }

and model.json:

.. code-block:: json

    {
        "accounting" : [ {
            "lastName"  : "Doe",
            "age"       : 23
        }, {
            "firstName" : "Mary",
            "lastName"  : "Smith",
            "age"       : "[0-9]+"
        } ],
        "sales" : [ {
            "firstName" : "Sally",
            "lastName"  : "(.*)",
            "age"       : 24
        }, {
            "firstName" : "Jim",
            "lastName"  : "Galley",
            "age"       : 41
        } ]
    }

Then

.. code-block:: bash

    .json_diff.py -d --mode j2m new.json model.json

Should produce output

.. code-block:: bash

    2015-03-24 12:59:08,576 - jsondiff - INFO - +: accounting[0].firstName=John
    2015-03-24 12:59:08,576 - jsondiff - INFO - Changed: sales[0].age to 27 from 24

As you can see we find a match on numbers even though the type is ‘int’
(Mary Smith’s age). Also, even though we changed Sally’s age, we were
still able to find a match on her entry with a regular expression
representing her last name.

.. _Contributor’s guide: https://github.com/bazaarvoice/json-regex-difftool/blob/master/CONTRIBUTING.md

.. |Build Status| image:: https://travis-ci.org/bazaarvoice/json-regex-difftool.svg?branch=master
   :target: https://travis-ci.org/bazaarvoice/json-regex-difftool