require 'exiftool'

module ExiftoolVendored
  def self.path_to_exiftool
    globbed = File.expand_path('../../bin/*/exiftool', __FILE__)
    Dir.glob(globbed).first
  end
end

Exiftool.command = ExiftoolVendored.path_to_exiftool
