Summary:	Identify or delete duplicate files
Name:		fdupes
Version:	2.3.2
Release:	1
License:	BSD like
Group:		File tools
Url:		https://github.com/adrianlopezroche/fdupes
Source0:	https://github.com/adrianlopezroche/fdupes/releases/download/v%{version}/fdupes-%{version}.tar.gz
Source1:	macros.fdupes
	
BuildSystem:	autotools
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:	pkgconfig(sqlite3)

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%install -a
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.%{name}

%if ! %{cross_compiling}
%check
cd _OMV_rpm_build
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir
%endif

%files
%doc CHANGES CONTRIBUTORS INSTALL README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man7/%{name}-help.*
%{_sysconfdir}/rpm/macros.fdupes
