Name:           httpd
Epoch:          10
Version:        10
Release:        1%{?dist}
Summary:        Nginx high performance HTTP and reverse proxy server
License:        BSD
URL:            http://www.nginx.org/
BuildArch:      noarch
Provides:       httpd-mmn webserver
Obsoletes:      httpd-mmn
Requires:       nginx

%description
In the presence of this meta-package, all dependencies on "httpd" will be
satisfied by Nginx instead of Apache.


%build
echo '%{description}' > README


%files
%doc README


%changelog

* Fri Aug 24 2012 Craig Barnes <cr@igbarn.es> - 10:10-1
- Add "httpd-mmn" to "Obsoletes:" to prevent pulling in Apache
- Add "httpd-mmn" and "webserver" to "Provides:" to satify PHP dependencies
- Simplify description
- Use description to generate README instead of using external sources
- Bump epoch and version to 10 to avoid any later surprises

* Thu Jan 02 2012 Craig Barnes <cr@igbarn.es> - 1:1-1
- Initial package
