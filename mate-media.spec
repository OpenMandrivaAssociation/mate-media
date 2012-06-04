%define major	0
%define	libname %mklibname mate-media-profiles %{major}
%define	devname %mklibname mate-media-profiles -d

Summary:	MATE media programs
Name:		mate-media
Version:	1.2.0
Release:	1
License:	GPLv2+ and GFDL+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires: docbook-dtd412-xml
BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: mate-conf
BuildRequires: xsltproc
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: pkgconfig(gladeui-1.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mateconf-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(mate-keybindings)
BuildRequires: pkgconfig(unique-1.0)

Requires:   gstreamer0.10-plugins-good
Requires:   gstreamer0.10-plugins-base
Suggests:   gstreamer0.10-flac
Suggests:   gstreamer0.10-speex
Requires(post,preun):	mate-conf

%description
This package contains a few media utilities for the MATE desktop,
including a sound recorder and an audio mixer.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
libraries for running MATE media.

%package -n %{devname}
Summary:	Development libraries, include files for MATE media
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Panel libraries and header files for MATE media.

%prep
%setup -q 
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper

%make

%install
MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}-2.0 --with-gnome --all-name

%files -f  %{name}-2.0.lang
%doc AUTHORS NEWS README
%{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas
%{_sysconfdir}/mateconf/schemas/mate-sound-recorder.schemas
%{_sysconfdir}/xdg/autostart/mate-volume-control-applet.desktop
%{_bindir}/*
%{_libdir}/glade3/modules/libmate-media-profiles.so
%{_datadir}/applications/mate-sound-recorder.desktop
%{_datadir}/mate-media
%{_datadir}/mate-sound-recorder
%{_datadir}/applications/mate-gstreamer-properties.desktop
%{_datadir}/applications/mate-volume-control.desktop
%{_datadir}/glade3/catalogs/mate-media-profiles.xml
%{_datadir}/mate-gstreamer-properties/gstreamer-properties.ui
%{_datadir}/mate-gstreamer-properties/icons/gstreamer-properties.png
%dir %{_datadir}/sounds/
%dir %{_datadir}/sounds/mate/
%{_datadir}/sounds/mate/default/
%{_iconsdir}/mate/48x48/apps/gstreamer-properties.png
%{_iconsdir}/hicolor/*/*/*.*
# mate help file
%{_datadir}/mate/help

%files -n %{libname}
%{_libdir}/libmate-media-profiles.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/mate-media
%dir %{_includedir}/mate-media/profiles
%{_includedir}/mate-media/profiles/*
%{_libdir}/libmate-media-profiles.so
%{_libdir}/pkgconfig/mate-media-profiles.pc

