module ExiftoolVendored
  PATCHLEVEL = 0

  # This is only used by the rake 'update_exiftool' task.
  def self.extract_version
    require 'exiftool'
    require 'exiftool_vendored'
    ExiftoolVendored.set_exiftool_command # < in case it was already run
    version = ::Exiftool.exiftool_version
    raise "version is missing from #{dirname}" unless version.to_f > 0
    "#{version}.#{PATCHLEVEL}"
  rescue StandardError => e
    raise "Cannot extract version: #{e}"
  end
end
