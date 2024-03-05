%define major 0
%define libname %mklibname imagequant
%define devname %mklibname imagequant -d

Name:           libimagequant
Version:        2.18.0
Release:        1
Summary:        Palette quantization library
Group:          System/Libraries
License:        GPLv3+ and MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%description
Small, portable C library for high-quality conversion of RGBA images to 8-bit
indexed-color (palette) images.

%package -n %{libname}
Summary:        Palette quantization library
Group:          System/Libraries

%description -n %{libname}
Small, portable C library for high-quality conversion of RGBA images to 8-bit
indexed-color (palette) images.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       imagequant-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# fix libdir
sed -i -e '/libdir/s/lib$/%{_lib}/g' imagequant.pc.in

%build
%configure
%make_build

%install
%make_install

# Don't ship static library
rm -f %{buildroot}%{_libdir}/%{name}.a

%files -n %{libname}
%license COPYRIGHT
%doc README.md CHANGELOG
%{_libdir}/%{name}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/imagequant.pc
