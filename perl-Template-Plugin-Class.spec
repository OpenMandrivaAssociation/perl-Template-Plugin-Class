%define upstream_name    Template-Plugin-Class
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Allow calling of class methods on arbitrary classes
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Template)
BuildArch:	noarch

%description
Template::Plugin::Class allows you to call class methods on arbitrary classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 405531
- rebuild using %%perl_convert_version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2010.0
+ Revision: 373049
- new version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.13-5mdv2009.0
+ Revision: 241950
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-3mdv2008.0
+ Revision: 86930
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-2mdv2007.0
- Rebuild

* Thu May 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- new version
- no buildrequires on perl-devel, this is a Module-Build managed module

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-4mdk
- fix buildrequires

* Thu Mar 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-3mdk
- spec rewrite

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 0.12-2mdk
- rpmlint fixes

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 0.12-1mdk
- Initial build.

