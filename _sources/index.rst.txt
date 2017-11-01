========
mlogtest
========

*Last updated:* |today|

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

#. Run the ``transferlogs.sh`` script to copy full log, conf file, and snippet
   logs for each version.

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


Modules
~~~~~~~

.. toctree::

   difflogs.rst
   transferlogs.rst
