%global         commit ade649abd2bd0d949a7e22baa4a7d8dff9a757f9
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           sassc
Version:        1
Release:        2%{?dist}
Summary:        Command line Sass compiler
License:        MIT
URL:            https://github.com/hcatlin/sassc
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  libsass-devel

%description
%{summary}.


%prep
%setup -qn sassc-%{commit}
# Fix sass_interface.h location
sed -ri '/^#include/s|libsass/(sass_interface.h)|\1|' sassc.c


%build
gcc %{optflags} -c -o sassc.o sassc.c
gcc %{optflags} -lstdc++ -lm -lsass -o sassc sassc.o


%install
install -Dpm0755 sassc %{buildroot}%{_bindir}/sassc
mkdir -p %{buildroot}%{_datadir}/sass
cp -r spec/bourbon %{buildroot}%{_datadir}/sass


%files
%doc Readme.md LICENSE
%{_bindir}/sassc
%dir %{_datadir}/sass/
%{_datadir}/sass/*


%changelog

* Mon Nov 19 2012 Craig Barnes <cr@igbarn.es> - 1-2
- Add Bourbon to package
- Add /usr/share/sass to sassc include path

* Sun Oct 14 2012 Craig Barnes <cr@igbarn.es> - 1-1
- Initial package
