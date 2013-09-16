#------------------------------------------------------------------------------
# File:         Apple.pm
#
# Description:  Apple EXIF maker notes tags
#
# Revisions:    2013-09-13 - P. Harvey Created
#------------------------------------------------------------------------------

package Image::ExifTool::Apple;

use strict;
use vars qw($VERSION);
use Image::ExifTool::PLIST;

$VERSION = '1.00';

%Image::ExifTool::Apple::Main = (
    WRITE_PROC => \&Image::ExifTool::Exif::WriteExif,
    CHECK_PROC => \&Image::ExifTool::Exif::CheckExif,
    WRITABLE => 1,
    GROUPS => { 0 => 'MakerNotes', 2 => 'Image' },
    NOTES => 'Tags extracted from maker notes of images from the iPhone 5 with iOS 7.',
    # 0x0001 - int32s: seen 0, 1
    0x0003 => {
        Name => 'CMTime',
        SubDirectory => { TagTable => 'Image::ExifTool::Apple::CMTime' },
    },
    # 0x0004 - int32s: normally 1, but 0 for low-light images
    # 0x0005 - int32s: seen values 147-247, and 100 for blank images
    # 0x0006 - int32s: seen values 186-241, and 20 for blank images
    # 0x0007 - int32s: seen 1
    0x000a => {
        Name => 'HDRImageType',
        Writable => 'int32s',
        PrintConv => {
            3 => 'HDR Image',
            4 => 'Original Image',
        },
    },
);

# PLIST-format CMTime information (ref PH)
# (CMTime ref https://developer.apple.com/library/ios/documentation/CoreMedia/Reference/CMTime/Reference/reference.html)
%Image::ExifTool::Apple::CMTime = (
    PROCESS_PROC => \&Image::ExifTool::PLIST::ProcessBinaryPLIST,
    GROUPS => { 0 => 'MakerNotes', 2 => 'Image' },
    timescale => { Name => 'CMTimeScale' }, # (seen 1000000000 - ns)
    epoch     => { Name => 'CMTimeEpoch' }, # (seen 0)
    value     => { Name => 'CMTimeValue' }, # (should divide by CMTimeScale to get seconds)
    # observed "value" from images of one camera (iOS 7 beta):
    # DateTimeOriginal      Value
    # 2013:09:03 06:20:11	392368459447083
    # 2013:09:03 09:44:22	399081122065875
    # 2013:09:04 09:05:38	417739069527500
    # 2013:09:06 06:47:55	452906569605333
    # 2013:09:07 20:17:27	29656470330750
    # 2013:09:08 16:50:43	51536195061583
    # 2013:09:09 08:10:29	62485213304958
    # --> can't figure these out
    flags => {
        Name => 'CMTimeFlags',
        PrintConv => { BITMASK => {
            0 => 'Valid',
            1 => 'Has been rounded',
            2 => 'Positive infinity',
            3 => 'Negative infinity',
            4 => 'Indefinite',
        }},
    },
);

1;  # end

__END__

=head1 NAME

Image::ExifTool::Apple - Apple EXIF maker notes tags

=head1 SYNOPSIS

This module is loaded automatically by Image::ExifTool when required.

=head1 DESCRIPTION

This module contains definitions required by Image::ExifTool to interpret
Apple maker notes in EXIF information.

=head1 AUTHOR

Copyright 2003-2013, Phil Harvey (phil at owl.phy.queensu.ca)

This library is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

=head1 SEE ALSO

L<Image::ExifTool::TagNames/Apple Tags>,
L<Image::ExifTool(3pm)|Image::ExifTool>

=cut
