Summary: perl module for image data extraction
Name: perl-Image-ExifTool
Version: 9.33
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
  3FR   r     | EIP   r     | LA    r     | ORF   r/w   | RSRC  r
  3G2   r     | EPS   r/w   | LNK   r     | OTF   r     | RTF   r
  3GP   r     | ERF   r/w   | M2TS  r     | PAC   r     | RW2   r/w
  ACR   r     | EXE   r     | M4A/V r     | PAGES r     | RWL   r/w
  AFM   r     | EXIF  r/w/c | MEF   r/w   | PBM   r/w   | RWZ   r
  AI    r/w   | EXR   r     | MIE   r/w/c | PCD   r     | RM    r
  AIFF  r     | F4A/V r     | MIFF  r     | PDF   r/w   | SO    r
  APE   r     | FFF   r/w   | MKA   r     | PEF   r/w   | SR2   r/w
  ARW   r/w   | FLA   r     | MKS   r     | PFA   r     | SRF   r
  ASF   r     | FLAC  r     | MKV   r     | PFB   r     | SRW   r/w
  AVI   r     | FLV   r     | MNG   r/w   | PFM   r     | SVG   r
  BMP   r     | FPF   r     | MODD  r     | PGF   r     | SWF   r
  BTF   r     | FPX   r     | MOS   r/w   | PGM   r/w   | THM   r/w
  CHM   r     | GIF   r/w   | MOV   r     | PLIST r     | TIFF  r/w
  COS   r     | GZ    r     | MP3   r     | PICT  r     | TTC   r
  CR2   r/w   | HDP   r/w   | MP4   r     | PMP   r     | TTF   r
  CRW   r/w   | HDR   r     | MPC   r     | PNG   r/w   | VRD   r/w/c
  CS1   r/w   | HTML  r     | MPG   r     | PPM   r/w   | VSD   r
  DCM   r     | ICC   r/w/c | MPO   r/w   | PPT   r     | WAV   r
  DCP   r/w   | IDML  r     | MQV   r     | PPTX  r     | WDP   r/w
  DCR   r     | IIQ   r/w   | MRW   r/w   | PS    r/w   | WEBP  r
  DFONT r     | IND   r/w   | MXF   r     | PSB   r/w   | WEBM  r
  DIVX  r     | INX   r     | NEF   r/w   | PSD   r/w   | WMA   r
  DJVU  r     | ITC   r     | NRW   r/w   | PSP   r     | WMV   r
  DLL   r     | J2C   r     | NUMBERS r   | QTIF  r     | WV    r
  DNG   r/w   | JNG   r/w   | ODP   r     | RA    r     | X3F   r/w
  DOC   r     | JP2   r/w   | ODS   r     | RAF   r/w   | XCF   r
  DOCX  r     | JPEG  r/w   | ODT   r     | RAM   r     | XLS   r
  DV    r     | K25   r     | OFR   r     | RAR   r     | XLSX  r
  DVB   r     | KDC   r     | OGG   r     | RAW   r/w   | XMP   r/w/c
  DYLIB r     | KEY   r     | OGV   r     | RIFF  r     | ZIP   r

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
