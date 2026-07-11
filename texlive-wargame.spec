%global tl_name wargame
%global tl_revision 72903

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	A LaTeX package to prepare hexncounter wargames
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wargame
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can help make classic Hex'n'Counter wargames using LaTeX.
The package provides tools for generating Hex maps and boards Counters
for units, markers, and so on Counter sheets Order of Battle charts
Illustrations in the rules using the defined maps and counters The
result will often be a PDF (or set of PDFs) that contains everything one
will need for a game (rules, charts, boards, counter sheets). The
package uses NATO App6 symbology for units. The package uses NATO App6
symbology for units. The package uses TikZ for most things. The package
supports exporting the game to a VASSAL module See also the README.md
file for more, and of course the documentation (including the tutorial
in tutorial/game.pdf).

