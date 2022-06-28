#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9147B477339A9B86 (vinay_sajip@yahoo.co.uk)
#
Name     : pypi-distlib
Version  : 0.3.4
Release  : 36
URL      : https://bitbucket.org/pypa/distlib/downloads/distlib-0.3.4.zip
Source0  : https://bitbucket.org/pypa/distlib/downloads/distlib-0.3.4.zip
Source1  : https://bitbucket.org/pypa/distlib/downloads/distlib-0.3.4.zip.asc
Summary  : Distribution utilities
Group    : Development/Tools
License  : HPND Python-2.0
Requires: pypi-distlib-license = %{version}-%{release}
Requires: pypi-distlib-python = %{version}-%{release}
Requires: pypi-distlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/appveyor/build/vsajip/distlib
:alt: AppVeyor
.. image:: https://coveralls.io/repos/github/vsajip/distlib/badge.svg?branch=master
:target: https://coveralls.io/github/vsajip/distlib?branch=master

%package license
Summary: license components for the pypi-distlib package.
Group: Default

%description license
license components for the pypi-distlib package.


%package python
Summary: python components for the pypi-distlib package.
Group: Default
Requires: pypi-distlib-python3 = %{version}-%{release}

%description python
python components for the pypi-distlib package.


%package python3
Summary: python3 components for the pypi-distlib package.
Group: Default
Requires: python3-core
Provides: pypi(distlib)

%description python3
python3 components for the pypi-distlib package.


%prep
%setup -q -n distlib-0.3.4
cd %{_builddir}/distlib-0.3.4
pushd ..
cp -a distlib-0.3.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656407873
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-distlib
cp %{_builddir}/distlib-0.3.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-distlib/79c85e153df486fd6c05a2f7359e1ff6dc288867
cp %{_builddir}/distlib-0.3.4/tests/test_testdist-0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-distlib/71ff42eed070086a7e794fdab6a1c16495923820
cp %{_builddir}/distlib-0.3.4/tests/testdist-0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-distlib/71ff42eed070086a7e794fdab6a1c16495923820
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-distlib/71ff42eed070086a7e794fdab6a1c16495923820
/usr/share/package-licenses/pypi-distlib/79c85e153df486fd6c05a2f7359e1ff6dc288867

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
