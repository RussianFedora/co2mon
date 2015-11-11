Name:           co2mon
Version:        2.1.0
Release:        1%{?dist}
Summary:        CO2 monitor software

License:        GPLv3+
URL:            https://github.com/dmage/co2mon
Source0:        https://github.com/dmage/co2mon/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel

%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for USB CO2 Monitor devices.

%prep
%setup -q


%build
mkdir build
cd build
%cmake ..
%make_build


%install
cd build
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p %{buildroot}%{_udevrulesdir}
%{__install} -p -m 644 ../udevrules/99-co2mon.rules %{buildroot}%{_udevrulesdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/co2mond
%{_libdir}/*.so.*
%{_udevrulesdir}/99-co2mon.rules

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
* Wed Nov 11 2015 vascom <vascom2@gmail.com> 2.1.0-1
- Update to 2.1.0
- Added udev rule

* Sun Nov 08 2015 vascom <vascom2@gmail.com> 2.0.2-1
- First package release
