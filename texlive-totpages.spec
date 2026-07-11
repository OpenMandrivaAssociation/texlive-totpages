%global tl_name totpages
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.00
Release:	%{tl_revision}.1
Summary:	Count pages in a document, and report last page number
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/totpages
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totpages.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package counts the actual pages in the document (as opposed to
reporting the number of the last page, as does lastpage). The counter
itself may be shipped out to the DVI file. The package uses the everyshi
package for its task.

