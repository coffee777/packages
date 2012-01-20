Name:           mbrola
Version:        301
Release:        1%{?dist}
Summary:        A collection of diphone voices for speech synthesis
License:        Freeware
URL:            http://tcts.fpms.ac.be/synthesis/
BuildArch:      i386

Source0:        http://www.tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr301h.zip

%description
The Mbrola project is a collection of diphone voices for speech synthesis.
They do not include any text-to-phoneme translation, so this must be
done by another program. The Mbrola voices are cost-free but are not
open source.

This package contains the mbrola program, which all of the
mbrola-voice data packages require to function.


%prep
%setup -q -c %{name}-%{version}


%install
rm -rf %{buildroot}
install -p -D -m 0644 mbrola-linux-i386 %{buildroot}%{_bindir}/mbrola


%files
%doc readme.txt
%{_bindir}/mbrola


%changelog

* Fri Jan 20 2012 Craig Barnes <cr@igbarn.es> - 301-1
- Initial package.
