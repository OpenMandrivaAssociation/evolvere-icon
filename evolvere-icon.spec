%global theme	evolvere

Name:		evolvere-icon
Version:	1.1.9
Release:	1
Summary:	%{theme} icon theme
Group:		Graphical desktop/Other

License:	cc-by-nc-nd
URL:		https://plus.google.com/111079135224465849361

Source0:	%{theme}.tar-%{version}.tar.gz

BuildArch:	noarch

%description
%{theme} a smooth icon theme for your KDE workspace.


%prep
%setup -c -n %{name}-%{version}


%build
# Nothing to build


%install
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
cp -axv ./ %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/
