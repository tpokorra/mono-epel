Name:           epel-rpm-macros
Version:        7
Release:        5
Summary:        Extra Packages for Enterprise Linux RPM macros

Group:          System Environment/Base
License:        GPLv2

# This is a EPEL maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://download.fedoraproject.org/pub/epel
Source0:        macros.epel-rpm-macros
Source1:        GPL
Source2:        macros.mono-srpm

BuildArch:     noarch
Requires:      redhat-release >=  %{version}

%description
This package contains the Extra Packages for Enterprise Linux (EPEL) RPM
macros for building EPEL packages. 

%prep
install -pm 644 %{SOURCE1} .

%install
#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT/usr/lib/rpm/macros.d/macros.epel-rpm-macros
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT/usr/lib/rpm/macros.d/macros.mono-srpm

%files
%license GPL
/usr/lib/rpm/macros.d/macros.epel-rpm-macros
/usr/lib/rpm/macros.d/macros.mono-srpm


%changelog
* Wed Jan  6 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 7-5
- add macros for Mono (#1295117)

* Thu Oct  8 2015 Thomas Spura <tomspur@fedoraproject.org> - 7-4
- Fix python_provide macro to use epoch and obsolete previous python- package

* Tue Aug 18 2015 Orion Poplawski <orion@cora.nwra.com> 7-3
- Fix py2_install macro
- Cleanup spec

* Sat Aug 01 2015 Kevin Fenzi <kevin@scrye.com> 7-2
- Add python macros. Fixes bug #1241655

* Wed Apr 29 2015 Kevin Fenzi <kevin@scrye.com> 7-1
- Initial version for epel.
