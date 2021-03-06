BTrieve Driver
==============

This project presents a pure Python implementation of the BTrieve database
driver. Due to there not being a great deal of information about this
database format, this is mostly an exercise in reverse engineering the binary
grammar.


Current State
=============

This is in the very early stages of development. There is a test.py file
that shows the current usage of the tools. This will be made into a more
comprehensive toolset. It will be available as:

* Pypi module install
* Standalone tools with binaries for Linux and Windows


The Current List of Work
========================

* More V8 Support
* Schema tools
* Query engine
* Connections
* SQLAlchemy integration
* DB Writes with index updates

More database examples

What is BTrieve?
================

BTrieve is an Indexed Sequential Access Method (ISAM) database. It was developed
by a company called SoftCraft in 1982 who were purchased by Novell in 1987.
They sold the product to BTrieve Technologies in 1994 who then renamed 
themselves in 1996 to Pervasive. In 2013 they were acquired by Actian.

These databases are a lot more common than most people realise and sometimes
companies don't even realise they have a BTrieve database because it is mostly
tightly embedded into whatever software they are managing. Searching for DDF
file extensions can sometimes yield unexpected results.

Pervasive later changed the technology for their RDBMS to be more akin to other
RDBMS technologies.

Where does this fit in?
=======================

This tool is targetted towards those poor souls who have applications where
the data has been stored in what they think is a proprietary database format
but is really stored in a BTrieve file.

The primary aim of this toolset is to help get the information out and into
something a bit more modern.

How do you know about this?
===========================

I've stumbled across the BTrieve database format several times in my travels
working on a variety of systems. My first work with the format actually involved
some technical work during the Novell years and actually managed to contribute
code to Novell's source code (some Novell network related code and also MU/CCPM 
process management code). This gave me some insight and contacts in the BTrieve
world.

SQLAlchemy
==========

URI Example: btrieve:///database_path

Like:

from sqlalchemy import create_engine
engine = create_engine("btrieve:///database_path")

or

engine = create_engine("btrieve:///database_path/field.ddf")

In case the field.ddf/file.ddf is called something different
