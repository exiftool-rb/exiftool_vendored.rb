module ExiftoolVendored
  PATCHLEVEL = 0

  def self.extract_version
    require 'yaml'
    meta_yml = Dir[File.expand_path("../../../bin/*/META.yml", __FILE__)].first
    return 'unknown' unless meta_yml && File.exist?(meta_yml)
    version = YAML::load_file(meta_yml)['version']
    unless version.to_f > 0
      raise "version is missing from #{meta_yml}"
    end
    "#{version}.#{PATCHLEVEL}"
  rescue StandardError => e
    raise "Cannot extract version: #{e}"
  end
end
