#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Cache
Summary:	IPC::Cache - persisted data across process boundaries
Summary(pl):	IPC::Cache - zachowywanie danych mi�dzy procesami
Name:		perl-IPC-Cache
Version:	0.02
Release:	3
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(IPC::ShareLite) >= 0.06
BuildRequires:	perl(Storable) >= 0.607
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Cache Perl module implements an object store where data is
persisted across processes.

%description -l pl
Modu� Perla IPC::Cache implementuje pami�� podmiotow�, zapewniaj�c�
niezale�n� od proces�w trwa�o�� danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%{perl_sitelib}/IPC/Cache.pm
%{_mandir}/man3/*.3pm*
