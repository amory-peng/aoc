class Entry

  attr_accessor :patterns, :outputs, :map, :decoded_output

  def initialize(patterns, outputs)
    @patterns = patterns
    @outputs = outputs
    @map = {}
    @decoded_output = []
  end

  def decode_easy!
    outputs.each_with_index do |output, idx|
      arr = output.split('')
      decoded = nil
      case output.length
      when 2
        decoded = 1
      when 4
        decoded = 4
      when 3
        decoded = 7
      when 7
        decoded = 8
      end
      if decoded
        map[decoded] = arr
        decoded_output[idx] = decoded
      else
        decoded_output[idx] = output
      end
    end
  end

  def decode_hard!
    patterns.each do |pattern|
      arr = pattern.split('')
      decoded = nil
      # 1, 4, 7, 8
      case pattern.length
      when 2
        decoded = 1
      when 4
        decoded = 4
      when 3
        decoded = 7
      when 7
        decoded = 8
      end
      map[decoded] = arr if decoded
    end
    # 0, 6, 9
    patterns6 = patterns.select { |p| p.length == 6 }
    # 2, 3, 5
    patterns5 = patterns.select { |p| p.length == 5 }
    # 9 includes 7 and 4
    map[9] = patterns6.find do |pattern|
      arr = pattern.split('')
      (map[4] - arr).empty?  && (map[7] - arr).empty?
    end.split('')
    # 0 includes 1, 6 doesnt
    map[0], map[6] = (patterns6 - [map[9].join]).partition { |p| (map[1] - p.split('')).empty? }.map {|p| p[0].split('')}
    # 3 includes 1
    map[3] = patterns5.find do |p|
      arr = p.split('')
      (map[1] - arr).empty?
    end.split('')
    # 2 + 4 = 0
    map[2], map[5] = (patterns5 - [map[3].join]).partition { |p| (map[0] - map[4] - p.split('')).empty? }.map {|p| p[0].split('')}
  end

  def decode_outputs
    map.each { |_, v| v.sort! }
    outputs.each do |output|
      arr = output.split('')
      map.each do |k, v|
        decoded_output << k if arr.sort == v
      end
    end
    decoded_output
  end
end

def read_input(filename)
  File.open(filename).readlines.map(&:chomp)
end

def parse_file(file)
  file.map do |line|
    pattern, output = line.split(" | ")
    Entry.new(pattern.split(" "), output.split(" "))
  end
end

def solve_1
  entries = parse_file(read_input('day8/input.txt'))
  num = 0
  entries.map do |entry|
    entry.decode_easy!
    entry.decoded_output.each do |val|
      num += 1 if (0..9).include?(val)
    end
  end
  num
end

def solve_2
  entries = parse_file(read_input('day8/input.txt'))
  num = 0
  entries.each do |entry|
    entry.decode_hard!
    num += entry.decode_outputs.join.to_i
  end
  p num
end

solve_2