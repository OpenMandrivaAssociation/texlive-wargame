Name:		texlive-wargame
Version:	66713
Release:	1
Summary:	A LaTeX package to prepare hex'n'counter wargames
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wargame
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wargame.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can help make classic Hex'n'Counter wargames using
LaTeX. The package provide tools for generating Hex maps and
boards Counters for units, markers, and so on Counter sheets
Order of Battle charts Illustrations in the rules using the
defined maps and counters The result will often be a PDF (or
set of PDFs) that contain everything one will need for a game
(rules, charts, boards, counter sheets). The package uses NATO
App6 symbology for units. The package uses NATO App6 symbology
for units. The package uses TikZ for most things. The package
support exporting the game to a VASSAL module See also the
README.md file for more, and of course the documentation
(including the tutorial in tutorial/game.pdf).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/wargame
%{_texmfdistdir}/tex/latex/wargame
%doc %{_texmfdistdir}/doc/latex/wargame

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
