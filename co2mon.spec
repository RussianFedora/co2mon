%global gitcommit_full 6a53ffa3c69418d999178e0ba0dddf01b043173f
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20190313

Name:           co2mon
Version:        2.1.1
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        CO2 monitor software

License:        GPLv3+
URL:            https://github.com/dmage/co2mon
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

Requires:       udev

%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for USB CO2 Monitor devices.

%prep
%autosetup -n dmage-%{name}-%{gitcommit}


%build
mkdir build
pushd build
    %cmake ..
    %make_build
popd


%install
pushd build
    %make_install
popd

mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 644 udevrules/99-%{name}.rules %{buildroot}%{_udevrulesdir}

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r graph %{buildroot}%{_datadir}/%{name}/


%files
%doc README.md
%license LICENSE
%{_bindir}/co2mond
%{_datadir}/%{name}
%{_libdir}/*.so.1*
%{_udevrulesdir}/99-%{name}.rules

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
* Fri Jun 14 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.1-1.20190313git6a53ffa
- Clean spec

* Tue Jun 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-0.20190313git6a53ffa.1
- Update to latest git

* Fri Jul 20 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-0.20180527git664378b
- Update to latest git

* Wed Apr 13 2016 vascom <vascom2@gmail.com> 2.1.0-2
- Add udev post script

* Wed Nov 11 2015 vascom <vascom2@gmail.com> 2.1.0-1
- Update to 2.1.0
- Added udev rule

* Sun Nov 08 2015 vascom <vascom2@gmail.com> 2.0.2-1
- First package release
