# frozen_string_literal: true

# This is only used by the rake 'update_exiftool' task.
module ExiftoolVendored
  PATCHLEVEL = 2

  def self.extract_version
    require 'exiftool'
    require 'exiftool_vendored'
    ExiftoolVendored.set_exiftool_command # < in case it was already run
    version = ::Exiftool.exiftool_version
    raise "version is missing from #{dirname}" unless version.to_f.positive?

    "#{version}.#{PATCHLEVEL}"
  rescue StandardError => e
    raise "Cannot extract version: #{e}"
  end
end
