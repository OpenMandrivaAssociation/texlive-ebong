Name:		texlive-ebong
Version:	67933
Release:	1
Summary:	Utility for writing Bengali in Rapid Roman Format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/ebong
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebong.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebong.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ebong.bin = %{EVRD}

%description
A tool (preprocessor) for writing your pRaa-ne-r ka-thaa in the
bengali langauage. It allows one to write the text in Rapid
Roman Bangla and convert it to the bangtex format by a python
program. All LaTeX markups are preserved in the target file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ebong
%{_texmfdistdir}/scripts/ebong/ebong.py
%doc %{_texmfdistdir}/doc/latex/ebong/ANNOUNCE.txt
%doc %{_texmfdistdir}/doc/latex/ebong/README
%doc %{_texmfdistdir}/doc/latex/ebong/eb.b
%doc %{_texmfdistdir}/doc/latex/ebong/eb.pdf
%doc %{_texmfdistdir}/doc/latex/ebong/eb_tex.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ebong/ebong.py ebong
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
