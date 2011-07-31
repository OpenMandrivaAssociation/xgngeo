%define name xgngeo
%define longname XGngeo
%define version 16
%define rel 2
%define release %mkrel %{rel}

Summary: %{longname} - NeoGeo Emulator Front-End
Name: %{name}
Version: %{version}
Release: %{release}
BuildRequires: pygtk2.0-devel
BuildRequires: desktop-file-utils
Requires: pygtk2.0
Requires: gngeo
Source0: %{longname}-%{version}.tar.bz2
Source1: %{name}-16.png
Source2: %{name}-32.png
Source3: %{name}-48.png
Patch0: %{name}-%{version}-install-and-paths.patch
Group: Emulators
License: GPLv2
URL: http://www.choplair.org/?XGngeo
#or http://choplair.org/?fr/XGngeo
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
XGngeo is a front-end for GnGeo, a NeoGeo emulator for Linux.
It uses PyGTK as the GUI toolkit.

%prep
%setup -q -n %{longname}-%{version}
%patch0 -p1

%build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --add-category="Emulator" \
 --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
 --dir %{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/applications/*

#icons
install -D -m 644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES.txt README.txt doc/xgngeo-doc.pdf doc/xgngeo-doc.txt
%{_bindir}/%{name}
%dir %{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}/*.py
%{py_puresitedir}/XGngeo-16-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif

