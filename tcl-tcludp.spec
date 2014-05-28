%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%define realname tcludp

Name:		tcl-%{realname}
Version:	1.0.10
Release:	3%{?dist}
Summary:	Tcl extension for UDP support
Group:		System Environment/Libraries
License:	MIT
URL:		http://sourceforge.net/projects/tcludp
Source0:	http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}.tar.gz
Provides:	tcl-udp = %{version}-%{release}
Provides:	%{realname} = %{version}-%{release}
BuildRequires:	tcl-devel, tk-devel
Requires:	tcl(abi) = 8.6

%description
The Tcl UDP extension provides a simple library to support UDP socket in Tcl.

%prep
%setup -q -n %{realname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/udp%{version} %{buildroot}%{tcl_sitearch}/udp%{version}

%files
%doc README license.terms ChangeLog
%{tcl_sitearch}/udp%{version}/
%{_mandir}/mann/udp*

%changelog
* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.10-3
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.10-1
- update to 1.0.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.8-1
- initial package for Fedora
