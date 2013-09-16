Summary: perl module for image data extraction
Name: perl-Image-ExifTool
Version: 9.37
Release: 1
License: Artistic/GPL
Group: Development/Libraries/Perl
URL: http://owl.phy.queensu.ca/~phil/exiftool/
Source0: Image-ExifTool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ExifTool is a customizable set of Perl modules plus a full-featured
application for reading and writing meta information in a wide variety of
files, including the maker note information of many digital cameras by
various manufacturers such as Canon, Casio, FLIR, FujiFilm, GE, HP,
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo,
Sigma/Foveon and Sony.

Below is a list of file types and meta information formats currently
supported by ExifTool (r = read, w = write, c = create):

  File Types
  ------------+-------------+-------------+-------------+------------
  3FR   r     | EPS   r/w   | M2TS  r     | PAGES r     | RWZ   r
  3G2   r     | ERF   r/w   | M4A/V r     | PBM   r/w   | RM    r
  3GP   r     | EXE   r     | MEF   r/w   | PCD   r     | SO    r
  ACR   r     | EXIF  r/w/c | MIE   r/w/c | PDF   r/w   | SR2   r/w
  AFM   r     | EXR   r     | MIFF  r     | PEF   r/w   | SRF   r
  AI    r/w   | F4A/V r     | MKA   r     | PFA   r     | SRW   r/w
  AIFF  r     | FFF   r/w   | MKS   r     | PFB   r     | SVG   r
  APE   r     | FLA   r     | MKV   r     | PFM   r     | SWF   r
  ARW   r/w   | FLAC  r     | MNG   r/w   | PGF   r     | THM   r/w
  ASF   r     | FLV   r     | MODD  r     | PGM   r/w   | TIFF  r/w
  AVI   r     | FPF   r     | MOS   r/w   | PLIST r     | TORRENT r
  BMP   r     | FPX   r     | MOV   r     | PICT  r     | TTC   r
  BTF   r     | GIF   r/w   | MP3   r     | PMP   r     | TTF   r
  CHM   r     | GZ    r     | MP4   r     | PNG   r/w   | VRD   r/w/c
  COS   r     | HDP   r/w   | MPC   r     | PPM   r/w   | VSD   r
  CR2   r/w   | HDR   r     | MPG   r     | PPT   r     | WAV   r
  CRW   r/w   | HTML  r     | MPO   r/w   | PPTX  r     | WDP   r/w
  CS1   r/w   | ICC   r/w/c | MQV   r     | PS    r/w   | WEBP  r
  DCM   r     | IDML  r     | MRW   r/w   | PSB   r/w   | WEBM  r
  DCP   r/w   | IIQ   r/w   | MXF   r     | PSD   r/w   | WMA   r
  DCR   r     | IND   r/w   | NEF   r/w   | PSP   r     | WMV   r
  DFONT r     | INX   r     | NRW   r/w   | QTIF  r     | WV    r
  DIVX  r     | ITC   r     | NUMBERS r   | RA    r     | X3F   r/w
  DJVU  r     | J2C   r     | ODP   r     | RAF   r/w   | XCF   r
  DLL   r     | JNG   r/w   | ODS   r     | RAM   r     | XLS   r
  DNG   r/w   | JP2   r/w   | ODT   r     | RAR   r     | XLSX  r
  DOC   r     | JPEG  r/w   | OFR   r     | RAW   r/w   | XMP   r/w/c
  DOCX  r     | K25   r     | OGG   r     | RIFF  r     | ZIP   r
  DV    r     | KDC   r     | OGV   r     | RSRC  r     |
  DVB   r     | KEY   r     | ORF   r/w   | RTF   r     |
  DYLIB r     | LA    r     | OTF   r     | RW2   r/w   |
  EIP   r     | LNK   r     | PAC   r     | RWL   r/w   |

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  APE            r
  ICC Profile    r/w/c  |  DICOM          r    |  Vorbis         r
  MIE            r/w/c  |  Flash          r    |  SPIFF          r
  JFIF           r/w/c  |  FlashPix       r    |  DjVu           r
  Ducky APP12    r/w/c  |  QuickTime      r    |  M2TS           r
  PDF            r/w/c  |  Matroska       r    |  PE/COFF        r
  PNG            r/w/c  |  GeoTIFF        r    |  AVCHD          r
  Canon VRD      r/w/c  |  PrintIM        r    |  ZIP            r
  Nikon Capture  r/w/c  |  ID3            r    |  (and more)

See html/index.html for more details about ExifTool features.

%prep
%setup -n Image-ExifTool-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=%{?buildroot:%{buildroot}}
find $RPM_BUILD_ROOT -name perllocal.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes html
/usr/lib/perl5/*
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Tue May 09 2006 - Niels Kristian Bech Jensen <nkbj@mail.tele.dk>
- Spec file fixed for Mandriva Linux 2006.
* Mon May 08 2006 - Volker Kuhlmann <VolkerKuhlmann@gmx.de>
- Spec file fixed for SUSE.
- Package available from: http://volker.dnsalias.net/soft/
* Sat Jun 19 2004 Kayvan Sylvan <kayvan@sylvan.com> - Image-ExifTool
- Initial build.
