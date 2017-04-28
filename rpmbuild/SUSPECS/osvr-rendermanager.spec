Name: osvr-rendermanager
Version: @VERSION@
Release: 1
Summary:  API for rendering and presenting graphics for virtual reality.

License: ASL 2.0
URL: https://github.com/sensics/OSVR-RenderManager.git
Source0: osvr-rendermanager-@VERSION@.tar.gz

BuildRequires: cmake

%description
RenderManager is an API for rendering and presenting graphics for virtual reality. There is a detailed description below, but in short, it is a codebase that contains:
- Rendering code that performs time-warp, distortion correction, (per-eye) client-side prediction, for multiple graphics APIs
- Distortion mesh creation from a variety of distortion descriptions
- An output backend for rendering in extended or direct mode on a range of platforms and drivers


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
