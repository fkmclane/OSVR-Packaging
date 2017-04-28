Name: libfunctionality
Version: @VERSION@
Release: 1
Summary: A minimal library for dynamically-loaded or statically linked functionality modules.

License: ASL 2.0
URL: http://github.com/OSVR/libfunctionality
Source0: libfunctionality-@VERSION@.tar.gz

BuildRequires: cmake

%description
A minimal library for dynamically-loaded or statically-linked functionality modules, which we call plugins. What you do with them and how you interact with them is your business. How you load them is ours. Designed to factor out the nitty-gritty of plugin loading, entry points, and dynamic loading vs. systems that only support static linking (like iOS).

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
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc LICENSE README.md NOTICE CONTRIBUTING.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/*.so


%changelog
* Tue Feb 28 2017 Joshua Forbes
-
