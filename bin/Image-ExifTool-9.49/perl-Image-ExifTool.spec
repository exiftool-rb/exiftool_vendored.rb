Summary: perl module for image data extraction
Name: perl-Image-ExifTool
Version: 9.49
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
  3FR   r     | EIP   r     | LNK   r     | PAC   r     | RWL   r/w
  3G2   r/w   | EPS   r/w   | M2TS  r     | PAGES r     | RWZ   r
  3GP   r/w   | ERF   r/w   | M4A/V r/w   | PBM   r/w   | RM    r
  ACR   r     | EXE   r     | MEF   r/w   | PCD   r     | SO    r
  AFM   r     | EXIF  r/w/c | MIE   r/w/c | PDF   r/w   | SR2   r/w
  AI    r/w   | EXR   r     | MIFF  r     | PEF   r/w   | SRF   r
  AIFF  r     | F4A/V r/w   | MKA   r     | PFA   r     | SRW   r/w
  APE   r     | FFF   r/w   | MKS   r     | PFB   r     | SVG   r
  ARW   r/w   | FLA   r     | MKV   r     | PFM   r     | SWF   r
  ASF   r     | FLAC  r     | MNG   r/w   | PGF   r     | THM   r/w
  AVI   r     | FLV   r     | MODD  r     | PGM   r/w   | TIFF  r/w
  BMP   r     | FPF   r     | MOS   r/w   | PLIST r     | TORRENT r
  BTF   r     | FPX   r     | MOV   r/w   | PICT  r     | TTC   r
  CHM   r     | GIF   r/w   | MP3   r     | PMP   r     | TTF   r
  COS   r     | GZ    r     | MP4   r/w   | PNG   r/w   | VRD   r/w/c
  CR2   r/w   | HDP   r/w   | MPC   r     | PPM   r/w   | VSD   r
  CRW   r/w   | HDR   r     | MPG   r     | PPT   r     | WAV   r
  CS1   r/w   | HTML  r     | MPO   r/w   | PPTX  r     | WDP   r/w
  DCM   r     | ICC   r/w/c | MQV   r/w   | PS    r/w   | WEBP  r
  DCP   r/w   | IDML  r     | MRW   r/w   | PSB   r/w   | WEBM  r
  DCR   r     | IIQ   r/w   | MXF   r     | PSD   r/w   | WMA   r
  DFONT r     | IND   r/w   | NEF   r/w   | PSP   r     | WMV   r
  DIVX  r     | INX   r     | NRW   r/w   | QTIF  r/w   | WV    r
  DJVU  r     | ITC   r     | NUMBERS r   | RA    r     | X3F   r/w
  DLL   r     | J2C   r     | ODP   r     | RAF   r/w   | XCF   r
  DNG   r/w   | JNG   r/w   | ODS   r     | RAM   r     | XLS   r
  DOC   r     | JP2   r/w   | ODT   r     | RAR   r     | XLSX  r
  DOCX  r     | JPEG  r/w   | OFR   r     | RAW   r/w   | XMP   r/w/c
  DPX   r     | K25   r     | OGG   r     | RIFF  r     | ZIP   r
  DV    r     | KDC   r     | OGV   r     | RSRC  r     |
  DVB   r/w   | KEY   r     | ORF   r/w   | RTF   r     |
  DYLIB r     | LA    r     | OTF   r     | RW2   r/w   |

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
