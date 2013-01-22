Summary:	Enlightenment Foundation Library
Name:		evas
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	2ddc24ac1b3f5459553c8241586286a1
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eet-devel
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel
BuildRequires:	giflib-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/evas

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects and much more.

%package devel
Summary:	Header files for evas library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for evas library.

%package modules
Summary:	Engines, loaders and savers modules
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description modules
Engines, loaders and savers modules.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static		\
	--disable-wayland-egl		\
	--disable-wayland-shm		\
%ifarch %{ix86}
	--enable-cpu-sse3=no		\
%endif
	--enable-buffer
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -name *.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libevas.so.1
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevas.so
%{_includedir}/evas-1
%{_pkgconfigdir}/evas*.pc

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evas_cserve2_client
%attr(755,root,root) %{_bindir}/evas_cserve2_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_usage

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/dummy_slave
%attr(755,root,root) %{_libexecdir}/evas_cserve2
%attr(755,root,root) %{_libexecdir}/evas_cserve2_slave

%dir %{_libdir}/evas
%dir %{_libdir}/evas/cserve2
%dir %{_libdir}/evas/cserve2/loaders
%dir %{_libdir}/evas/cserve2/loaders/*
%dir %{_libdir}/evas/cserve2/loaders/*/linux-gnu-*
%dir %{_libdir}/evas/modules
%dir %{_libdir}/evas/modules/engines
%dir %{_libdir}/evas/modules/engines/*
%dir %{_libdir}/evas/modules/engines/*/linux-gnu-*
%dir %{_libdir}/evas/modules/loaders
%dir %{_libdir}/evas/modules/loaders/*
%dir %{_libdir}/evas/modules/loaders/*/linux-gnu-*
%dir %{_libdir}/evas/modules/savers
%dir %{_libdir}/evas/modules/savers/*
%dir %{_libdir}/evas/modules/savers/*/linux-gnu-*

%attr(755,root,root) %{_libdir}/evas/cserve2/loaders/*/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/evas/modules/engines/*/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/evas/modules/loaders/*/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/evas/modules/savers/*/linux-gnu-*/module.so


