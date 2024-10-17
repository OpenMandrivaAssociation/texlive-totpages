Name:		texlive-totpages
Version:	15878
Release:	2
Summary:	Count pages in a document, and report last page number
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/totpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package counts the actual pages in the document (as opposed
to reporting the number of the last page, as does lastpage).
The counter itself may be shipped out to the DVI file. The
package uses the everyshi package for its task.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
