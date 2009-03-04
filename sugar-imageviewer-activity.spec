# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-imageviewer-activity
Version: 6
Release: %mkrel 1
Summary: Image viewer activity for Sugar
License: GPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/ImageViewer/ImageViewer-6.tar.bz2

Requires: sugar-toolkit >= 0.84.0

BuildRequires: gettext  
BuildRequires: sugar-toolkit >= 0.84.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Image viewer activity for Sugar.

%prep
%setup -q -n ImageViewer-6


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.ImageViewerActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.ImageViewerActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING NEWS

