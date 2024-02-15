Contributing Guide
==================

Welcome! There are many ways to contribute, including submitting bug
reports, improving documentation, submitting feature requests, reviewing
new submissions, or contributing code that can be incorporated into the
project.

Initial setup for local development
-----------------------------------

Install Git
~~~~~~~~~~~

Please follow `instruction <https://docs.github.com/en/get-started/quickstart/set-up-git>`_.

Create a fork
~~~~~~~~~~~~~

If you are not a member of a development team building Evacuator, you should create a fork before making any changes.

Please follow `instruction <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_.

Clone the repo
~~~~~~~~~~~~~~

Open terminal and run these commands:

.. code:: bash

    git clone git@github.com:myuser/evacuator.git -b develop

    cd evacuator

Setup environment
~~~~~~~~~~~~~~~~~

Create virtualenv and install dependencies:

.. code:: bash

    # create virtual environment
    python -m venv venv
    source venv/bin/activate
    pip install -U wheel
    pip install -U pip setuptools

    # install requirements
    pip install -U \
        -r requirements-dev.txt \
        -r requirements-docs.txt \
        -r requirements-test.txt

Enable pre-commit hooks
~~~~~~~~~~~~~~~~~~~~~~~

Install pre-commit hooks:

.. code:: bash

    pre-commit install --install-hooks

Test pre-commit hooks run:

.. code:: bash

    pre-commit run

How to
------


Run tests
~~~~~~~~~

.. code:: bash

    # run tests
    pytest


Build documentation
~~~~~~~~~~~~~~~~~~~

Build documentation using Sphinx:

.. code:: bash

    cd docs
    make html

Then open in browser ``docs/_build/index.html``.


Review process
--------------

Please create a new GitHub issue for any significant changes and
enhancements that you wish to make. Provide the feature you would like
to see, why you need it, and how it will work. Discuss your ideas
transparently and get community feedback before proceeding.

Significant Changes that you wish to contribute to the project should be
discussed first in a GitHub issue that clearly outlines the changes and
benefits of the feature.

Small Changes can directly be crafted and submitted to the GitHub
Repository as a Pull Request.

Create pull request
~~~~~~~~~~~~~~~~~~~

Commit your changes:

.. code:: bash

    git commit -m "Commit message"
    git push

Then open Github interface and `create pull request <https://docs.github.com/en/get-started/quickstart/contributing-to-projects#making-a-pull-request>`_.
Please follow guide from PR body template.

After pull request is created, it get a corresponding number, e.g. 123 (``pr_number``).

Write release notes
~~~~~~~~~~~~~~~~~~~

``Evacuator`` uses `towncrier <https://pypi.org/project/towncrier/>`_
for changelog management.

To submit a change note about your PR, add a text file into the
`docs/changelog/next_release <./next_release>`_ folder. It should contain an
explanation of what applying this PR will change in the way
end-users interact with the project. One sentence is usually
enough but feel free to add as many details as you feel necessary
for the users to understand what it means.

**Use the past tense** for the text in your fragment because,
combined with others, it will be a part of the "news digest"
telling the readers **what changed** in a specific version of
the library *since the previous version*.

You should also use
reStructuredText syntax for highlighting code (inline or block),
linking parts of the docs or external sites.
If you wish to sign your change, feel free to add ``-- by
:user:`github-username``` at the end (replace ``github-username``
with your own!).

Finally, name your file following the convention that Towncrier
understands: it should start with the number of an issue or a
PR followed by a dot, then add a patch type, like ``feature``,
``doc``, ``misc`` etc., and add ``.rst`` as a suffix. If you
need to add more than one fragment, you may add an optional
sequence number (delimited with another period) between the type
and the suffix.

In general the name will follow ``<pr_number>.<category>.rst`` pattern,
where the categories are:

- ``feature``: Any new feature
- ``bugfix``: A bug fix
- ``improvement``: An improvement
- ``doc``: A change to the documentation
- ``dependency``: Dependency-related changes
- ``misc``: Changes internal to the repo like CI, test and build changes

A pull request may have more than one of these components, for example
a code change may introduce a new feature that deprecates an old
feature, in which case two fragments should be added. It is not
necessary to make a separate documentation fragment for documentation
changes accompanying the relevant code changes.

Examples for adding changelog entries to your Pull Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: rst
    :caption: docs/changelog/next_release/1234.doc.1.rst

    Added a ``:github:user:`` role to Sphinx config -- by :github:user:`someuser`

.. code-block:: rst
    :caption: docs/changelog/next_release/2345.bugfix.rst

    Fixed behavior of ``WebDAV`` connector -- by :github:user:`someuser`

.. code-block:: rst
    :caption: docs/changelog/next_release/3456.feature.rst

    Added support of ``timeout`` in ``S3`` connector
    -- by :github:user:`someuser`, :github:user:`anotheruser` and :github:user:`otheruser`

.. tip::

    See `pyproject.toml <pyproject.toml>`_ for all available categories
    (``tool.towncrier.type``).

.. _Towncrier philosophy:
    https://towncrier.readthedocs.io/en/stable/#philosophy

How to skip change notes check?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just add ``ci:skip-changelog`` label to pull request.

Release Process
^^^^^^^^^^^^^^^

Before making a release from the ``develop`` branch, follow these steps:

0. Checkout to ``develop`` branch and update it to the actual state

.. code:: bash

    git checkout develop
    git pull -p

1. Backup ``NEXT_RELEASE.rst``

.. code:: bash

    cp "docs/changelog/NEXT_RELEASE.rst" "docs/changelog/temp_NEXT_RELEASE.rst"

2. Build the Release notes with Towncrier

.. code:: bash

    VERSION=$(cat evacuator/VERSION)
    towncrier build "--version=${VERSION}" --yes

3. Change file with changelog to release version number

.. code:: bash

    mv docs/changelog/NEXT_RELEASE.rst "docs/changelog/${VERSION}.rst"

4. Remove content above the version number heading in the ``${VERSION}.rst`` file

.. code:: bash

    sed "0,/^.*towncrier release notes start/d" -i "docs/changelog/${VERSION}.rst"

5. Update Changelog Index

.. code:: bash

    sed -E "s/DRAFT/DRAFT\n    ${VERSION}/" -i "docs/changelog/index.rst"

6. Restore ``NEXT_RELEASE.rst`` file from backup

.. code:: bash

    mv "docs/changelog/temp_NEXT_RELEASE.rst" "docs/changelog/NEXT_RELEASE.rst"

7. Commit and push changes to ``develop`` branch

.. code:: bash

    git add .
    git commit -m "Prepare for release ${VERSION}"
    git push

8. Merge ``develop`` branch to ``master``, **WITHOUT** squashing

.. code:: bash

    git checkout master
    git pull
    git merge develop
    git push

9. Add git tag to the latest commit in ``master`` branch

.. code:: bash

    git tag "$VERSION"
    git push origin "$VERSION"

10. Update version in ``develop`` branch **after release**:

.. code:: bash

    git checkout develop

    NEXT_VERSION=$(echo "$VERSION" | awk -F. '/[0-9]+\./{$NF++;print}' OFS=.)
    echo "$NEXT_VERSION" > evacuator/VERSION

    git add .
    git commit -m "Bump version"
    git push
