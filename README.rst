.. title

Evacuator
=========

|Build Status|
|ReadTheDocs| |PyPI|

.. |Build Status| image:: https://github.com/MobileTeleSystems/evacuator/workflows/Tests/badge.svg
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |ReadTheDocs| image:: https://readthedocs.org/projects/evacuator/badge/?version=latest
    :target: https://evacuator.readthedocs.io/en/latest/?badge=latest
.. |PyPI| image:: https://img.shields.io/badge/pypi-download-orange
    :target: http://rep.msk.mts.ru/ui/packages/pypi:%2F%2Fevacuator?name=evacuator&type=packages

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code


**Supports only Python 3.7+**

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

.. install

Installation
---------------

Stable release
~~~~~~~~~~~~~~~
Stable version is released on every tag to ``master`` branch. Please use stable releases on production environment.
Version example: ``1.0.0``

.. code:: bash

    pip install evacuator==1.0.0 # exact version

    pip install evacuator # latest release

.. development

Development
---------------

Clone repo
~~~~~~~~~~~

.. code:: bash

    git clone git@github.com:MobileTeleSystems/Evacuator.git -b develop

    cd mtspark

Install dependencies for development:

.. code:: bash

    pip install -r requirements-dev.txt

Pre-commit
~~~~~~~~~~

Install pre-commit hooks:

.. code:: bash

    pre-commit install
    pre-commit autoupdate
    pre-commit install-hooks

Test pre-commit hooks run:

.. code:: bash

    pre-commit run --all-files -v

Testing
~~~~~~~~~~~~~~~
Run tests using ``pytest``

.. code:: bash

    pytest
