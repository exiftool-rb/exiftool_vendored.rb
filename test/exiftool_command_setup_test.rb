require 'test_helper'

describe ExiftoolVendored do
  it 'sets up Exiftool to work with the vendored command' do
    bin = File.expand_path('../../bin', __FILE__)
    expected_path = Regexp.new("#{bin}/[^/]+/exiftool")
    Exiftool.command.must_match expected_path
  end

  it 'matches the expected version' do
    ExiftoolVendored::VERSION.to_s.must_match /^#{Exiftool.exiftool_version}/
  end
end
