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

  spec.required_ruby_version = '>= 2.4'
  spec.post_install_message = '
    ***********************
    * Ruby Support Notice *
    ***********************

    Starting March 31, 2021 releases of `exiftool_vendored` Gem will no longer support following
    Ruby Versions due to their End Of Life (https://www.ruby-lang.org/en/downloads/branches/)
    - Ruby 2.4 (EOL 2020-03-31)
    - Ruby 2.5 (EOL 2021-03-31)
  '

  spec.files         = `git ls-files -- lib bin`.split($/)

  # We don't add any spec.executables, because it's for our eyes only.

  spec.require_paths = %w[lib]

  spec.add_dependency 'exiftool', '>= 0.7.0'
  spec.add_development_dependency 'bundler'
  spec.add_development_dependency 'minitest'
  spec.add_development_dependency 'minitest-great_expectations'
  spec.add_development_dependency 'minitest-reporters' unless ENV['CI']
  spec.add_development_dependency 'nokogiri'
  spec.add_development_dependency 'rake'
  spec.add_development_dependency 'rubocop'
  spec.add_development_dependency 'simplecov', '~> 0.17.1'
  spec.add_development_dependency 'simplecov-console'
  spec.add_development_dependency 'yard'
end
