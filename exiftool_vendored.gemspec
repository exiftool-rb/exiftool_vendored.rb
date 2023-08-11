# frozen_string_literal: true

lib = File.expand_path('lib', __dir__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'exiftool_vendored/version'

Gem::Specification.new do |spec|
  spec.name          = 'exiftool_vendored'
  spec.version       = ExiftoolVendored::VERSION
  spec.authors       = ['Matthew McEachen', 'Sergey Morozov']
  spec.email         = %w[matthew+github@mceachen.org morozgrafix@gmail.com]
  spec.description   = 'Vendored version of exiftool'
  spec.summary       = 'Vendored version of exiftool'
  spec.homepage      = 'https://github.com/exiftool-rb/exiftool_vendored.rb'
  spec.license       = 'MIT'

  spec.metadata['rubygems_mfa_required'] = 'true'

  spec.required_ruby_version = '>= 2.7'

  spec.files         = `git ls-files -- lib bin`.split($/)

  # We don't add any spec.executables, because it's for our eyes only.

  spec.require_paths = %w[lib]

  spec.add_dependency 'exiftool', '>= 0.7.0'
end
