# frozen_string_literal: true

require 'test_helper'

describe ExiftoolVendored do
  it 'raises NoSuchFile for missing files' do
    _ { Exiftool.new('no/such/file') }.must_raise Exiftool::NoSuchFile
  end

  it 'raises NotAFile for directories' do
    _ { Exiftool.new(File.dirname(__FILE__)) }.must_raise Exiftool::NotAFile
  end

  it 'no-ops with no files' do
    e = Exiftool.new([])
    value(e.errors?).must_be_false
  end

  it 'has no errors with files without EXIF headers' do
    e = Exiftool.new('LICENSE.txt')
    validate_result(e, 'LICENSE.txt')
  end

  describe 'single-get' do
    it 'responds with known correct responses' do
      samples = %w[Canon.jpg NikonD70.jpg FujiFilm.jpg Olympus.jpg Panasonic.jpg Sony.jpg]
      Dir['bin/t/images/*.jpg'].select { |ea| samples.include?(File.basename(ea)) }.each do |filename|
        e = Exiftool.new(filename)
        validate_result(e, filename)
      end
    end
  end

  describe 'multi-get' do
    def test_multi_matches
      samples = %w[Canon.jpg NikonD70.jpg FujiFilm.jpg Olympus.jpg Panasonic.jpg Sony.jpg]
      filenames = Dir['bin/t/images/*.jpg']
                  .select { |ea| samples.include?(File.basename(ea)) }
      e = Exiftool.new(filenames)
      filenames.each { |f| validate_result(e.result_for(f), f) }
    end
  end

  def validate_result(result, filename)
    basename = File.basename(filename)
    yaml_file = "test/expected/#{basename}.yaml"
    actual = result.to_hash.delete_if { |k, _v| ignorable_key?(k) }
    File.open(yaml_file, 'w') { |out| YAML.dump(actual, out) } if ENV['DUMP_RESULTS']
    expected = File.open(yaml_file) { |f| YAML.safe_load(f, [Symbol, Date, Rational]) }
    expected.delete_if { |k, _v| ignorable_key?(k) }
    _(expected).must_equal_hash(actual)
  end

  # These are expected to be different on travis, due to different paths, filesystems, or
  # exiftool version differences.
  # fov and hyperfocal_distance, for example, are different between v8 and v9.
  IGNORABLE_KEYS = %i[
    circle_of_confusion
    directory
    exif_tool_version
    file_access_date
    file_access_date_civil
    file_inode_change_date
    file_inode_change_date_civil
    file_modify_date
    file_modify_date_civil
    file_permissions
    intelligent_contrast
    max_focal_length
    min_focal_length
    source_file
    thumbnail_image
    af_area_mode
    blue_trc
    dof
    file_type_extension
    fov
    green_trc
    hyperfocal_distance
    lens_type
    long_focal
    maker_note_unknown_binary
    measurement_geometry
    megapixels
    nd_filter
    red_trc
    short_focal
    strip_byte_counts
    strip_offsets
    warning
  ].freeze

  puts "Ignoring #{IGNORABLE_KEYS.size} keys."

  IGNORABLE_PATTERNS = [
    /.*\-ml-\w\w-\w\w$/, # < translatable
    /35efl$/ # < 35mm Effective focal length, whose calculation was changed between v8 and v9.
  ].freeze

  def ignorable_key?(key)
    IGNORABLE_KEYS.include?(key) || IGNORABLE_PATTERNS.any? { |ea| key.to_s =~ ea }
  end
end
