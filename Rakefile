# coding: utf-8
require 'bundler/gem_tasks'

require 'yard'
YARD::Rake::YardocTask.new do |t|
  t.files = ['lib/**/*.rb', 'README.md']
end

require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs.push 'lib'
  t.libs.push 'test'
  t.pattern = 'test/**/*_test.rb'
  t.verbose = true
end

task :default => :test

desc 'Update the vendored Exiftool to the latest version'
task :update_exiftool do
  require 'open-uri'
  require 'nokogiri'
  require 'pathname'

  doc = Nokogiri::HTML(open('http://owl.phy.queensu.ca/~phil/exiftool/rss.xml'))
  latest = doc.xpath('//rss/channel/item/enclosure').select do |ea|
    ea[:url] && ea[:url].end_with?('.tar.gz')
  end.sort.first
  fail 'Failed to parse the exiftool/rss.xml' if latest.nil?

  latest_url = latest[:url]
  basename = latest_url.split('/').last

  tgz = Pathname.new(File.expand_path("../downloads/#{basename}", __FILE__))
  tgz.parent.mkpath

  if tgz.exist? && tgz.size > 0
    puts "Assuming #{tgz} is valid…"
  else
    puts "Downloading #{latest_url} to #{tgz}…"
    tgz.open('wb') do |io_out|
      open(latest_url, 'rb') do |io_in|
        io_out.write(io_in.read)
      end
    end
  end

  dest_dir = File.expand_path('../bin', __FILE__)
  FileUtils.remove_entry_secure(dest_dir) if File.exist?(dest_dir)
  FileUtils.mkdir(dest_dir)
  `tar xzf #{tgz.realpath.to_s} -C #{dest_dir}`
  # Move contents out of the subdirectory and into bin directly:
  `mv #{dest_dir}/Image-ExifTool-*/* #{dest_dir}`
  `rmdir #{dest_dir}/Image-ExifTool-*`

  require 'exiftool_vendored/version_extractor'
  new_version = ExiftoolVendored.extract_version
  puts "New rubygem version is #{new_version}!"

  ver_rb = Pathname.new(File.expand_path("../lib/exiftool_vendored/version.rb", __FILE__))
  ver_rb.open("w") do |io|
    io.write <<-EOF
module ExiftoolVendored
  VERSION = Gem::Version.new('#{new_version}')
end
    EOF
  end
  `git add --all #{dest_dir}`
  puts "Added #{dest_dir}. Now `rake test`, `git commit -a` and `rake release`…"
end
