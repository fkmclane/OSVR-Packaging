Name: osvr-tracker-viewer
Version: @VERSION@
Release: 1
Summary:  Utility for viewing OSVR tracking data, using OpenSceneGraph.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Tracker-Viewer
Source0: osvr-tracker-viewer-@VERSION@.tar.gz

BuildRequires: cmake

%description
Utility for viewing tracker (pose, position, orientation) data from the OSVR framework.


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
