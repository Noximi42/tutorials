.. documentation documentation master file, created by
   sphinx-quickstart on Thu May 16 12:40:08 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to documentation's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Introduction
============

This is a sample document written in reStructuredText. This format is used for writing technical documentation and supports a variety of features.

Sections are created using overline and underline adornments.

Paragraphs are separated by blank lines.

.. This is a comment. It will not be rendered in the output.


Features
========

Inline Markup
-------------

Text can be written *italic*, **bold**, or as ``code``.

Hyperlinks can be included like `this <https://heise-academy.de>`_.

Lists
-----

Unordered Lists
^^^^^^^^^^^^^^^

* one item
* another item

  * one subitem
  * another subitem

* final item

Ordered Lists
^^^^^^^^^^^^^

#. first item
#. second item

   a. first subitem
   b. second subitem

#. third item

Source Code
-----------

.. code:: python

   def hello_world():
       print('Hello, World!')

Math
----

.. math::

   \lim_{n \to \infty} \frac{n}{\sqrt[n]{n!}} = e


Kroki Diagrams
==============

See examples at: `<https://kroki.io/examples.html>`_

Block Diagram
-------------

.. kroki:: blockdiag

   blockdiag {
       A -> B -> C -> D;
       A -> E -> F -> G;
   }

UML Diagram
-----------

.. kroki:: plantuml

   class Animal
   class Dog
   class Cat
   class Main
   Animal <|-- Dog
   Animal <|-- Cat
   Main --> Animal
   Main ..> Dog
   Main ..> Cat
