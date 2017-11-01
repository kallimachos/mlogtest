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

#. Generate logs using `create_mongodb_logs.py
   <https://github.com/jorge-imperial/create_mongodb_logs>`__. Adjust
   ``commands.js`` and ``mongod.conf`` as required.

   For example:

   ``python create_mongodb_logs.py --jscript commands.js -o logs``.

#. Run the ``transferlogs.py`` script to copy full log, conf file, and snippet
   logs for each version.

   This script creates directories for each log version in the form:
   ``v*/*/mongod.log``.

   For example:

   .. code::

      python transferlogs.py -i logs/ -o result/
      ...
      result/v3.2/3.2.1/mongod-3.2.1.log
      result/v3.2/3.2.1/mongod-3.2.1.conf
      result/v3.2/3.2.1/MTEST-insert
      result/v3.2/3.2.1/MTEST-bulkinsert

#. Run ``python transferlogs.py -h`` to see available options.


Diffing logs
~~~~~~~~~~~~

#. Run the ``difflogs.py`` script to produce a report of
   differences between the specified log versions.

   The script treats the first argument as the base version, and outputs the
   lines in the second file that differ from the first.

   For example:

   python difflogs.py logs/v3.2/3.2.1/ logs/v3.4/3.4.10/

#. Run ``python difflogs.py -h`` to see available options.
