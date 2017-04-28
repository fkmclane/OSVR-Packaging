Name: osvr-cpi
Version: @VERSION@
Release: 1
Summary: OSVR Control Panel Interface.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-CPI
Source0: osvr-cpi-@VERSION@.tar.gz

BuildRequires: cmake

%description
A simple QT based utility to help users set up their configuration parameters.


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
