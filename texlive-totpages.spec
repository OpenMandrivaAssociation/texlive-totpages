# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/totpages
# catalog-date 2007-01-18 20:18:05 +0100
# catalog-license lppl
# catalog-version 2.00
Name:		texlive-totpages
Version:	2.00
Release:	1
Summary:	Count pages in a document, and report last page number
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/totpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package counts the actual pages in the document (as opposed
to reporting the number of the last page, as does lastpage).
The counter itself may be shipped out to the DVI file. The
package uses the everyshi package for its task.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/totpages/totpages.sty
%doc %{_texmfdistdir}/doc/latex/totpages/README
%doc %{_texmfdistdir}/doc/latex/totpages/totexmpl.tex
%doc %{_texmfdistdir}/doc/latex/totpages/totpages.pdf
#- source
%doc %{_texmfdistdir}/source/latex/totpages/totpages.drv
%doc %{_texmfdistdir}/source/latex/totpages/totpages.dtx
%doc %{_texmfdistdir}/source/latex/totpages/totpages.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
