%global optflags %{optflags} -Wno-c++11-narrowing

Summary:	A portable Nintendo Entertainment System emulator
Name:		nestopia
Version:	1.52.1
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		https://0ldsk00l.ca/nestopia.html
Source0:	https://github.com/0ldsk00l/nestopia/archive/refs/tags/%{version}.tar.gz

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(fontconfig)

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	autoconf-archive
BuildRequires:	libtool

%description
NEStopia is a portable Nintendo Entertainment System emulator written in C++ 
by Martin Freij and ported to Linux by R. Belmont.

NEStopia strives for the most accurate emulation possible at the 
pixel-by-pixel and sample-by-sample level, and it has excellent mapper 
and UNIF board support as well.

A few features:
- Supports .nes, .unf/.unif, and XML format ROMs, including Vs. and 
 Playchoice 10 games
- Supports .fds discs (a file named diskrom.sys is needed for this feature)
- Supports .nsf music rips
- All supported files can be extracted from zip or 7zip containers (an 
 archive browser is not yet included - this assumes the common GoodSet case 
 of one zip or 7zip per game)
- Supports save states
- Supports movie recordings
- Supports the “rewinder” - if you make a bad jump and screw up your 
 game, press Backspace and the game will run in reverse. Press \ to take over 
 again and try to fix your mistake.
- Friendly GUI configuration
- Autodetection of PAL and NTSC format games
- Supports drag and drop of compatible games and music rips from modern Linux 
 file managers, including KDE’s Konqueror and GNOME’s Nautilus.

%files
%{_bindir}/nestopia
%{_datadir}/nestopia
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/nestopia.desktop
%doc %{_docdir}/nestopia

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install
