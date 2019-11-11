%global _el_version rtcs_el6
%global _el_sub .buildsys

Name:       chainbuild-test
Summary:    Macros for the Buildsystem
Version:    1
Release:    0
License:    GPL
Group:      Development/Buildsystem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%description
This particular package contains the macros needed for the buildsys for TTC el6.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/rpm/
VERSION=%{version}
printf %s%b "%" "rhel 6\n" >> %{buildroot}/etc/rpm/test
printf %s%b "%" "dist .rtcs_el6\n" >> %{buildroot}/etc/rpm/test
printf %s%b "%" "rtcs_el6 7\n" >> %{buildroot}/etc/rpm/test

%files
%defattr(-,root,root,-)
/etc/rpm/test
%clean
rm -rf %{buildroot}


%changelog
* Thu Oct 31 2019 Craig Swearingen <craig.swearingen@forcepoint.com>
- Initial variables for koji mock build of ttc packages
