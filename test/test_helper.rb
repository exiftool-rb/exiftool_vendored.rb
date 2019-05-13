# frozen_string_literal: true

require 'simplecov'
SimpleCov.start do
  add_filter '/test/'
end

require 'minitest/autorun'
require 'minitest/great_expectations'
require 'yaml'
require 'pathname'
require 'exiftool_vendored'

# We need a predictable timezone offset so non-tz-offset timestamps are comparable:
ENV['TZ'] = 'UTC'

unless ENV['CI']
  require 'minitest/reporters'
  MiniTest::Reporters.use!
end

puts "Exiftool.exiftool_version = #{Exiftool.exiftool_version}"
