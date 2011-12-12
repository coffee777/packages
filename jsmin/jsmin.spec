Name:           jsmin
Version:        2011.09.30
Release:        1%{?dist}
Summary:        Tool to remove comments and whitespace from JavaScript files
License:        Douglas Crockford's crazy, edgy license
URL:            http://www.crockford.com/javascript/jsmin.html

Source0:        https://raw.github.com/douglascrockford/JSMin/a9b4755/jsmin.c
Source1:        https://raw.github.com/douglascrockford/JSMin/a9b4755/README

%description
JSMin is a filter that removes comments and unnecessary whitespace from
JavaScript files. It typically reduces filesize by half, resulting in
faster downloads. It also encourages a more expressive programming style
because it eliminates the download cost of clean, literate self-documentation.


%prep
cp %{SOURCE0} %{SOURCE1} %{_builddir}


%build
cc -o jsmin jsmin.c


%install
rm -rf %{buildroot}
%{__install} -p -D -m 0755 jsmin %{buildroot}%{_sbindir}/jsmin


%files
%defattr(-,root,root,-)
%doc README
%{_sbindir}/jsmin


%changelog

* Tue Nov 15 2011 Craig Barnes <cr@igbarn.es> - 2011.09.30-1
- Initial package
