%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE media programs
Name:		mate-media
Version:	1.18.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libmatemixer)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mate-keybindings)
BuildRequires:	pkgconfig(unique-3.0)

%description
This package contains a few media utilities for the MATE desktop,
including a sound recorder and an audio mixer.

%prep
%setup -q 
%apply_patches

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files -f  %{name}.lang
%doc AUTHORS NEWS README
%{_sysconfdir}/xdg/autostart/mate-volume-control-applet.desktop
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-applet
%{_datadir}/mate-media
%{_datadir}/applications/mate-volume-control.desktop
%dir %{_datadir}/sounds/
%dir %{_datadir}/sounds/mate/
%{_datadir}/sounds/mate/default/
%{_mandir}/man1/mate-volume-control.1*
%{_mandir}/man1/mate-volume-control-applet.1*

