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
  spec.homepage      = 'https://github.com/mceachen/vendored_exiftool'
  spec.license       = 'MIT'

  spec.files         = `git ls-files`.split($/)
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = %w(lib)

  spec.add_dependency 'exiftool'
  spec.add_development_dependency 'bundler'
  spec.add_development_dependency 'rake'
  spec.add_development_dependency 'yard'
  spec.add_development_dependency 'nokogiri'

end
