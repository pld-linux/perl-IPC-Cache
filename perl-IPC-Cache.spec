#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Cache
Summary:	IPC::Cache - persisted data across process boundaries
Summary(pl):	IPC::Cache - zachowywanie danych miêdzy procesami
Name:		perl-IPC-Cache
Version:	0.02
Release:	4
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f730e095f98e44c7b5a9cb5647e6db02
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(IPC::ShareLite) >= 0.06
BuildRequires:	perl(Storable) >= 0.607
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%{perl_vendorlib}/IPC/Cache.pm
%{_mandir}/man3/*.3pm*
