#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Cache
Summary:	IPC::Cache Perl module
Summary(cs):	Modul IPC::Cache pro Perl
Summary(da):	Perlmodul IPC::Cache
Summary(de):	IPC::Cache Perl Modul
Summary(es):	Módulo de Perl IPC::Cache
Summary(fr):	Module Perl IPC::Cache
Summary(it):	Modulo di Perl IPC::Cache
Summary(ja):	IPC::Cache Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	IPC::Cache ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul IPC::Cache
Summary(pl):	Modu³ Perla IPC::Cache
Summary(pt):	Módulo de Perl IPC::Cache
Summary(pt_BR):	Módulo Perl IPC::Cache
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl IPC::Cache
Summary(sv):	IPC::Cache Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl IPC::Cache
Summary(zh_CN):	IPC::Cache Perl Ä£¿é
Name:		perl-IPC-Cache
Version:	0.02
Release:	1
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(IPC::ShareLite) >= 0.06
BuildRequires:	perl(Storable) >= 0.607
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Cache Perl module implements an object store where data is
persisted across processes.

%description -l pl
Modu³ Perla IPC::Cache implementuje pamiêæ podmiotow±, zapewniaj±c±
niezale¿n± od procesów trwa³o¶æ danych.

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
%{_mandir}/man3/*.3pm.gz
