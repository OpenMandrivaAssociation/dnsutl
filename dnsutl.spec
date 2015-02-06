%define name  dnsutl
%define version   1.8
%define release   6

Summary:      Utilities to make DNS easier to configure
Name:         %{name}
Version:      %{version}
Release:      %{release}
License:    GPL
Group:        Networking/Other
Source:       http://www.canb.auug.org.au/%7Emillerp/dnsutl/%{name}-%{version}.tar.bz2
URL:          http://www.canb.auug.org.au/~millerp/dnsutl/
 
Buildrequires: byacc gettext-devel gawk
# (tv) for gsoelim:
Buildrequires: groff
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The dnsutl package is a collection of tools to make administering
DNS easier.  The tools include:

dns-rev: Take the forward DNS mapping and generate the reverse mapping.

dns-hosts: Take the forward DNS mapping and generate the /etc/hosts file.

dns-ng: Take the forward DNS mapping and generate the /etc/netgroup file.

dns-ethers: By using a bogus record type, you can keep the MAC address
	with the IP address, and generate the /etc/ethers file.

dns-bootp: Using the MAC and IP information, you can generate the
	/etc/bootptab file.

dns-bootparams: Using the MAC and IP information, you can generate the
	Sun /etc/bootparams file.

All of these programs are both faster than shell scripts, and more
robust when faced with all the peculiar semantics of DNS resource files.
They even understand the \f(CW$include\fP directive.

%prep

%setup -q 
%configure2_5x

%build
# doesn't build with -j
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc etc/CHANGES.1*
%doc README 
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8-5mdv2011.0
+ Revision: 617863
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.8-4mdv2010.0
+ Revision: 428412
- use %%configure2_5x
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.8-3mdv2009.0
+ Revision: 222092
- buildrequires groff for gsoelim
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.8-2mdv2007.0
- rebuild

* Thu Mar 09 2006 Lenny Cartier <lenny@mandriva.com> 1.8-1mdk
- 1.8

* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 1.7-1mdk
- 1.7

* Thu Jun 03 2004 Michael Scherer <misc@mandrake.org> 1.6-8mdk 
- rebuild for new libintl 
- add patch0
- various spec improvement

