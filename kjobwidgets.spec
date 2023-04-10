#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kjobwidgets
Version  : 5.105.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.105/kjobwidgets-5.105.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.105/kjobwidgets-5.105.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.105/kjobwidgets-5.105.0.tar.xz.sig
Summary  : Widgets for tracking KJob instances
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-3.0
Requires: kjobwidgets-data = %{version}-%{release}
Requires: kjobwidgets-lib = %{version}-%{release}
Requires: kjobwidgets-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KJobWidgets
Widgets for showing progress of asynchronous jobs
## Introduction
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package data
Summary: data components for the kjobwidgets package.
Group: Data

%description data
data components for the kjobwidgets package.


%package dev
Summary: dev components for the kjobwidgets package.
Group: Development
Requires: kjobwidgets-lib = %{version}-%{release}
Requires: kjobwidgets-data = %{version}-%{release}
Provides: kjobwidgets-devel = %{version}-%{release}
Requires: kjobwidgets = %{version}-%{release}

%description dev
dev components for the kjobwidgets package.


%package lib
Summary: lib components for the kjobwidgets package.
Group: Libraries
Requires: kjobwidgets-data = %{version}-%{release}
Requires: kjobwidgets-license = %{version}-%{release}

%description lib
lib components for the kjobwidgets package.


%package license
Summary: license components for the kjobwidgets package.
Group: Default

%description license
license components for the kjobwidgets package.


%prep
%setup -q -n kjobwidgets-5.105.0
cd %{_builddir}/kjobwidgets-5.105.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681143798
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1681143798
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kjobwidgets
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kjobwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kjobwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.JobView.xml
/usr/share/dbus-1/interfaces/kf5_org.kde.JobViewServer.xml
/usr/share/dbus-1/interfaces/kf5_org.kde.JobViewV2.xml
/usr/share/locale/af/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/en/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kjobwidgets5_qt.qm
/usr/share/qlogging-categories5/kjobwidgets.categories
/usr/share/qlogging-categories5/kjobwidgets.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KJobWidgets/KAbstractWidgetJobTracker
/usr/include/KF5/KJobWidgets/KDialogJobUiDelegate
/usr/include/KF5/KJobWidgets/KJobWidgets
/usr/include/KF5/KJobWidgets/KStatusBarJobTracker
/usr/include/KF5/KJobWidgets/KUiServerJobTracker
/usr/include/KF5/KJobWidgets/KUiServerV2JobTracker
/usr/include/KF5/KJobWidgets/KWidgetJobTracker
/usr/include/KF5/KJobWidgets/kabstractwidgetjobtracker.h
/usr/include/KF5/KJobWidgets/kdialogjobuidelegate.h
/usr/include/KF5/KJobWidgets/kjobwidgets.h
/usr/include/KF5/KJobWidgets/kjobwidgets_export.h
/usr/include/KF5/KJobWidgets/kjobwidgets_version.h
/usr/include/KF5/KJobWidgets/kstatusbarjobtracker.h
/usr/include/KF5/KJobWidgets/kuiserverjobtracker.h
/usr/include/KF5/KJobWidgets/kuiserverv2jobtracker.h
/usr/include/KF5/KJobWidgets/kwidgetjobtracker.h
/usr/lib64/cmake/KF5JobWidgets/KF5JobWidgetsConfig.cmake
/usr/lib64/cmake/KF5JobWidgets/KF5JobWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF5JobWidgets/KF5JobWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5JobWidgets/KF5JobWidgetsTargets.cmake
/usr/lib64/libKF5JobWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KJobWidgets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5JobWidgets.so.5
/usr/lib64/libKF5JobWidgets.so.5.105.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kjobwidgets/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kjobwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kjobwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kjobwidgets/e458941548e0864907e654fa2e192844ae90fc32
