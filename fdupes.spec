%define name	fdupes
%define version	1.40
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Identify or delete duplicate files
License:	BSD like
Group:		File tools
Source:		http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}.tar.bz2
Patch:		%{name}-1.40.makefile.patch.bz2
Url:		http://netdial.caribe.net/~adrian2/fdupes.html

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%prep
%setup
%patch

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTRIBUTORS INSTALL README TODO
%{_bindir}/%{name}

