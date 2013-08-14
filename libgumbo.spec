%global     commit eec95fa853506bd6b0eee1d35f9f4f112add6ee9
%global     shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       libgumbo
Version:    0
Release:    1.git%{shortcommit}%{?dist}
Summary:    A C99 implementation of the HTML5 parsing algorithm
License:    ASL 2.0
URL:        https://github.com/google/gumbo-parser
Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

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
%configure --disable-static
make %{?_smp_mflags}


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

* Wed Aug 14 2013 Craig Barnes <cr@igbarn.es> - 0-1.giteec95fa
- Initial package
