Name:		nestopia
Version:	1.43
Release:	2

Summary:	A portable Nintendo Entertainment System emulator
License:	GPLv2+
Group:		Emulators
URL:		http://0ldsk00l.ca/nestopia.html
Source0:	https://github.com/downloads/rdanbrook/nestopia/nestopia-1.43.tgz
Patch0:		nestopia-1.43-makefile.patch

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)

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

%prep
%setup -q
%patch0 -p1

%build
%make

%install
# binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 nestopia %{buildroot}%{_bindir}/

# data files
install -d -m 755 %{buildroot}%{_datadir}/nestopia
install -m 644 NstDatabase.xml %{buildroot}%{_datadir}/nestopia/
install -d -m 755 %{buildroot}%{_datadir}/nestopia/icons
install -m 644 source/linux/icons/nespad.svg %{buildroot}%{_datadir}/nestopia/icons/

# icons
for N in 32 48 64 96 128;
do
install -D source/linux/icons/%{name}${N}.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

# xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-nestopia.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=NEStopia
Comment=%{summary}
Exec=nestopia
Icon=nestopia
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%doc README.linux
%{_bindir}/nestopia
%{_datadir}/nestopia
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-nestopia.desktop

