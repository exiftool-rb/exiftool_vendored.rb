module ExiftoolVendored

  PATCHLEVEL = 0

  def self.version
    require 'yaml'
    meta_yml = Dir[File.expand_path("../../../bin/*/META.yml", __FILE__)].first
    return 'unknown' unless meta_yml && File.exist?(meta_yml)
    version = YAML::load_file(meta_yml)['version']
    unless version.to_f > 0
      raise "version is missing from #{meta_yml}"
    end
    Gem::Version.new("#{version}.#{PATCHLEVEL}")
  rescue StandardError => e
    raise "Cannot extract version: #{e}. Please file an issue: https://github.com/mceachen/exiftool_vendored/issues"
  end

  VERSION = version
end
