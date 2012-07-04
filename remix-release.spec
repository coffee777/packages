Name:           remix-release
Version:        0.0.1
Release:        1%{?dist}
Summary:        Fedora Remix release files
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        remix.repo

%description
Yum repository configurations for this Fedora Remix release.


%prep
cp %{SOURCE0} %{_builddir}


%install
install -Dpm644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/remix.repo


%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/remix.repo


%changelog

* Sun May 06 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package
