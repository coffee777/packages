Name:           httpd
Epoch:          1
Version:        1
Release:        1%{?dist}
Summary:        Nginx high performance HTTP and reverse proxy server
License:        BSD
URL:            http://www.nginx.org/
BuildArch:      noarch
Requires:       nginx
Source0:        README

%description
Nginx [engine x] is a HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.

In the presence of this meta-package, all dependencies on
"httpd" will be satisfied by Nginx instead of the former default Apache.


%prep
cp %{SOURCE0} %{_builddir}


%files
%doc README


%changelog

* Thu Jan 02 2012 Craig Barnes <cr@igbarn.es> - 1:1-1
- Initial package
