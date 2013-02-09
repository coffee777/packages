Name:           libtermkey
Version:        0.16
Release:        1%{?dist}
Summary:        A library that allows easy processing of terminal input
License:        MIT
URL:            http://www.leonerd.org.uk/code/libtermkey/
Source0:        %{url}%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognize special keys,
UTF-8 combining, and so on, with a simple interface.


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
make %{?_smp_mflags} LIBDIR='%{_libdir}'


%install
%make_install PREFIX='%{_prefix}' LIBDIR='%{_libdir}' \
              INCDIR='%{_includedir}' MANDIR='%{_mandir}'
rm -f %{buildroot}%{_libdir}/%{name}.a
rm -f %{buildroot}%{_libdir}/%{name}.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc LICENSE
%{_libdir}/libtermkey.so.*


%files devel
%{_includedir}/termkey.h
%{_mandir}/man?/termkey*
%{_libdir}/libtermkey.so
%{_libdir}/pkgconfig/termkey.pc


%changelog

* Sat Feb 09 2013 Craig Barnes <cr@igbarn.es> - 0.16-1
- Initial package
