%define         gitcommit  f212c3f
Name:           tidy
Version:        1
Release:        2.git%{gitcommit}%{?dist}
Summary:        Utility to clean, validate and pretty print HTML
Group:          Applications/Text
License:        W3C
URL:            https://github.com/w3c/tidy-html5
Source0:        %{url}/tarball/%{gitcommit}
BuildRequires:  libtool
BuildRequires:  libxslt
Requires:       libtidy%{?_isa} = %{version}-%{release}

%description
HTML Tidy is a utility for cleaning, validating and formatting HTML
documents. It works great on the atrociously hard to read markup generated
by specialized HTML editors and conversion tools and can help you identify
where you need to pay further attention on making your pages more accessible
to people with disabilities.


%package        -n libtidy
Summary:        Shared libraries for tidy
%description    -n libtidy
%{summary}.


%package        -n libtidy-devel
Summary:        Development files for tidy
Requires:       libtidy%{?_isa} = %{version}-%{release}
%description    -n libtidy-devel
%{summary}.


%prep
%setup -q -n w3c-tidy-html5-%{gitcommit}
sh build/gnuauto/setup.sh


%build
%configure --disable-static --disable-dependency-tracking
make %{?_smp_mflags}
# Docs
pushd htmldoc
../console/tidy -xml-config > tidy-config.xml
../console/tidy -xml-help   > tidy-help.xml
xsltproc -o tidy.1 tidy1.xsl tidy-help.xml
xsltproc -o quickref.html quickref-html.xsl tidy-config.xml
popd


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -Dpm 644 htmldoc/tidy.1 %{buildroot}%{_mandir}/man1/tidy.1
rm -f %{buildroot}%{_libdir}/libtidy.la
rm -f %{buildroot}%{_bindir}/tab2space


%post   -n libtidy -p /sbin/ldconfig
%postun -n libtidy -p /sbin/ldconfig


%files
%doc README.md htmldoc/quickref.html
%{_bindir}/tidy
%{_mandir}/man1/tidy.1*


%files -n libtidy
%doc license.html
%{_libdir}/libtidy-0.99.so.0*


%files -n libtidy-devel
%doc htmldoc/api/*
%{_includedir}/*.h
%{_libdir}/libtidy.so


%changelog

* Tue Jun 05 2012 Craig Barnes <cr@igbarn.es> - 1-2.gitf212c3f
- Update to latest git master

* Mon Feb 27 2012 Craig Barnes <cr@igbarn.es> - 1-1.git9412ef6
- Initial package
