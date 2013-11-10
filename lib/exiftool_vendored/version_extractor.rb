module ExiftoolVendored
  PATCHLEVEL = 0

  # This is only used by the rake 'update_exiftool' task.
  def self.extract_version
    # We can't use the YAML file, because he doesn't encode it as a string,
    # so "9.40" returns as "9.4"
    dirname = Dir[File.expand_path("../../../bin/Image-ExifTool-*", __FILE__)].sort.last
    basename = File.basename(dirname)
    version = basename["Image-ExifTool-".length..-1]
    unless version.to_f > 0
      raise "version is missing from #{dirname}"
    end
    "#{version}.#{PATCHLEVEL}"
  rescue StandardError => e
    raise "Cannot extract version: #{e}"
  end
end
