%global         commit 046d736d25e8239a1ea659255f2da8e6d6aa037b
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         prerel rc2

# There's no debug info but rpmbuild attempts to generate a useless
# debug package anyway because it's not marked as noarch (see below)
%global         debug_package %{nil}

# Metalua currently pre-compiles bytecode that is only compatible with
# 32-bit, little endian platforms.
ExclusiveArch:  i686

Name:           metalua
Version:        0.5
Release:        1.%{prerel}%{?dist}
Summary:        Static meta-programming for Lua
License:        MIT
URL:            http://metalua.luaforge.net/
Source0:        https://github.com/fab13n/metalua/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Requires:       lua >= 5.1

%description
Metalua is a static meta-programming system for Lua: a set of tools
that let you alter the compilation process in arbitrary, powerful and
maintainable ways.


%prep
%setup -qn %{name}-%{commit}
# The LICENSE file contains "Tomás Guisasola", encoded in latin-1
# All packaged files should be in UTF-8
iconv -f LATIN1 -t UTF-8 LICENSE > LICENSE.UTF8
mv LICENSE.UTF8 LICENSE


%build
export BUILD=%{_builddir}/buildtmp
export INSTALL_BIN=%{buildroot}%{_bindir}
# Platform-independant code should usually go in _datadir (not _libdir) but
# pre-generated metalua bytecode is currently 32-bit, little endian only
export INSTALL_LIB=%{buildroot}%{_libdir}/%{name}
cd src && ./make.sh


%install
sed -i 's|^METALUA_LIB=.*|METALUA_LIB=%{_libdir}/%{name}|' src/make-install.sh
cd src && ./make-install.sh


%files
%doc LICENSE README.TXT
%{_bindir}/metalua
%dir %{_libdir}/metalua
%{_libdir}/metalua/*


%changelog

* Thu Jan 17 2013 Craig Barnes <cr@igbarn.es> - 0.5-1.rc2
- Initial package
