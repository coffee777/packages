%global         gitcommit c744346
Name:           sundown
Version:        1
Release:        1.git%{gitcommit}%{?dist}
Summary:        Command-line tool for processing Markdown documents into HTML
License:        ISC
URL:            http://blog.vmarti.net/sundown/
Source0:        https://github.com/tanoku/sundown/tarball/%{gitcommit}
Patch0:         sundown-gcc47-flagfix.patch
Requires:       libsundown%{?_isa} = %{version}-%{release}

%description
Sundown is a Markdown to HTML conversion utility. It is distributed as part
of libsundown, a standards compliant, fast, secure Markdown processing
library.


%package -n libsundown
Summary: Standards compliant, fast, secure markdown processing library
%description -n libsundown
%{summary}.


%package -n libsundown-devel
Summary: Development files for libsundown
Requires: libsundown%{?_isa} = %{version}-%{release}
%description -n libsundown-devel
%{summary}.


%prep
%setup -q -n tanoku-sundown-%{gitcommit}
%patch0


%build
make %{?_smp_mflags} CFLAGS='%{optflags} -c -fPIC -Isrc -Ihtml'


%install
rm -rf %{buildroot}
install -Dpm0755 sundown %{buildroot}%{_bindir}/sundown
install -Dpm0755 libsundown.so.1 %{buildroot}%{_libdir}/libsundown.so.1
install -Dp libsundown.so %{buildroot}%{_libdir}/libsundown.so
install -dm0755 %{buildroot}%{_includedir}/libsundown/
install -pm0644 src/*.h html/*.h %{buildroot}%{_includedir}/libsundown/


%post -n libsundown -p /sbin/ldconfig
%postun -n libsundown -p /sbin/ldconfig


%files
%{_bindir}/sundown


%files -n libsundown
%doc README.markdown
%{_libdir}/libsundown.so.1


%files -n libsundown-devel
%{_libdir}/libsundown.so
%{_includedir}/libsundown/*.h


%changelog

* Wed Jun 06 2012 Craig Barnes <cr@igbarn.es> - 1-1.gitc744346
- Initial package
