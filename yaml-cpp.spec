Name:               yaml-cpp
Version:            0.6.3
Release:            1
Summary:            A YAML parser and emitter in C++.
License:            MIT
URL:                https://github.com/jbeder/yaml-cpp
Source0:            https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz
Patch2:             CVE-2017-5950.patch
BuildRequires:      cmake gcc gcc-c++

%description
yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.

%package            devel
Summary:            Development files for yaml-cpp
Requires:           yaml-cpp = %{version}-%{release} boost-devel pkgconfig
Provides:           yaml-cpp-static = %{version}-%{release}
Obsoletes:          yaml-cpp-static < %{version}-%{release}

%description        devel
This package contains libraries and header files for developing applications that use yaml-cpp.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%build
rm -rf build_*
mkdir build_dynamic_lib
mkdir build_static_lib
cd build_dynamic_lib
%cmake -DYAML_BUILD_SHARED_LIBS=ON -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF ../
%make_build

cd ../build_static_lib
%cmake -DYAML_BUILD_SHARED_LIBS=OFF -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF ../
%make_build
cd -

%install
cd build_dynamic_lib
%make_install
mv %{buildroot}%{_libdir}/cmake/yaml-cpp %{buildroot}%{_libdir}/cmake/yaml-cpp-dynamic
mv %{buildroot}%{_libdir}/pkgconfig/yaml-cpp.pc %{buildroot}%{_libdir}/pkgconfig/yaml-cpp-dynamic.pc

cd ../build_static_lib
%make_install
mv %{buildroot}%{_libdir}/cmake/yaml-cpp %{buildroot}%{_libdir}/cmake/yaml-cpp-static
mv %{buildroot}%{_libdir}/pkgconfig/yaml-cpp.pc %{buildroot}%{_libdir}/pkgconfig/yaml-cpp-static.pc
cd -

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/yaml-cpp/
%{_libdir}/cmake/
%{_libdir}/pkgconfig/


%changelog
* Mon Jan 6 2020 Senlin Xia<xiasenlin1@huawei.com> - 0.6.3-1
- Package init
