BTrieve Driver
==============

This project presents a pure Python implementation of the BTrieve database
driver.

TODO
====

* V8 Support
* Schema tools
* Query engine
* Connections
* SQLAlchemy integration
* Write to DB

Find more database examples


DDF File Format
===============

Files (Case insensitive)
------------------------

file.ddf
fields.ddf - A collection of all fields in all tables with a table ID
index.ddf


High Level File Contents
========================

* Each file contains a number of pages
* Each page contains a number of blocks.
* The block size is 256 bytes.

+-------------------------------------------+
| PAGE                                      |
| +---------------------------------------+ |
| | BLOCK (256 Bytes)                     | |
| |                                       | |
| +---------------------------------------+ |
| +---------------------------------------+ |
| | BLOCK (256 Bytes)                     | |
| |                                       | |
| +---------------------------------------+ |
| +---------------------------------------+ |
| | BLOCK (256 Bytes)                     | |
| |                                       | |
| +---------------------------------------+ |
| +---------------------------------------+ |
| | BLOCK (256 Bytes)                     | |
| |                                       | |
| +---------------------------------------+ |
+-------------------------------------------+

Page size = block size (256) * page block count

The File Control Record Block
=============================

The first block in any file is the File Control Record (FCR)

Magic number for the file is in the first 2 bytes. The contents are: FC

The first 44 bytes of the FCR contain the page size for the version of the files.

Sample data for this section (i=ignore):

FCiiAAAABBCCDDDDEEEEFFGGxxxxxxxxxxxxxxxxxxxx

* A = Usage count
* B = Version 6 page blocks
* C = Acceleration flags
* D = Next reuse page (Page pointer)
* E = Next reuse record (Record pointer)
* F = Defined keys
* G = Record length
* C = Version 8 page blocks
* 
