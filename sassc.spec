%global         gitcommit cbcaa8c
Name:           sassc
Version:        1
Release:        1%{?dist}
Summary:        Command line Sass compiler
License:        MIT
URL:            https://github.com/hcatlin/sassc
Source0:        %{url}/tarball/%{gitcommit}
BuildRequires:  libsass-devel >= 1-1
Requires:       libsass >= 1-1

%description
%{summary}.


%prep
%setup -q -n hcatlin-sassc-%{gitcommit}


%build
sed -ri '/^#include/s|libsass/(sass_interface.h)|\1|' sassc.c
gcc %{optflags} -c -o sassc.o sassc.c
gcc %{optflags} -lstdc++ -lm -lsass -o sassc sassc.o


%install
install -Dpm0755 sassc %{buildroot}%{_bindir}/sassc


%files
%doc Readme.md LICENSE
%{_bindir}/sassc


%changelog

* Sun Oct 14 2012 Craig Barnes <cr@igbarn.es> - 1-1
- Initial package
