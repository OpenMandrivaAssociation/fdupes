Summary:	Identify or delete duplicate files
Name:		fdupes
Version:	2.1.2
Release:	3
License:	BSD like
Group:		File tools
Url:		https://github.com/adrianlopezroche/fdupes
Source0:	https://github.com/adrianlopezroche/fdupes/archive/%{name}-%{version}.tar.gz
Source1:	macros.fdupes
	
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpcre2-posix)

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%prep
%setup -q
%autopatch -p1

%build
autoreconf --install
%setup_compile_flags
%configure
%make CC=%{__cc} LDFLAGS="%{ldflags}" COMPILER_OPTIONS="%{optflags}"

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.%{name}

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

%files
%doc CHANGES CONTRIBUTORS INSTALL README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_sysconfdir}/rpm/macros.fdupes
