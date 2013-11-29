require 'test_helper'

describe ExiftoolVendored do

  DUMP_RESULTS = false

  it 'raises NoSuchFile for missing files' do
    proc { Exiftool.new('no/such/file') }.must_raise Exiftool::NoSuchFile
  end

  it 'raises NotAFile for directories' do
    proc { Exiftool.new(File.dirname(__FILE__)) }.must_raise Exiftool::NotAFile
  end

  it 'no-ops with no files' do
    e = Exiftool.new([])
    e.errors?.must_be_false
  end

  it 'has errors with files without EXIF headers' do
    e = Exiftool.new('Gemfile')
    e.errors?.must_be_true
  end

  describe 'single-get' do
    it 'responds with known correct responses' do
      Dir['test/*.jpg'].each do |filename|
        e = Exiftool.new(filename)
        validate_result(e, filename)
      end
    end
  end

  describe 'multi-get' do
    def test_multi_matches
      samples = %w[Canon.jpg NikonD70.jpg FujiFilm.jpg Olympus.jpg Panasonic.jpg Sony.jpg]
      filenames = Dir['bin/*/t/images/*.jpg'].
        select { |ea| samples.include?(File.basename(ea)) }
      e = Exiftool.new(filenames)
      filenames.each { |f| validate_result(e.result_for(f), f) }
    end
  end

  def validate_result(result, filename)
  basename = File.basename(filename)
    yaml_file = "test/expected/#{basename}.yaml"
    exif = result.to_hash.select{|k,v| !IGNORABLE_KEYS.include?(k) }
    File.open(yaml_file, 'w') { |out| YAML.dump(exif, out) } if DUMP_RESULTS
    e = File.open(yaml_file) { |f| YAML::load(f) }
    bad_keys = exif.keys.select do |k|
      next if ignorable_key?(k)
      expected = e[k]
      next if expected.nil? # older version of exiftool
      actual = exif[k]
      if expected.is_a?(String)
        expected.downcase!
        actual.downcase!
      end
      expected != actual
    end
    fail "#{filename}[#{bad_keys.join(',')}] didn't match" unless bad_keys.empty?
  end

  # These are expected to be different on travis, due to different paths, filesystems, or
  # exiftool version differences.
  # fov and hyperfocal_distance, for example, are different between v8 and v9.
  IGNORABLE_KEYS = [
    :circle_of_confusion,
    :create_date,
    :date_time_original,
    :directory,
    :exif_tool_version,
    :file_access_date,
    :file_inode_change_date,
    :file_modify_date,
    :file_permissions,
    :fov,
    :hyperfocal_distance,
    :modify_date,
    :nd_filter,
    :source_file
  ]

  IGNORABLE_PATTERNS = [
    /.*\-ml-\w\w-\w\w$/, # < translatable
    /35efl$/ # < 35mm Effective focal length, whose calculation was changed between v8 and v9.
  ]

  def ignorable_key?(key)
    IGNORABLE_KEYS.include?(key) || IGNORABLE_PATTERNS.any? { |ea| key.to_s =~ ea }
  end
end
