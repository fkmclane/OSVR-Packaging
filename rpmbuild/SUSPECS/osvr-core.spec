Name: osvr-core
Version: @VERSION@
Release: 1
Summary: The core libraries, applications, and plugins of the OSVR software platform.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Core
Source0: osvr-core-@VERSION@.tar.gz

BuildRequires: cmake

%description
This is the code and libraries to use when developing with OSVR.

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
