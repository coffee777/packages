%global         commit 906a9a139a89f1a26ecd93e6447e9b38d274fa78
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           libsass
Version:        1
Release:        2%{?dist}
Summary:        A C++ implementation of the Sass CSS precompiler
License:        MIT
URL:            https://github.com/hcatlin/libsass
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original version
was written in Ruby, but this version is meant for efficiency and
portability.

This library strives to be light, simple, and easy to build and integrate
with a variety of platforms and languages.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libsass-%{commit}


%build
make %{?_smp_mflags} shared CFLAGS='%{optflags} -fPIC' \
                            LDFLAGS='-Wl,-soname,libsass.so.1'


%install
install -Dpm0755 libsass.so %{buildroot}%{_libdir}/libsass.so.1
ln -s libsass.so.1 %{buildroot}%{_libdir}/libsass.so
install -Dpm0644 sass_interface.h %{buildroot}%{_includedir}/sass_interface.h


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc COPYING LICENSE Readme.md
%{_libdir}/libsass.so.*


%files devel
%{_libdir}/libsass.so
%{_includedir}/sass_interface.h


%changelog

* Sat Mar 23 2013 Craig Barnes <cr@igbarn.es> - 1-2
- Update to latest git commit
- Conform to Fedora packaging guidelines for GitHub

* Sun Oct 14 2012 Craig Barnes <cr@igbarn.es> - 1-1
- Initial package
