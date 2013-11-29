require 'exiftool'

module ExiftoolVendored

  def self.path_to_exiftool_home
    Dir[File.expand_path('../../bin/*', __FILE__)].sort.last
  end

  def self.path_to_exiftool
    Dir[File.expand_path('../../bin/*/exiftool', __FILE__)].sort.last
  end

  def self.set_exiftool_command
    Exiftool.command = ExiftoolVendored.path_to_exiftool
  end
end

ExiftoolVendored.set_exiftool_command
