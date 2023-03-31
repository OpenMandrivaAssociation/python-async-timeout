%global srcname async-timeout

Name:		python-%{srcname}
Version:	4.0.2
Release:	2
Summary:	An asyncio-compatible timeout context manager
License:	ASL 2.0
URL:		https://github.com/aio-libs/async-timeout
Source0:	%{url}/archive/v%{version}/async-timeout-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python-pytest-runner
%{?python_provide:%python_provide python-%{srcname}}

%description
asyncio-compatible timeout context manager\
The context manager is useful in cases when you want to apply timeout\
logic around block of code or in cases when asyncio.wait_for() is not \
suitable. Also it's much faster than asyncio.wait_for() because timeout\
doesn't create a new task.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files -n python-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/async_timeout/
%{python_sitelib}/async_timeout-*.egg-info/
