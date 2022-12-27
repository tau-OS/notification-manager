%global extdir %{_datadir}/gnome-shell/extensions/notification-manager@tauos.co

Summary:        Allow adjustments of notification positioning
Name:           tau-notification-manager
# This should match the version in metadata.json
Version:        1
Release:        1.4%{dist}
License:        GPLv3+
URL:            http://tauos.co
Source0:        https://github.com/tau-OS/notification-manager/archive/refs/heads/main.zip
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

%description
Allow adjustments of notification positioning

%prep
%setup -q -n notification-manager-main

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
%{_datadir}/glib-2.0/schemas/*.xml

%changelog
* Mon May 16 2022 Lains <lainsce@airmail.cc> - 1-1.3
- Fix right position horizontally

* Sat May 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1.2
- Keep schema

* Fri May 13 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1.1
- Default notification on right

* Thu May 12 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1
- Initial Release
