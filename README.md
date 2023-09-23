# exiftool-vendored.rb

[![Build Status](https://app.travis-ci.com/exiftool-rb/exiftool_vendored.rb.svg?branch=master)](https://app.travis-ci.com/github/exiftool-rb/exiftool_vendored.rb/builds)
[![Build Status](https://github.com/exiftool-rb/exiftool_vendored.rb/actions/workflows/build.yml/badge.svg)](https://github.com/exiftool-rb/exiftool_vendored.rb/actions)
[![Gem Version](https://badge.fury.io/rb/exiftool_vendored.svg)](http://rubygems.org/gems/exiftool_vendored)
[![Gem Downloads](https://img.shields.io/gem/dt/exiftool_vendored.svg)](http://rubygems.org/gems/exiftool_vendored)
[![Gem Latest](https://img.shields.io/gem/dtv/exiftool_vendored.svg)](http://rubygems.org/gems/exiftool_vendored)
[![Test Coverage](https://api.codeclimate.com/v1/badges/57fa22bff558e49bf128/test_coverage)](https://codeclimate.com/github/exiftool-rb/exiftool_vendored.rb/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/57fa22bff558e49bf128/maintainability)](https://codeclimate.com/github/exiftool-rb/exiftool_vendored.rb/maintainability)

This is

- a vendored version of Phil Harvey's excellent [exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool) library, and
- a dependency on the [exiftool](https://github.com/exiftool-rb/exiftool.rb) rubygem, and
- an autoload script that configures the Exiftool gem to use the vendored version of the exiftool library.

## Ruby Support Deprecation Notice

Future releases of `exiftool_vendored` Gem will no longer support following
Ruby Versions due to their [End Of Life](https://www.ruby-lang.org/en/downloads/branches/) announcements:

- Ruby 2.4 (EOL 2020-03-31)
- Ruby 2.5 (EOL 2021-03-31)
- Ruby 2.6 (EOL 2022-04-12)
- Ruby 2.7 (EOL 2023-03-31)

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
=> "/Users/sergey/.rbenv/versions/2.7.2/lib/ruby/gems/2.7.0/gems/exiftool_vendored-12.15.0/bin/exiftool"
irb(main):003:0> Exiftool.exiftool_version
=> "12.15"
```

## Versioning

The version of this rubygem will match the major and minor versions of the exiftool library that it
vendors.
