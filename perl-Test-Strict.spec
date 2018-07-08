#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Strict
Version  : 0.47
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-0.47.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-0.47.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-strict-perl/libtest-strict-perl_0.45-1.debian.tar.xz
Summary  : 'Check syntax, presence of use strict; and test coverage'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Strict-license
Requires: perl-Test-Strict-man
Requires: perl(IO::Scalar)
BuildRequires : perl(IO::Scalar)

%description
testing strictness in a distribution, by Pierre Denis <pdenis@gmail.com>.
* Installation

%package license
Summary: license components for the perl-Test-Strict package.
Group: Default

%description license
license components for the perl-Test-Strict package.


%package man
Summary: man components for the perl-Test-Strict package.
Group: Default

%description man
man components for the perl-Test-Strict package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Test-Strict-0.47
mkdir -p %{_topdir}/BUILD/Test-Strict-0.47/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-Strict-0.47/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Test-Strict
cp LICENSE %{buildroot}/usr/share/doc/perl-Test-Strict/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Test-Strict/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Test/Strict.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Test-Strict/LICENSE
/usr/share/doc/perl-Test-Strict/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Strict.3
