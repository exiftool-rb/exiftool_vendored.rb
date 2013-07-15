# coding: utf-8
require 'bundler/gem_tasks'

require 'yard'
YARD::Rake::YardocTask.new do |t|
  t.files = ['lib/**/*.rb', 'README.md']
end

require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs.push "lib"
  t.libs.push "test"
  t.pattern = 'test/**/*_test.rb'
  t.verbose = true
end

task :default => :test

task :update_exiftool do

  require 'open-uri'
  require 'nokogiri'

  doc = Nokogiri::HTML(open('http://owl.phy.queensu.ca/~phil/exiftool/rss.xml'))
  latest = doc.xpath('//rss/channel/item/enclosure').first
  fail 'Failed to parse the exiftool/rss.xml' if latest.nil?

  latest_url = latest[:url]
  basename = latest_url.split('/').last
  src_file = File.expand_path("../downloads/#{basename}", __FILE__)

  unless File.exist?(src_file)
    puts "Downloading #{latest_url}…"
    File.open(src_file, "wb") do |io_out|
      open(latest_url, 'rb') do |io_in|
        io_out.write(io_in.read)
      end
    end
  end

  puts 'Unpacking …'
  dest_dir = File.expand_path('../bin', __FILE__)
  FileUtils.remove_entry_secure(dest_dir) if File.exist?(dest_dir)
  FileUtils.mkdir(dest_dir)
  `tar xzf #{src_file} -C #{dest_dir}`
  `git add bin downloads`

  puts 'Remember to update the version!'
end
