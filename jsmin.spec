%global         commit 49a70cf
Name:           jsmin
Version:        2012.07.02
Release:        1%{?dist}
Summary:        Tool to remove comments and whitespace from JavaScript files
License:        Douglas Crockford's crazy, edgy license
URL:            http://www.crockford.com/javascript/jsmin.html
Source0:        https://raw.github.com/douglascrockford/JSMin/%{commit}/jsmin.c
Source1:        https://raw.github.com/douglascrockford/JSMin/%{commit}/README

%description
JSMin is a filter that removes comments and unnecessary whitespace from
JavaScript files. It typically reduces filesize by half, resulting in
faster downloads. It also encourages a more expressive programming style
because it eliminates the download cost of clean, literate self-documentation.


%prep
cp %{SOURCE0} %{SOURCE1} %{_builddir}


%build
gcc %{optflags} -o jsmin jsmin.c


%install
install -Dpm0755 jsmin %{buildroot}%{_bindir}/jsmin


%files
%doc README
%{_bindir}/jsmin


%changelog

* Wed Jul 04 2012 Craig Barnes <cr@igbarn.es> - 2012.07.02-1
- Update to latest version
- Use "gcc" instead of "cc"
- Use optflags
- Install to bin directory instead of sbin directory
- Clean up install section
- Use global macro to specify git commit of specific version

* Tue Nov 15 2011 Craig Barnes <cr@igbarn.es> - 2011.09.30-1
- Initial package
