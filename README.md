# md-highlighter README

`md-highlighter` is a VSCode extension for syntax highlighting of text files used in molecular modeling and molecular dynamics simulation. The current version focuses on file type registration, keyword matching, and TextMate scope assignment for supported formats. It is intended to make these files easier to read and edit in VSCode.

## Features

Supported formats:

- NAMD: rtf, pdb, prm, psf, str, inp
- Amber: in, prmtop, inpcrd, prepin, frcmod, lib/off, ac, mc
- Gromacs: gro, atp, arn, rtp, hdb, r2b, tdb, mtp, vsd
- small molecule: sdf, mol2
- PLUMED: .plumed.dat

For Gromacs `.top`/`.itp` files, you may also install `gromacs-helper`.

Tested in theme "Atom One Light".

## Gallery

Examples of highlighted files:

![ph-pdb](https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/pdb.png)

<center><font size=3.5>.pdb file</font></center>

![rtf](https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/rtf.png)

<center><font size=3.5>NAMD/CHARMM .rtf file</font></center>

<center><img src="https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/psf.png" alt="psf" style="zoom: 67%;" /></center>

<center><font size=3.5>NAMD/CHARMM .psf file</font></center>

<center><img src="https://cdn.jsdelivr.net/gh/gxf1212/md-highlighter@master/images/prm.png" alt="prm" style="zoom:67%;" /></center>

<center><font size=3.5>NAMD/CHARMM .prm file</font></center>

## Conventions

- variable.other.residue-number (except psf,gro)
- entity.name.type.residue-name (except hdb)
- constant.numeric.atom-number (except gro,lib)
- entity.name.tag.atom-name
- support.type.atom-type
- constant.numeric.mass
- constant.numeric.coordinate
- string.quoted.charge (rtf,psf,mol2,prepi, except rtf)
- string.quoted.element-symbol
- string.quoted.bond-number
- string.quoted.velocity
- support.type.segment-name (except psf)
- entity.name.function: a different kind of blue

Different file types may render differently under different themes.

## Known Issues

- **Are the files too colorful?**
- PDB: CONNECT and TER highlight later terms
- RTF: the structure depiction after ! is italic...
- atom names
  - with `'`, `+`, `-` in them are matched by `\\S+` but not `[A-Z+-']`
  - not always start with numbers (`-?\\+?[A-Z]+[0-9]*[A-Z0-9_]*`)
  - MTP: the last word in rotations
- Amber `.in` files include various types; so do Gromacs `.itp` files
- PRMTOP: E-01, normal `constant`?
- FRCMOD: I know atomtypes can only be 1/2 characters long. Matching with this may solve the mismatching problem
- LIB: later section not read and implemented
- MTP/RTP: cannot match the last atom name?
- not fully tested for OPLS series and some other force fields where naming conventions may differ

TODO:

- add self-defined colors for aminoacids types (polar, nonpolar, etc.)
- add self-defined colors like pink, etc.
- refine sdf file rules

## Release Notes

see CHANGELOG

## For more information

Welcome to contact me for any problems: [gxf1212@zju.edu.cn](mailto:gxf1212@zju.edu.cn)

**Enjoy!**
