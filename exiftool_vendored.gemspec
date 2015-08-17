# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'exiftool_vendored/version'

Gem::Specification.new do |spec|
  spec.name          = 'exiftool_vendored'
  spec.version       = ExiftoolVendored::VERSION
  spec.authors       = ['Matthew McEachen']
  spec.email         = %w(matthew+github@mceachen.org)
  spec.description   = %q{Vendored version of exiftool}
  spec.summary       = %q{Vendored version of exiftool}
  spec.homepage      = 'https://github.com/mceachen/exiftool_vendored'
  spec.license       = 'MIT'

  spec.files         = `git ls-files -- lib bin`.split($/)

  # We don't add any spec.executables, because it's for our eyes only.

  spec.require_paths = %w(lib)

  spec.add_dependency 'exiftool', '>= 0.7.0'
  spec.add_development_dependency 'bundler'
  spec.add_development_dependency 'rake'
  spec.add_development_dependency 'yard'
  spec.add_development_dependency 'nokogiri'
  spec.add_development_dependency 'minitest'
  spec.add_development_dependency 'minitest-great_expectations'
  spec.add_development_dependency 'minitest-reporters' unless ENV['CI']
end
