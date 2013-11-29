# ExiftoolVendored

[![Build Status](https://secure.travis-ci.org/mceachen/exiftool_vendored.png?branch=master)](http://travis-ci.org/mceachen/exiftool_vendored)
[![Gem Version](https://badge.fury.io/rb/exiftool_vendored.png)](http://rubygems.org/gems/exiftool_vendored)

This is
* a vendored version of Phil Harvey's excellent [exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool) library, and
* a dependency on the [exiftool](https://github.com/mceachen/exiftool) rubygem, and
* an autoload script that configures the Exiftool gem to use the vendored version of the exiftool library.

## Installation

Add this line to your application's Gemfile:

    gem 'exiftool_vendored'

## Example

    $ exiftool
    -bash: exiftool: command not found

```ruby
irb(main):001:0> require 'exiftool_vendored'
=> true
irb(main):002:0> Exiftool.command
=> "/Users/mrm/.rbenv/versions/1.9.3-p429/lib/ruby/gems/1.9.1/gems/exiftool_vendored-9.33/bin/Image-ExifTool-9.33/exiftool"
irb(main):003:0> Exiftool.exiftool_version
=> 9.33
```

## Versioning

The version of this rubygem will match the exiftool library that it vendors.

