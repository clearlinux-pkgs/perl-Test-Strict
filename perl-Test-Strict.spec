#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Strict
Version  : 0.52
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-0.52.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-0.52.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-strict-perl/libtest-strict-perl_0.45-1.debian.tar.xz
Summary  : 'Check syntax, presence of use strict; and test coverage'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Strict-license = %{version}-%{release}
Requires: perl-Test-Strict-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Scalar)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
testing strictness in a distribution, by Pierre Denis <pdenis@gmail.com>.
* Installation

%package dev
Summary: dev components for the perl-Test-Strict package.
Group: Development
Provides: perl-Test-Strict-devel = %{version}-%{release}
Requires: perl-Test-Strict = %{version}-%{release}

%description dev
dev components for the perl-Test-Strict package.


%package license
Summary: license components for the perl-Test-Strict package.
Group: Default

%description license
license components for the perl-Test-Strict package.


%package perl
Summary: perl components for the perl-Test-Strict package.
Group: Default
Requires: perl-Test-Strict = %{version}-%{release}

%description perl
perl components for the perl-Test-Strict package.


%prep
%setup -q -n Test-Strict-0.52
cd %{_builddir}
tar xf %{_sourcedir}/libtest-strict-perl_0.45-1.debian.tar.xz
cd %{_builddir}/Test-Strict-0.52
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-Strict-0.52/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Strict
cp %{_builddir}/Test-Strict-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Strict/e93136f38a901c445d16669f3994b8b17a8f93e1 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Strict.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Strict/e93136f38a901c445d16669f3994b8b17a8f93e1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
