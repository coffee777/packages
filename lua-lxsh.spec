%global         gitcommit ee16ce4
Name:           lua-lxsh
Version:        0.8.7
Release:        1%{?dist}
Summary:        Lexing and Syntax Highlighting in Lua
License:        MIT
URL:            http://peterodding.com/code/lua/lxsh/
BuildArch:      noarch
Source0:        https://github.com/xolox/lua-lxsh/tarball/%{version}
Requires:       lua = 5.1

%description

LXSH is a collection of lexers and syntax highlighters written in Lua using
the excellent pattern-matching library LPeg. Several syntaxes are currently
supported: Lua, C, BibTeX and shell script. The syntax highlighters support
three output formats: HTML, LaTeX and RTF.


%prep
%setup -q -n xolox-lua-lxsh-%{gitcommit}


%install
mkdir -p %{buildroot}%{_datadir}/lua/5.1
cp -r src %{buildroot}%{_datadir}/lua/5.1/lxsh


%files
%doc README.md
%dir %{_datadir}/lua/5.1/lxsh/
%dir %{_datadir}/lua/5.1/lxsh/*/
%{_datadir}/lua/5.1/lxsh/*.lua
%{_datadir}/lua/5.1/lxsh/*/*.lua


%changelog

* Thu Oct 18 2012 Craig Barnes <cr@igbarn.es> - 0.8.7-1
- Initial package
