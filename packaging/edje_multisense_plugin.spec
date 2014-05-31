#sbs-git:slp/pkgs/e/edje_multisense_plugin
Name:       edje_multisense_plugin
Summary:    multisense plugin of edje
Version:    0.1.17b02
Release:    1
VCS:        magnolia/framework/uifw/edje_multisense_plugin#0.1.15-0-g9d2c5ca903a7d5cf3a3e1f6daeeff4fe1757b8b4
Group:      System/Libraries
License:    LGPLv2.1
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(mm-sound)
BuildRequires:  pkgconfig(remix)

%description
EDJE & libremix Plugins for TIZEN sound/tone play
Multise plugin for use with libedje
It includes sound, haptic, and vibration.

%prep
%setup -q

%build
cd %{_repository} && ./autogen.sh
make %{?jobs:-j%jobs}

%install
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi
cd %{_repository} && make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

%clean
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi
rm -f edje-multisense-plugin*.tar.bz2 edje-multisense-plugin-*.tar.bz2.cdbs-config_list

%files
%defattr(-,root,root,-)
%{_libdir}/remix/*
%manifest %{name}.manifest
/usr/share/license/%{name}
