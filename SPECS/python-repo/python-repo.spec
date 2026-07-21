# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond check 0

%global srcname repo

Name:           python-%{srcname}
Version:        2.65
Release:        %autorelease
Summary:        Repo is a tool built on top of Git
License:        Apache-2.0
URL:            https://gerrit.googlesource.com/git-repo
#!RemoteAsset:  git+%{url}#v%{version}
#!CreateArchive
Source:         %{name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
%if %{with check}
BuildRequires:  python3dist(pytest)
%endif

BuildArch:      noarch

Provides:       %{srcname} = %{version}-%{release}

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       git

%description
Repo helps manage many Git repositories, does the uploads to revision
control systems, and automates parts of the development workflow.
Repo is not meant to replace Git, only to make it easier to work with Git.


%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
# repo is an unusual tool because it downloads all of its own Python modules
# at runtime using GPG-signed git tags, and stores those files as part of the
# project that it is working with. This package just provides the wrapper
# script, which provides the GPG signing keys for verifying that the correct
# Python code was downloaded, so there's nothing to actually build.

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{srcname}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/%{srcname}*.1
install -Dpm0644 completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{srcname}

%check
%if %{with check}
%{py3_test_envvars} %{python3} -m pytest
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}*.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{srcname}

%changelog
%autochangelog
