%global         commit ee16ce4903616030a26c15c4f8ce2222434f0ade
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           lua-lxsh
Version:        0.8.7
Release:        2%{?dist}
Summary:        Lexing and Syntax Highlighting in Lua
License:        MIT
URL:            http://peterodding.com/code/lua/lxsh/
BuildArch:      noarch
Source0:        https://github.com/xolox/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Requires:       lua = 5.1

%description

LXSH is a collection of lexers and syntax highlighters written in Lua using
the excellent pattern-matching library LPeg. Several syntaxes are currently
supported: Lua, C, BibTeX and shell script. The syntax highlighters support
three output formats: HTML, LaTeX and RTF.


%prep
%setup -qn %{name}-%{commit}


%install
mkdir -p %{buildroot}%{_datadir}/lua/5.1
cp -r src %{buildroot}%{_datadir}/lua/5.1/lxsh
install -Dpm0755 etc/lxsh %{buildroot}%{_bindir}/lxsh


%files
%doc README.md
%dir %{_datadir}/lua/5.1/lxsh/
%dir %{_datadir}/lua/5.1/lxsh/*/
%{_datadir}/lua/5.1/lxsh/*.lua
%{_datadir}/lua/5.1/lxsh/*/*.lua
%{_bindir}/lxsh


%changelog

* Fri Jan 11 2013 Craig Barnes <cr@igbarn.es> - 0.8.7-2
- Conform to Fedora packaging guidelines for archives from GitHub
- Install etc/lxsh to _bindir (wasn't installed at all before)

* Thu Oct 18 2012 Craig Barnes <cr@igbarn.es> - 0.8.7-1
- Initial package
