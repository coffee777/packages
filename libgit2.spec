%global         commit 5b9fac39d8a76b9139667c26a63e6b3f204b3977
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           libgit2
Version:        0.17.0
Release:        1
Summary:        Portable, pure C implementation of the Git core methods
License:        GPLv2
Url:            http://libgit2.github.com/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  cmake pkgconfig openssl-devel

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.


%package devel
Summary: Development headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libgit2.


%prep
%setup -qn %{name}-%{commit}


%build
cmake . \
    -DCMAKE_C_FLAGS:STRING="%{optflags}" \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DINSTALL_LIB:PATH=%{_libdir}
make %{?_smp_mflags}


%install
%make_install


%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README.md
%{_libdir}/%{name}.so.*


%files devel
%doc CONVENTIONS
%{_libdir}/%{name}.so
%{_includedir}/git2*
%{_libdir}/pkgconfig/libgit2.pc


%changelog

* Thu Apr 04 2013 Craig Barnes <cr@igbarn.es> - 0.17.0-1
- Initial package
