#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : hacking
Version  : 0.13.0
Release  : 28
URL      : http://tarballs.openstack.org/hacking/hacking-0.13.0.tar.gz
Source0  : http://tarballs.openstack.org/hacking/hacking-0.13.0.tar.gz
Source99 : http://tarballs.openstack.org/hacking/hacking-0.13.0.tar.gz.asc
Summary  : OpenStack Hacking Guideline Enforcement
Group    : Development/Tools
License  : Apache-2.0
Requires: hacking-python
Requires: flake8
Requires: flake8-docstrings
Requires: mccabe
Requires: pbr
Requires: pep8
Requires: pyflakes
Requires: six
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : configparser-python
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
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes
BuildRequires : pytest
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
BuildRequires : tox
BuildRequires : traceback2
BuildRequires : unittest2
BuildRequires : virtualenv
Patch1: requires.patch

%description
Introduction
============
hacking is a set of flake8 plugins that test and enforce the :ref:`StyleGuide`.

%package python
Summary: python components for the hacking package.
Group: Default

%description python
python components for the hacking package.


%prep
%setup -q -n hacking-0.13.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489025537
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1489025537
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
