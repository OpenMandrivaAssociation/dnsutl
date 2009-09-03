%define name  dnsutl
%define version   1.8
%define release   %mkrel 4

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

