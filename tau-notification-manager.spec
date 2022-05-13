%global extdir %{_datadir}/gnome-shell/extensions/notification-manager@tauos.co

Summary:        Allow adjustments of notification positioning
Name:           tau-notification-manager
# This should match the version in metadata.json
Version:        1
Release:        1
License:        GPLv3+
URL:            http://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

%description
Allow adjustments of notification positioning

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,schemas}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{extdir}

%changelog
* Thu May 12 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1
- Initial Release