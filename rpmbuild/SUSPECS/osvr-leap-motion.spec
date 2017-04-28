Name: osvr-leapmotion
Version: @VERSION@
Release: 1
Summary:OSVR Leap Motion plugin.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Leap-Motion
Source0: osvr-leap-motion-@VERSION@.tar.gz

BuildRequires: cmake

%description
OSVR Leap Motion plugin.


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
