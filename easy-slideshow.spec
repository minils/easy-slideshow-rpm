Name:                    easy-slideshow
Version:                 0.4.5
Release:                 1%{?dist}
Summary:                 Simple slideshow displaying images randomly

License:                 GPLv3
URL:                     https://github.com/minils/easy-slideshow
Source0:                 https://github.com/minils/%{name}/archive/v%{version}.tar.gz

BuildRequires:           qt5-qtbase-devel
BuildRequires:           qt5-rpm-macros
BuildRequires:           libexif-devel
Requires:                libexif
Requires:                qt5-qtbase
ExcludeArch:             noarch

%description
Slideshow that displays the images of multiple folders in a randomized order. 

%global debug_package %{nil}

%prep
%autosetup

%build
CONFIG=release qmake-qt5 .
make

%install
INSTALL_ROOT="%{buildroot}" make install

%files
%{_bindir}/easyslideshow
%{_datadir}/applications/easyslideshow.desktop
%{_datadir}/icons/hicolor/scalable/apps/easyslideshow.svg

%changelog
* Fri Jun 19 2020 Nils Schwabe <nils@schwabe.ws> - 0.4.5-1
 - Initial package  
