#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hacking
Version  : 0.10.2
Release  : 15
URL      : http://tarballs.openstack.org/hacking/hacking-0.10.2.tar.gz
Source0  : http://tarballs.openstack.org/hacking/hacking-0.10.2.tar.gz
Summary  : OpenStack Hacking Guideline Enforcement
Group    : Development/Tools
License  : Apache-2.0
Requires: hacking-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : coverage
BuildRequires : discover
BuildRequires : docutils
BuildRequires : eventlet
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8
BuildRequires : greenlet
BuildRequires : mccabe
BuildRequires : oslosphinx
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pyflakes
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : testrepository
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2
BuildRequires : unittest2
Patch1: unlock-pep8.patch

%description
Introduction
============
hacking is a set of flake8 plugins that test and enforce the `OpenStack
Style Guidlines <http://docs.openstack.org/developer/hacking>`_.

%package python
Summary: python components for the hacking package.
Group: Default

%description python
python components for the hacking package.


%prep
%setup -q -n hacking-0.10.2
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
