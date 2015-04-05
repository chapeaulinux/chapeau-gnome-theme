%define _use_internal_dependency_generator 0

Summary:	Chapeau Gnome Themes
Name:		chapeau-gnome-theme
Version:	1
Release:	1%{?dist}
License:	distributable
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	noarch

Requires:	moka-icon-theme
Requires:	faba-icon-theme


%description
A meta package which requires the theming packages for Chapeau's Gnome desktop

%prep

%build

%clean 

%install

%post
# remove self after required packages are pulled.
#rpm -e %{name}

%files 


%changelog
* Fri Apr 03 2015 Vince Pooley <vince@chapeaulinux.org>
- initial release

