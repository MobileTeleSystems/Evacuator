.. title

Evacuator
=========

|Build Status| |Quality Gate Status| |Maintainability Rating| |Coverage|
|Documentation| |PyPI|

.. |Build Status| image:: https://gitlab.services.mts.ru/bigdata/platform/everproject/evacuator/badges/develop/pipeline.svg
    :target: https://gitlab.services.mts.ru/bigdata/platform/everproject/evacuator/-/pipelines
.. |Quality Gate Status| image:: https://sonar.bd.msk.mts.ru/api/project_badges/measure?project=evacuator&metric=alert_status
    :target: https://sonar.bd.msk.mts.ru/dashboard?id=evacuator
.. |Maintainability Rating| image:: https://sonar.bd.msk.mts.ru/api/project_badges/measure?project=evacuator&metric=sqale_rating
    :target: https://sonar.bd.msk.mts.ru/dashboard?id=evacuator
.. |Coverage| image:: https://sonar.bd.msk.mts.ru/api/project_badges/measure?project=evacuator&metric=coverage
    :target: https://sonar.bd.msk.mts.ru/dashboard?id=evacuator
.. |Documentation| image:: https://img.shields.io/badge/docs-latest-success
    :target: https://bigdata.pages.mts.ru/platform/everproject/evacuator/
.. |PyPI| image:: https://img.shields.io/badge/pypi-download-orange
    :target: http://rep.msk.mts.ru/ui/packages/pypi:%2F%2Fevacuator?name=evacuator&type=packages

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code


**Supports only Python 3.7+**

.. documentation

Documentation
-------------

See https://bigdata.pages.mts.ru/platform/everproject/evacuator/

.. contribution

Contribution guide
-------------------

See https://wiki.bd.msk.mts.ru/display/DAT/Contribution+guide

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

    git clone ssh://git@gitlab.services.mts.ru:8022/bigdata/platform/everproject/evacuator.git -b develop

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
