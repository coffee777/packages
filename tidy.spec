%global         gitcommit 1b4dcd0
Name:           tidy
Version:        1
Release:        6.git%{gitcommit}%{?dist}
Summary:        Utility to clean, validate and pretty print HTML
Group:          Applications/Text
License:        W3C
URL:            https://github.com/w3c/tidy-html5
Source0:        %{url}/tarball/%{gitcommit}
Source1:        tidy-completion.bash
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
%make_install
install -Dpm0644 htmldoc/tidy.1 %{buildroot}%{_mandir}/man1/tidy.1
rm -f %{buildroot}%{_libdir}/libtidy.la %{buildroot}%{_bindir}/tab2space
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/tidy


%post   -n libtidy -p /sbin/ldconfig
%postun -n libtidy -p /sbin/ldconfig


%files
%doc README.md htmldoc/quickref.html
%{_bindir}/tidy
%{_mandir}/man1/tidy.1*
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/tidy


%files -n libtidy
%doc license.html
%{_libdir}/libtidy-0.99.so.0*


%files -n libtidy-devel
%doc htmldoc/api/*
%{_includedir}/*.h
%{_libdir}/libtidy.so


%changelog

* Thu Nov 15 2012 Craig Barnes <cr@igbarn.es> - 1-6.git1b4dcd0
- Add bash completion script

* Sun Jul 22 2012 Craig Barnes <cr@igbarn.es> - 1-5.git1b4dcd0
- Update to latest git master

* Fri Jul 06 2012 Craig Barnes <cr@igbarn.es> - 1-4.git79439b0
- Update to latest git master
- Drop workaround for autotools build (fixed upstream)

* Fri Jul 06 2012 Craig Barnes <cr@igbarn.es> - 1-3.gitd3440ed
- Update to latest git master
- Add temporary fix for upstream error in autotools build

* Tue Jun 05 2012 Craig Barnes <cr@igbarn.es> - 1-2.gitf212c3f
- Update to latest git master

* Mon Feb 27 2012 Craig Barnes <cr@igbarn.es> - 1-1.git9412ef6
- Initial package
