Name: osvr-openhmd
Version: @VERSION@
Release: 1
Summary: OSVR plugin providing Oculus Rift DK1 & DK2 orientation tracking via OpenHMD

License: ASL 2.0
URL: https://github.com/simlrh/OSVR-OpenHMD
Source0: osvr-openhmd-@VERSION@.tar.gz

BuildRequires: cmake

%description
This is an OSVR plugin providing Oculus Rift DK1 & DK2 orientation tracking via OpenHMD. OpenHMD and hidapi are embedded so you don't need those libraries installed.


%prep
%autosetup


%build
%cmake .
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc LICENSE README.md NOTICE CONTRIBUTING.md

%changelog
* Tue Feb 28 2017 Joshua Forbes
-
