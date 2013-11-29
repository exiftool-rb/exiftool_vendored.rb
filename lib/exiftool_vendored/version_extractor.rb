module ExiftoolVendored
  PATCHLEVEL = 1

  # This is only used by the rake 'update_exiftool' task.
  def self.extract_version
    require 'exiftool'
    set_exiftool_command
    version = ::Exiftool.exiftool_version
    raise "version is missing from #{dirname}" unless version.to_f > 0
    "#{version}.#{PATCHLEVEL}"
  rescue StandardError => e
    raise "Cannot extract version: #{e}"
  end
end
