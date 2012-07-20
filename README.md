Packages
========
Some extra, unofficial packages for [Fedora](http://fedoraproject.org/).

Building packages
-----------------

To build packages, use the command:

    sudo make [package]...

Where `[package]` is the name of one or more `.spec` files. For example:

    sudo make jsmin pngquant tidy

If sucessful, all built `.rpm` files will be copied to the current directory.

You can also use `make help` to show a list valid targets.

The Makefile knows how to set up a packaging environment, install build-time
dependencies, copy spec files and download sources. This is all automatic and
fairly robust.

Root priviledges are required to initialise the build process but these
priviledges are dropped and any downloaded build scripts are executed as the
dummy user `makerpm`. This means that the worst a rogue script can do is
read/write `/home/makerpm`. At *no* point does a downloaded script have root
access or access to your account.
