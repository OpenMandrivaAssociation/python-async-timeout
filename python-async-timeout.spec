%define module async-timeout
%define oname async_timeout

%bcond tests 1

Name:		python-async-timeout
Version:	5.0.1
Release:	1
Summary:	An asyncio-compatible timeout context manager
License:	ASL 2.0
URL:		https://github.com/aio-libs/async-timeout
Source0:	%{url}/archive/v%{version}/async-timeout-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
%endif

%description
asyncio-compatible timeout context manager\
The context manager is useful in cases when you want to apply timeout\
logic around block of code or in cases when asyncio.wait_for() is not \
suitable. Also it's much faster than asyncio.wait_for() because timeout\
doesn't create a new task.

%prep -a
sed -i '/addopts= --cov=async_timeout --cov-report=term --cov-report=html --cov-branch/d' setup.cfg

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -v
%endif

%files
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
