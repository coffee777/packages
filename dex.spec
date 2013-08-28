%global     commit 38c9ae5b4652ae28691803e11ae1ae2de568e6e7
%global     shortcommit %(c=%{commit}; echo ${c:0:7})
Name:       dex
Version:    0
Release:    2.git%{shortcommit}%{?dist}
Summary:    Small and easy to use text editor
License:    GPLv2
URL:        https://github.com/tihirvon/dex
Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
%{summary}.


%prep
%setup -qn dex-%{commit}


%build
make %{?_smp_mflags} CC='gcc' CFLAGS='%{optflags}'


%install
%make_install prefix=%{_prefix} \
              bindir=%{_bindir} \
              datadir=%{_datadir} \
              mandir=%{_mandir} \
              INSTALL='install -p'


%files
%doc README FAQ COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_mandir}/man1/dex.1*
%{_mandir}/man7/dex-syntax.7*


%changelog

* Wed Aug 28 2013 Craig Barnes <cr@igbarn.es> - 0-2.git38c9ae5
- Update

* Fri Aug 23 2013 Craig Barnes <cr@igbarn.es> - 0-1.gitcb8136f
- Initial package
