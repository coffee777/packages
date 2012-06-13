Packages
========

Additional packages for [Fedora] Linux


Building packages
-----------------

To build packages, use the command

    sudo make [package]...

Where `[package]` is the name of one or more `.spec` files. For example:

    sudo make jsmin pngquant tidy

If sucessful, all built [RPM] files will be copied to the current directory.

The Makefile knows how to set up a packaging environment, install build-time
dependencies, copy spec files and download sources. This is all automatic and
fairly robust.

Root priviledges are required to initialise the build process but these
priviledges are dropped and any downloaded build scripts are executed as the
dummy user `makerpm`. This means that the worst a rogue script can do is
read/write `/home/makerpm`. At *no* point does any downloaded script have root
access or even access to your own user account.

[Fedora]: http://fedoraproject.org/
[RPM]: http://www.rpm.org/
