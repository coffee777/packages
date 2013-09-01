%global     commit b4bf41ec41a830318b51de7f7464455eb576759d
%global     shortcommit %(c=%{commit}; echo ${c:0:7})
Name:       dex
Version:    0
Release:    4.git%{shortcommit}%{?dist}
Summary:    Small and easy to use text editor
License:    GPLv2
URL:        https://github.com/tihirvon/dex
Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
%{summary}.


%prep
%setup -qn dex-%{commit}


%build
cat > Config.mk << END
    CC      = gcc
    CFLAGS  = %{optflags}
    INSTALL = install -p
    prefix  = %{_prefix}
    bindir  = %{_bindir}
    datadir = %{_datadir}
    mandir  = %{_mandir}
END
make %{?_smp_mflags}


%install
%make_install


%files
%doc README FAQ COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_mandir}/man1/dex.1*
%{_mandir}/man7/dex-syntax.7*


%changelog

* Sun Sep 01 2013 Craig Barnes <cr@igbarn.es> - 0-4.gitb4bf41e
- Update

* Thu Aug 29 2013 Craig Barnes <cr@igbarn.es> - 0-3.git38c9ae5
- Generate a Config.mk file to configure build/installation options

* Wed Aug 28 2013 Craig Barnes <cr@igbarn.es> - 0-2.git38c9ae5
- Update

* Fri Aug 23 2013 Craig Barnes <cr@igbarn.es> - 0-1.gitcb8136f
- Initial package
