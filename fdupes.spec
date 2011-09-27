%define pre PR2

Name:		fdupes
Summary:		Identify or delete duplicate files
Group:		File tools
Version:		1.50
Release:		%mkrel -c %{pre} 3
License:		BSD like
Url:		http://netdial.caribe.net/~adrian2/fdupes.html
Source0:		http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}-%{pre}.tar.gz
Source1:		fdupes.macros
Patch0:     %{name}-%{version}-destdir.patch
# http://bugs.debian.org/213385
Patch1:     %{name}-%{version}-compare-file.patch
# http://bugs.debian.org/447601
Patch2:     %{name}-%{version}-lfs.patch
# http://bugs.debian.org/353789
Patch3:     %{name}-%{version}-typo.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
install -D -m644 %{S:1} %{buildroot}%{_sysconfdir}/rpm/macros.d/fdupes.macros

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTRIBUTORS INSTALL README TODO
%{_sysconfdir}/rpm/macros.d/fdupes.macros
%{_bindir}/%{name}
