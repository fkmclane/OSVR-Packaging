Name: osvr-steamvr
Version: @VERSION@
Release: 1
Summary:  An OSVR plugin for SteamVR, providing SteamVR support for OSVR HMDs.

License: ASL 2.0
URL: https://github.com/OSVR/SteamVR-OSVR
Source0: osvr-steamvr-@VERSION@.tar.gz

BuildRequires: cmake

%description
This is a SteamVR driver for allowing applications written against that API to work with hardware and software running with the OSVR software framework.


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
