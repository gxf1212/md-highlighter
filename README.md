# md-highlighter README

`md-highlighter` is a simple extension to highlight files about molecular modeling and molecular dynamics simulation. Specially, it supports NAMD/CHARMM and some of Amber file formats.

## Features

Supported format: 

- NAMD: rtf, pdb, prm, psf, str, inp
- Amber: in, prmtop, inpcrd, prepin, frcmod
- Gromacs: atp, rtp, mtp (pmx), ...
- small molecule: sdf, mol2 (modified from gromacs helper), ...
- PLUMED: .plumed.dat
- upcoming: (AmberTools leap), lib,...

For gromacs-related files, please install `gromacs-helper`. For VMD, install `TCL`. For Gaussian, install `Gaussian Input File (gjf)`. But maybe I'll make my own syntaxes.

Tested in theme "Atom One Light".

This extension is created with the help of ChatGPT and New Bing.

## Gallery

Install to explore more file types!

![ph-pdb](https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/pdb.png)

<center><font size=3.5>.pdb file</font></center>

![rtf](https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/rtf.png)

<center><font size=3.5>NAMD/CHARMM .rtf file</font></center>

<center><img src="https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/psf.png" alt="psf" style="zoom: 67%;" /></center>

<center><font size=3.5>NAMD/CHARMM .psf file</font></center>

<center><img src="https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/prm.png" alt="prm" style="zoom:67%;" /></center>

<center><font size=3.5>NAMD/CHARMM .prm file</font></center>

## Conventions

- variable.other.residue-number (except psf)
- entity.name.type.residue-name
- constant.numeric.atom-number
- entity.name.tag.atom-name
- support.type.atom-type
- constant.numeric.mass
- string.quoted.charge (rtf,psf,mol2,prepi, except rtf)
- string.quoted.element-symbol
- support.type.segment-name (except psf)
- entity.name.function: a different kind of blue

But different file types might rendered with different colors...

## Known Issues

- PDB: recognize lines starting with ATOM or HETATM by `"begin"` and `"end"`?
- PSF: ATOM and BOND are not highlighted.
- RTF: the structure depiction after ! is italic...
- MOL2: number of atoms/bonds (2nd line); atom number not matched
- atom names
  - with `'`, `+`, `-` in them are matched by `\\S+` but not `[A-Z+-']`
  - not always start with numbers (`-?\\+?[A-Z]+[0-9]*[A-Z0-9_]*`)
  - MTP: the last word in rotations
- Amber .in files include various types; so do Gromacs .itp file
- PRMTOP: E-01, normal `constant`?
- MTP/RTP: cannot match the last atom name?
- not fully tested files for OPLS series and more force field, where naming conventions might be different

TODO:

- add self-defined colors for aminoacids types (polar, nonpolar, etc.)
- add self-defined colors like pink, etc.

## Release Notes

see CHANGELOG

## For more information

Welcome to contact me for any problems: [gxf1212@zju.edu.cn](mailto:gxf1212@zju.edu.cn)

**Enjoy!**
