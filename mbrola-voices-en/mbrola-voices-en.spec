Name:       mbrola-voices-en
Version:    1
Release:    1%{?dist}
Summary:    English voices for the mbrola text-to-speech engine
License:    Freeware
URL:        http://www.tcts.fpms.ac.be/synthesis/mbrola/mbrcopybin.html
BuildArch:  noarch

Source0:    http://www.tcts.fpms.ac.be/synthesis/mbrola/dba/en1/en1-980910.zip
Source1:    http://www.tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
Source2:    http://www.tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
Source3:    http://www.tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip

Requires:   mbrola

%description
The Mbrola project is a collection of diphone voices for speech synthesis.
This package contains voice data for English voices en1, us1, us2 and us3.


%prep
%setup -q -c %{name} -T -a0 -a1 -a2 -a3


%install
rm -rf %{buildroot}
install -p -d -m 0755      %{buildroot}%{_datadir}/mbrola
install -p -m 0644 en1/en1 %{buildroot}%{_datadir}/mbrola
install -p -m 0644 us1/us1 %{buildroot}%{_datadir}/mbrola
install -p -m 0644 us2/us2 %{buildroot}%{_datadir}/mbrola
install -p -m 0644 us3/us3 %{buildroot}%{_datadir}/mbrola


%files
%{_datadir}/mbrola/en1
%{_datadir}/mbrola/us1
%{_datadir}/mbrola/us2
%{_datadir}/mbrola/us3


%changelog

* Fri Jan 20 2012 Craig Barnes <cr@igbarn.es> - 1-1
- Initial package.
