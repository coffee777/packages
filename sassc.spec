%global         gitcommit 57f687d
Name:           sassc
Version:        1
Release:        2%{?dist}
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
# Fix sass_interface.h location
sed -ri '/^#include/s|libsass/(sass_interface.h)|\1|' sassc.c
# Add /usr/share/sass to default sassc include path
sed -i '/^\s*ctx->options.include_paths = "";$/s|""|"%{_datadir}/sass"|' sassc.c


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
