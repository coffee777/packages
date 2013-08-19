%global     commit 8872bccc4550540ae11f7f0400038c6398c228d7
%global     shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       libgumbo
Version:    0
Release:    3.git%{shortcommit}%{?dist}
Summary:    A C99 implementation of the HTML5 parsing algorithm
License:    ASL 2.0
URL:        https://github.com/google/gumbo-parser
Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: libtool autoconf automake
BuildRequires: gtest-devel

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a
pure C99 library with no outside dependencies. It's designed to serve as a
building block for other tools and libraries such as linters, validators,
templating languages and refactoring and analysis tools.


%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n gumbo-parser-%{commit}


%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}


%check
make check


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_mandir}/man3
install -pm0644 docs/man/man3/*.3 %{buildroot}%{_mandir}/man3


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README.md COPYING THANKS
%{_libdir}/libgumbo.so.*


%files devel
%{_includedir}/gumbo.h
%{_libdir}/libgumbo.so
%{_libdir}/pkgconfig/gumbo.pc
%{_mandir}/man3/*.3*


%changelog

* Mon Aug 19 2013 Craig Barnes <cr@igbarn.es> - 0-3.git8872bcc
- Update to git master
- Add gtest as a build dependency and run the test suite
- Add autotools dependencies (no release tarballs available yet)
- Run ./autogen.sh before ./configure

* Sat Aug 17 2013 Craig Barnes <cr@igbarn.es> - 0-2.git53cd3a4
- Update

* Wed Aug 14 2013 Craig Barnes <cr@igbarn.es> - 0-1.giteec95fa
- Initial package
