========
mlogtest
========

.. image:: https://travis-ci.org/kallimachos/mlogtest.svg?branch=master
   :target: https://travis-ci.org/kallimachos/mlogtest

.. image:: https://img.shields.io/pypi/status/mlogtest.svg?style=flat
   :target: https://pypi.python.org/pypi/mlogtest

.. image:: https://img.shields.io/pypi/v/mlogtest.svg?style=flat
   :target: https://pypi.python.org/pypi/mlogtest

.. image:: https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: https://img.shields.io/badge/Python-3.6-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: http://img.shields.io/badge/license-GPL-blue.svg?style=flat
   :target: http://opensource.org/licenses/GPL-3.0


Generating log files for comparison testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install required versions using ``m`` and generate ``versions.json`` using
   ``m installed --tojson >> versions.json``.

   or

   Create ``versions.json`` with required versions and paths.

#. Generate logs using ``create_mongodb_logs.py``. Adjust ``commands.js`` and
   ``mongod.conf`` as required.

   For example:

   ``python create_mongodb_logs.py --jscript commands.js -o logs``.

#. Run the ``transferlogs.sh`` script to copy full log, conf file, and snippet logs
   for each version.

   Options:

   .. code::

      -i  --input   source directory containing log files
      -o  --output  output directory where translogs creates version directories

   This script creates directories for each log version in the form:
   ``test/logfiles/v*/*/mongod.log``.

   For example:

   .. code::

      test/logfiles/v3.2/3.2.1/mongod.log
      test/logfiles/v3.2/3.2.1/mongod.conf
      test/logfiles/v3.2/3.2.1/test-insert.log

#. Commit the files to ``git``.

Testing logs
~~~~~~~~~~~~

#. Run the ``mtools/test/test_logs.py`` script to produce a report of
   differences between all log versions in the ``mtools/test/logfiles/``
   directory.


mtools feature requests
~~~~~~~~~~~~~~~~~~~~~~~
-  mloginfo option to summarize log file variations
   -  read mode (legacy, command)
   -  write mode (legacy, command)
   -  client information summary by version and operating system
   -  logevent should parse appname info -> mloginfo
