%define pre     PR2

Summary:	Identify or delete duplicate files
Name:		fdupes
Version:	1.50
Release:	0.%{pre}.3
License:	BSD like
Group:		File tools
Url:		http://netdial.caribe.net/~adrian2/fdupes.html
Source0:	http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}-%{pre}.tar.gz
Source1:	macros.fdupes
Patch0:		%{name}-%{version}-destdir.patch
# http://bugs.debian.org/213385
Patch1:		%{name}-%{version}-compare-file.patch
# http://bugs.debian.org/447601
Patch2:		%{name}-%{version}-lfs.patch
# http://bugs.debian.org/353789
Patch3:		%{name}-%{version}-typo.patch

%description
FDUPES is a program for identifying or deleting duplicate files residing within
specified directories.

%prep
%setup -qn %{name}-%{version}-%{pre}
%apply_patches

%build
%make COMPILER_OPTIONS="%{optflags}"

%install
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
%doc CHANGES CONTRIBUTORS INSTALL README TODO
%{_bindir}/%{name}
%{_sysconfdir}/rpm/macros.fdupes

