=======
History
=======

0.3.0 (2019-12-25)
--------------------

* ``read_hierarchy()`` now explicitly sets each entry from the "name" column to the "namelong" attribute and the "name" attribute is the region key. In past versions, these metadata would clobber important node attribute names.


0.2.2 (2019-12-25)
--------------------

* Patch minor additional issues package version metadata.


0.2.1 (2019-12-25)
--------------------

* Patch minor issue with deployment and package version metadata.


0.2.0 (2019-12-25)
--------------------

* Add ``read_hierarchy()`` to read regional hierarchy CSV files.


0.1.2a2 (2019-10-31)
--------------------

* Add ``read_csvv()`` and ``dalia.csvv.Csvv`` to read and represent CSVV files.
* Initial documentation.


0.0.1a1 (2019-10-10)
--------------------

* First release on PyPI.
