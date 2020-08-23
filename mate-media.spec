%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE media programs
Name:		mate-media
Version:	1.24.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libmatemixer)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-keybindings)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	yelp-tools

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a few media utilities for the MATE desktop, including
a volume control.

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_sysconfdir}/xdg/autostart/mate-volume-control-status-icon.desktop
%{_libexecdir}/mate-volume-control-applet
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-status-icon
%{_datadir}/mate-media
%{_datadir}/applications/mate-volume-control.desktop
%{_datadir}/dbus-1/services/org.mate.panel.applet.GvcAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.GvcApplet.mate-panel-applet
%dir %{_datadir}/sounds/
%dir %{_datadir}/sounds/mate/
%{_datadir}/sounds/mate/default/
%{_mandir}/man1/mate-volume-control.1*
%{_mandir}/man1/mate-volume-control-applet.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}/%{_sysconfdir}/xdg/autostart/mate-volume-control-status-icon.desktop
