#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Attachment-Stripper
Summary:	Email::MIME::Attachment::Stripper - Strip the attachments from a mail
#Summary(pl):	
Name:		perl-Email-MIME-Attachment-Stripper
Version:	1.3
Release:	1
# same as perl-Mail-Message-Attachment-Stripper
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f554d9f0d941425cb36dd463088f812
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME >= 1.8
BuildRequires:	perl-Email-MIME-Encodings >= 1.1
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given a Email::MIME object, detach all attachments from the message. These
are then available separately.

# %description -l pl
# TODO

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
%doc Changes
%{perl_vendorlib}/Email/MIME/Attachment/*.pm
%{_mandir}/man3/*
