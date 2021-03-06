Name: osvr-display
Version: @VERSION@
Release: 1
Summary: Cross-platform detection and configuration of displays

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Display
Source0: osvr-display-@VERSION@.tar.gz

BuildRequires: cmake

%description
 Provides cross-platform functions for enumerating displays and detecting and changing their settings.


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
