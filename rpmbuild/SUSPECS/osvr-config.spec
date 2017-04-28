Name: osvr-config
Version: @VERSION@
Release: 1
Summary: Configuration utility for the OSVR Server.

License: ASL 2.0
URL: https://github.com/OSVR/OSVR-Config
Source0: osvr-config-@VERSION@.tar.gz

BuildRequires: cmake

%description
OSVR-Config is a utility to configure the OSVR Server, and gives you access to a few OSVR-related tools.


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
