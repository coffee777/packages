%global HOST http://aarnet.dl.sourceforge.net/project/corefonts/the%20fonts/final

Name:           ms-core-fonts
Summary:        Microsoft TrueType core fonts for the Web
Version:        3
Release:        1
URL:            http://www.microsoft.com/typography/faq/faq8.htm
License:        http://www.microsoft.com/typography/fontpack/eula.htm
BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  cabextract
Source0:        %HOST/andale32.exe
Source1:        %HOST/arial32.exe
Source2:        %HOST/arialb32.exe
Source3:        %HOST/comic32.exe
Source4:        %HOST/courie32.exe
Source5:        %HOST/georgi32.exe
Source6:        %HOST/impact32.exe
Source7:        %HOST/times32.exe
Source8:        %HOST/trebuc32.exe
Source9:        %HOST/webdin32.exe
Source10:       %HOST/verdan32.exe
Source11:       %HOST/wd97vwr32.exe

%description
The Microsoft "TrueType core fonts for the web", which were once
available for download.


%build
for FILE in %{sources}; do cabextract -Ldtmp $FILE; done
chmod 0644 tmp/*
cabextract -Ldtmp tmp/viewer1.cab


%install
install -dm0755 %{buildroot}%{_fontdir}
install -pm0644 tmp/*.ttf %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}
mkfontscale %{buildroot}%{_fontdir}


%_font_pkg *.ttf fonts.dir fonts.scale


%changelog

* Sun Sep 16 2012 Craig Barnes <cr@igbarn.es> - 3-1
- Initial package
