Name: osvr-oculus-rift
Version: @VERSION@
Release: 1
Summary: Oculus Rift tracking plugin for OSVR.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Oculus-Rift
Source0: osvr-oculus-rift-@VERSION@.tar.gz

BuildRequires: cmake

%description
This is a plugin for OSVR that provides access to Oculus Rift trackers from OSVR applications. It makes use of the Oculus VR SDK. This plugin currently supports Oculus VR SDK versions 0.4.4-beta through 1.13.0.


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
