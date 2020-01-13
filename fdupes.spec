Summary:	Identify or delete duplicate files
Name:		fdupes
Version:	2.0.0
Release:	1
License:	BSD like
Group:		File tools
Url:		https://github.com/adrianlopezroche/fdupes
Source0:	https://github.com/adrianlopezroche/fdupes/archive/%{name}-%{version}.tar.gz
Source1:	macros.fdupes
# From upstream.
Patch0:		%{url}/commit/315f6702f1cc37036d9f826314245b44a781c387.patch#/%{name}-1.6.1-delete_old_TODO.patch
Patch1:		%{url}/commit/e95ec42dc178eff0410880c3dc4c0dac3df442df.patch#/%{name}-1.6.1-option_sort_by_ctime.patch
Patch2:		%{url}/commit/88f3d2dd31fbef7e539b2523724221e8e8e5a9f0.patch#/%{name}-1.6.1-allow_a_instead_of_all.patch

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%prep
%setup -q
%autopatch -p1

%build
%setup_compile_flags
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
