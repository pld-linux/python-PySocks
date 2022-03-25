# TODO: finish tests
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# unit tests

Summary:	SOCKS client module for Python 2
Summary(pl.UTF-8):	Moduł klienta SOCKS dla Pythona 2
Name:		python-PySocks
Version:	1.7.1
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pysocks/
Source0:	https://files.pythonhosted.org/packages/source/P/PySocks/PySocks-%{version}.tar.gz
# Source0-md5:	89b1a6865c61bae67a32417517612ee6
URL:		https://pypi.org/project/PySocks/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	3proxy
BuildRequires:	python-psutil
BuildRequires:	python-pytest
BuildRequires:	python-test-server
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	3proxy
BuildRequires:	python3-psutil
BuildRequires:	python3-pytest
BuildRequires:	python3-test-server
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a standard socket-like interface for Python
for tunneling connections through SOCKS proxies.

%description -l pl.UTF-8
Ten moduł udostępnia standardowy interfejs linii gniazd dla Pythona
służący do tunelowania połączeń poprzez proxy SOCKS.

%package -n python3-PySocks
Summary:	SOCKS client module for Python 3
Summary(pl.UTF-8):	Moduł klienta SOCKS dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-PySocks
This module provides a standard socket-like interface for Python
for tunneling connections through SOCKS proxies.

%description -n python3-PySocks -l pl.UTF-8
Ten moduł udostępnia standardowy interfejs linii gniazd dla Pythona
służący do tunelowania połączeń poprzez proxy SOCKS.

%prep
%setup -q -n PySocks-%{version}

# precompiled x86_64 binary
%{__rm} test/bin/3proxy
%if %{with tests}
ln -sf /usr/bin/3proxy test/bin/3proxy
%endif

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/socks.py[co]
%{py_sitescriptdir}/sockshandler.py[co]
%{py_sitescriptdir}/PySocks-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-PySocks
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/socks.py
%{py3_sitescriptdir}/sockshandler.py
%{py3_sitescriptdir}/__pycache__/socks.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/sockshandler.cpython-*.py[co]
%{py3_sitescriptdir}/PySocks-%{version}-py*.egg-info
%endif
