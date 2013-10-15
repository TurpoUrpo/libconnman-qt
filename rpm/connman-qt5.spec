# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       connman-qt5

# >> macros
# << macros

Summary:    Qt bindings for connman
Version:    1.0.29
Release:    1
Group:      System/GUI/Other
License:    Apache License
URL:        https://github.com/nemomobile/libconnman-qt.git
Source0:    %{name}-%{version}.tar.bz2
Source100:  connman-qt5.yaml
Requires:   connman >= 1.15
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(dbus-1)

%description
This is a library for working with connman using Qt


%package declarative
Summary:    Declarative plugin for Qt Quick for connman-qt
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   connman-qt5

%description declarative
This package contains the files necessary to develop
applications using libconnman-qt


%package devel
Summary:    Development files for connman-qt
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
applications using libconnman-qt


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libconnman-qt5.so.*
# >> files
# << files

%files declarative
%defattr(-,root,root,-)
%{_usr}/lib/qt5/qml/MeeGo/Connman
# >> files declarative
# << files declarative

%files devel
%defattr(-,root,root,-)
%{_usr}/include/connman-qt5
%{_usr}/lib/pkgconfig/connman-qt5.pc
%{_usr}/lib/connman-qt5.pc
%{_usr}/lib/libconnman-qt5.prl
%{_usr}/lib/libconnman-qt5.so
# >> files devel
# << files devel
