%define name	fdupes
%define version	1.50
%define pre     PR2
%define release	%mkrel 0.%{pre}.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Identify or delete duplicate files
License:	BSD like
Group:		File tools
Url:		http://netdial.caribe.net/~adrian2/fdupes.html
Source:		http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}-%{pre}.tar.gz
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

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTRIBUTORS INSTALL README TODO
%{_bindir}/%{name}

