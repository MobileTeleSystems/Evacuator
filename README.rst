.. title

Evacuator
=========

|Repo Status| |PyPI| |PyPI License| |PyPI Python Version|
|Documentation| |Build Status| |Coverage|

.. |Repo Status| image:: https://www.repostatus.org/badges/latest/active.svg
    :target: https://github.com/MobileTeleSystems/evacuator
.. |PyPI| image:: https://img.shields.io/pypi/v/evacuator
    :target: https://pypi.org/project/evacuator/
.. |PyPI License| image:: https://img.shields.io/pypi/l/evacuator.svg
    :target: https://github.com/MobileTeleSystems/evacuator/blob/develop/LICENSE.txt
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/evacuator.svg
    :target: https://badge.fury.io/py/evacuator
.. |Build Status| image:: https://github.com/MobileTeleSystems/evacuator/workflows/Tests/badge.svg
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |Documentation| image:: https://readthedocs.org/projects/evacuator/badge/?version=stable
    :target: https://evacuator.readthedocs.io/en/stable/
.. |Coverage| image:: https://codecov.io/gh/MobileTeleSystems/evacuator/branch/develop/graph/badge.svg?token=CM6AQWY65P
    :target: https://codecov.io/gh/MobileTeleSystems/evacuator

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code.

Designed to be used in `Apache Airflow <https://airflow.apache.org/>`__ with:
    * ``BashOperator``
    * ``SSHOperator``
    * ``DockerOperator``
    * ``KubernetesPodOperator``
    * any other operator which can handle process exit codes.

.. installation

How to install
---------------

.. code:: bash

    pip install evacuator

.. documentation

Documentation
-------------

See https://evacuator.readthedocs.io/

.. contribution

Contribution guide
-------------------

See `<CONTRIBUTING.rst>`__

.. security

Security
-------------------

See `<SECURITY.rst>`__
