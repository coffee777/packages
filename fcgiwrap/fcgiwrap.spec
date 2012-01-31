%define gitcommit       1328862

Name:           fcgiwrap
Version:        1.0.3
Release:        1.git%{gitcommit}%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            http://nginx.localdomain.pl/
Source0:        https://github.com/gnosek/fcgiwrap/tarball/%{gitcommit}

BuildRequires:  autoconf
BuildRequires:  fcgi-devel
Requires:       spawn-fcgi

%description
fcgiwrap is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other web servers
that may need it).


%prep
%setup -q -n gnosek-fcgiwrap-%{gitcommit}


%build
autoreconf -i
%configure
# Bug: prefix erroneously added to absolute sbindir resulting in /usr/usr/sbin
sed -i '1,2s|/usr/usr|/usr|g' Makefile
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*


%changelog

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
