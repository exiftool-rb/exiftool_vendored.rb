Summary: perl module for image data extraction
Name: perl-Image-ExifTool
Version: 9.60
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
  3FR   r     | EIP   r     | LA    r     | OTF   r     | RW2   r/w
  3G2   r/w   | EPS   r/w   | LNK   r     | PAC   r     | RWL   r/w
  3GP   r/w   | ERF   r/w   | M2TS  r     | PAGES r     | RWZ   r
  ACR   r     | EXE   r     | M4A/V r/w   | PBM   r/w   | RM    r
  AFM   r     | EXIF  r/w/c | MEF   r/w   | PCD   r     | SEQ   r
  AI    r/w   | EXR   r     | MIE   r/w/c | PDF   r/w   | SO    r
  AIFF  r     | EXV   r/w/c | MIFF  r     | PEF   r/w   | SR2   r/w
  APE   r     | F4A/V r/w   | MKA   r     | PFA   r     | SRF   r
  ARW   r/w   | FFF   r/w   | MKS   r     | PFB   r     | SRW   r/w
  ASF   r     | FLA   r     | MKV   r     | PFM   r     | SVG   r
  AVI   r     | FLAC  r     | MNG   r/w   | PGF   r     | SWF   r
  BMP   r     | FLV   r     | MODD  r     | PGM   r/w   | THM   r/w
  BTF   r     | FPF   r     | MOS   r/w   | PLIST r     | TIFF  r/w
  CHM   r     | FPX   r     | MOV   r/w   | PICT  r     | TORRENT r
  COS   r     | GIF   r/w   | MP3   r     | PMP   r     | TTC   r
  CR2   r/w   | GZ    r     | MP4   r/w   | PNG   r/w   | TTF   r
  CRW   r/w   | HDP   r/w   | MPC   r     | PPM   r/w   | VRD   r/w/c
  CS1   r/w   | HDR   r     | MPG   r     | PPT   r     | VSD   r
  DCM   r     | HTML  r     | MPO   r/w   | PPTX  r     | WAV   r
  DCP   r/w   | ICC   r/w/c | MQV   r/w   | PS    r/w   | WDP   r/w
  DCR   r     | IDML  r     | MRW   r/w   | PSB   r/w   | WEBP  r
  DFONT r     | IIQ   r/w   | MXF   r     | PSD   r/w   | WEBM  r
  DIVX  r     | IND   r/w   | NEF   r/w   | PSP   r     | WMA   r
  DJVU  r     | INX   r     | NRW   r/w   | QTIF  r/w   | WMV   r
  DLL   r     | ITC   r     | NUMBERS r   | RA    r     | WV    r
  DNG   r/w   | J2C   r     | ODP   r     | RAF   r/w   | X3F   r/w
  DOC   r     | JNG   r/w   | ODS   r     | RAM   r     | XCF   r
  DOCX  r     | JP2   r/w   | ODT   r     | RAR   r     | XLS   r
  DPX   r     | JPEG  r/w   | OFR   r     | RAW   r/w   | XLSX  r
  DV    r     | K25   r     | OGG   r     | RIFF  r     | XMP   r/w/c
  DVB   r/w   | KDC   r     | OGV   r     | RSRC  r     | ZIP   r
  DYLIB r     | KEY   r     | ORF   r/w   | RTF   r     |

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  DPX            r
  ICC Profile    r/w/c  |  DICOM          r    |  APE            r
  MIE            r/w/c  |  Flash          r    |  Vorbis         r
  JFIF           r/w/c  |  FlashPix       r    |  SPIFF          r
  Ducky APP12    r/w/c  |  QuickTime      r    |  DjVu           r
  PDF            r/w/c  |  Matroska       r    |  M2TS           r
  PNG            r/w/c  |  MXF            r    |  PE/COFF        r
  Canon VRD      r/w/c  |  PrintIM        r    |  AVCHD          r
  Nikon Capture  r/w/c  |  FLAC           r    |  ZIP            r
  GeoTIFF        r/w/c  |  ID3            r    |  (and more)

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
%{_libdir}/perl5/*
/usr/share/*/*
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Tue May 06 2014 - Norbert de Rooy <nsrderooy@gmail.com>
- Spec file fixed for Redhat 6
* Tue May 09 2006 - Niels Kristian Bech Jensen <nkbj@mail.tele.dk>
- Spec file fixed for Mandriva Linux 2006.
* Mon May 08 2006 - Volker Kuhlmann <VolkerKuhlmann@gmx.de>
- Spec file fixed for SUSE.
- Package available from: http://volker.dnsalias.net/soft/
* Sat Jun 19 2004 Kayvan Sylvan <kayvan@sylvan.com> - Image-ExifTool
- Initial build.
