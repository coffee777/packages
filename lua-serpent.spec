%global         gitcommit e72ca38
Name:           lua-serpent
Version:        1
Release:        1.git%{gitcommit}%{?dist}
Summary:        Lua serializer and pretty printer
License:        MIT
BuildArch:      noarch
URL:            https://github.com/pkulchenko/serpent
Source0:        %{url}/tarball/%{gitcommit}
Requires:       lua >= 5.1

%description
%{summary}.


%prep
%setup -q -n pkulchenko-serpent-%{gitcommit}


%install
install -Dpm0644 src/serpent.lua %{buildroot}%{_datadir}/lua/5.1/serpent.lua


%files
%doc README.md LICENSE
%{_datadir}/lua/5.1/serpent.lua


%changelog

* Mon Oct 01 2012 Craig Barnes <cr@igbarn.es> - 1-1.gite72ca38
- Initial package
