%define name	fdupes
%define version	1.50
%define pre     PR2
%define release	%mkrel 0.%{pre}.3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Identify or delete duplicate files
License:	BSD like
Group:		File tools
Url:		http://netdial.caribe.net/~adrian2/fdupes.html
Source0:		http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}-%{pre}.tar.gz
Source1:        macros.fdupes
Patch0:     %{name}-%{version}-destdir.patch
# http://bugs.debian.org/213385
Patch1:     %{name}-%{version}-compare-file.patch
# http://bugs.debian.org/447601
Patch2:     %{name}-%{version}-lfs.patch
# http://bugs.debian.org/353789
Patch3:     %{name}-%{version}-typo.patch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make COMPILER_OPTIONS="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/

%files
%defattr(-,root,root)
%doc CHANGES CONTRIBUTORS INSTALL README TODO
%{_bindir}/%{name}
%{_sysconfdir}/rpm/macros.fdupes


%changelog
* Thu Nov 13 2012 akdengi <akdengi> 1.50-0.PR2.3
- add fdupes rpm macros

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.50-0.PR2.2mdv2011.0
+ Revision: 618262
- the mass rebuild of 2010.0 packages

* Mon Sep 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.50-0.PR2.1mdv2010.0
+ Revision: 432988
- new version (even Debian has it already...)

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.40-5mdv2010.0
+ Revision: 428713
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.40-4mdv2009.0
+ Revision: 245076
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.40-2mdv2008.1
+ Revision: 124930
- kill re-definition of %%buildroot on Pixel's request
- import fdupes


* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-2mdv2007.0
- %%mkrel

* Tue Jun 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdk 
- first mdk release
