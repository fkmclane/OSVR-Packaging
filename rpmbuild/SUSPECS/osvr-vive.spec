Name: osvr-vive
Version: @VERSION@
Release: 1
Summary:  OSVR driver for use with the HTC Vive (including Vive PRE)

License: ASL 2.0
URL: OSVR driver for use with the HTC Vive (including Vive PRE)
Source0: osvr-vive-@VERSION@.tar.gz

BuildRequires: cmake

%description
This is a plugin for OSVR that provides access to the tracker data on HTC Vive HMDs and controllers. It also contains tools to extract a display descriptor with distortion mesh data from a Vive, as well as additional tools that build from source but are not installed into binary snapshots.


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
