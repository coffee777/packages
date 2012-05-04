Name:           md2html
Version:        10
Release:        1%{?dist}
Summary:        Markdown to HTML conversion script
License:        BSD
URL:            http://www.anarchyinthetubes.com/src/md2html.awk/
BuildArch:      noarch
Source0:        %{url}md2html.10.awk
Requires:       gawk

%description
md2html is an AWK implementation of the Markdown language. It provides
a simple command-line utility that converts Markdown input into HTML.


%prep
cp %{SOURCE0} %{_builddir}


%install
rm -rf %{buildroot}
install -m 0755 -p -D md2html.10.awk %{buildroot}%{_bindir}/md2html


%files
%{_bindir}/md2html


%changelog

* Fri Dec 30 2011 Craig Barnes <cr@igbarn.es> - 10-1
- Initial package
