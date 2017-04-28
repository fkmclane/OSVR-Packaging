Name: libuvc
Version: @VERSION@
Release: 1
Summary: A cross-platform library for USB video devices

License: BSD
URL: https://int80k.com/libuvc/doc
Source0: libuvc-@VERSION@.tar.gz

BuildRequires: cmake libusbx-devel
Requires: libusbx

%description
libuvc is a library that supports enumeration, control and streaming for USB Video Class (UVC) devices, such as consumer webcams

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake .
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT${_libdir}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE.txt
%doc LICENSE.txt README.md changelog.txt
%{_libdir}/*.so

%files devel
%{_includedir}/*
%{_libdir}/cmake/*


%changelog
* Mon Apr 17 2017 Joshua Forbes
-
