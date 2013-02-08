Name:           hubbub
Version:        0.1.2
Release:        1%{?dist}
Summary:        HTML5 compliant parsing library, written in C
License:        MIT
URL:            http://www.netsurf-browser.org/projects/hubbub/
Source0:        http://download.netsurf-browser.org/libs/releases/hubbub-0.1.2-src.tar.gz

%description
Hubbub is an HTML5 compliant parsing library, written in C. It was developed
as part of the NetSurf project and is available for use by other software
under the MIT license.

The HTML5 specification defines a parsing algorithm, based on the behavior
of mainstream browsers, which provides instructions for how to parse all
markup, both valid and invalid. As a result, Hubbub parses web content well.


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
make %{?_smp_mflags} COMPONENT_TYPE=lib-shared


%install
%make_install COMPONENT_TYPE=lib-shared PREFIX=%{_prefix}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_libdir}/libhubbub.so.*


%files devel
%dir %{_includedir}/hubbub/
%{_includedir}/hubbub/*.h
%{_libdir}/libhubbub.so
%{_libdir}/pkgconfig/libhubbub.pc


%changelog

* Fri Feb 08 2013 Craig Barnes <cr@igbarn.es> - 0.1.2-1
- Initial package
