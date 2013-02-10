%global         commit 2a943dba6bae746075749499b1da7955474a47b1
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           jsmin
Version:        2012.12.04
Release:        1%{?dist}
Summary:        Tool to remove comments and whitespace from JavaScript files
License:        Douglas Crockford's crazy, edgy license
URL:            http://www.crockford.com/javascript/jsmin.html
Source0:        https://github.com/douglascrockford/JSMin/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
JSMin is a filter that removes comments and unnecessary whitespace from
JavaScript files. It typically reduces filesize by half, resulting in
faster downloads. It also encourages a more expressive programming style
because it eliminates the download cost of clean, literate self-documentation.


%prep
%setup -qn JSMin-%{commit}


%build
gcc %{optflags} -o jsmin jsmin.c


%install
install -Dpm0755 jsmin %{buildroot}%{_bindir}/jsmin


%files
%doc README
%{_bindir}/jsmin


%changelog

* Sun Feb 10 2013 Craig Barnes <cr@igbarn.es> - 2012.12.04-1
- Update to commit 2a943db
- Conform to Fedora packaging guidelines for GitHub

* Wed Jul 04 2012 Craig Barnes <cr@igbarn.es> - 2012.07.02-1
- Update to commit 49a70cf
- Use "gcc" instead of "cc"
- Use optflags
- Install to bin directory instead of sbin directory
- Clean up install section
- Use global macro to specify git commit

* Tue Nov 15 2011 Craig Barnes <cr@igbarn.es> - 2011.09.30-1
- Initial package
