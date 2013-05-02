Name:           libparserutils
Version:        0.1.2
Release:        1%{?dist}
Summary:        A library for building efficient parsers, written in C
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libparserutils/
Source0:        http://download.netsurf-browser.org/libs/releases/libparserutils-%{version}-src.tar.gz
BuildRequires:  netsurf-buildsystem >= 1.0

%description
LibParserUtils is a library for building efficient parsers, written in C. It
was developed as part of the NetSurf project and is available for use by
other software under the MIT license.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
export CFLAGS='%{optflags}'
make %{?_smp_mflags} COMPONENT_TYPE=lib-shared PREFIX=%{_prefix}


%install
%make_install COMPONENT_TYPE=lib-shared PREFIX=%{_prefix}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_libdir}/libparserutils.so.*


%files devel
%dir %{_includedir}/parserutils/
%{_includedir}/parserutils/*
%{_libdir}/libparserutils.so
%{_libdir}/pkgconfig/libparserutils.pc


%changelog

* Thu May 02 2013 Craig Barnes <cr@igbarn.es> - 0.1.2-1
- Update to latest release

* Fri Feb 08 2013 Craig Barnes <cr@igbarn.es> - 0.1.1-1
- Initial package
