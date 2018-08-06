# revision 26313
# category Package
# catalog-ctan /language/ebong
# catalog-date 2012-05-07 23:49:19 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-ebong
Version:	20180303
Release:	1
Summary:	Utility for writing Bengali in Rapid Roman Format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/ebong
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebong.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebong.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ebong/ebong.py ebong
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120507-1
+ Revision: 812245
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070306-2
+ Revision: 751284
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070306-1
+ Revision: 718296
- texlive-ebong
- texlive-ebong
- texlive-ebong
- texlive-ebong

