Name:           lunamark
Version:        0.2
Release:        1%{?dist}
Summary:        General markup format converter using Lua lpeg
License:        MIT
URL:            http://jgm.github.com/lunamark
BuildArch:      noarch

Source0:        https://github.com/jgm/lunamark/tarball/%{version}

Requires:       lua >= 5.1
Requires:       lua-lpeg >= 0.10
Requires:       lua-cosmo >= 10.0
Requires:       lua-unicode >= 1.1
Requires:       lua-alt-getopt >= 0.7
Requires:       lua-bit32

%description
Lunamark is a lua library and command-line program for conversion of
markdown to other textual formats. Currently HTML, Docbook, ConTeXt, LaTeX,
dzslides, and Groff man are the supported output formats, but it is easy to
add new writers or modify existing ones. The markdown parser is written
using a PEG grammar and can also be modified by the user.


%prep
%setup -q -n jgm-lunamark-c17d0da


%install
rm -rf %{buildroot}
install -dm755 %{buildroot}%{_datadir}/lua/5.1/
cp -rf lunamark %{buildroot}%{_datadir}/lua/5.1/
cp lunamark.lua %{buildroot}%{_datadir}/lua/5.1/
install -Dpm755 bin/lunamark %{buildroot}%{_bindir}/lunamark
install -Dpm755 bin/lunadoc %{buildroot}%{_bindir}/lunadoc


%files
%doc LICENSE README.markdown
%dir %{_datadir}/lua/5.1/lunamark/
%{_datadir}/lua/5.1/lunamark/*
%{_datadir}/lua/5.1/lunamark.lua
%{_bindir}/lunamark
%{_bindir}/lunadoc


%changelog

* Mon Mar 12 2012 Craig Barnes <cr@igbarn.es> - 0.2-1
- Initial package
