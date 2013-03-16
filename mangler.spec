Name:           mangler
Version:        1.2.5
Release:        1%{?dist}
Summary:        VOIP client capable of connecting to Ventrilo 3.x servers
License:        GPLv3
URL:            http://www.mangler.org
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
BuildRequires:  gsm-devel
BuildRequires:  speex-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  espeak-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  dbus-glib-devel

%description
Mangler is an open source VOIP client capable of connecting to Ventrilo 3.x
servers. It is capable of performing almost all standard user functionality
found in a Windows Ventrilo client.

The project's motto is: "No one should use our software... ever". There are
completely open source alternatives to Ventrilo. Mumble is highly
recommended.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{a,la}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README COPYING* AUTHORS NEWS ChangeLog
%{_bindir}/mangler
%{_libdir}/libventrilo3.so*
%{_includedir}/ventrilo3.h
%{_datadir}/applications/mangler.desktop
%{_datadir}/pixmaps/mangler_logo.svg
%{_mandir}/man1/mangler.1*


%changelog

* Wed Mar 06 2013 Craig Barnes <cr@igbarn.es> - 1.2.5-1
- Initial package
