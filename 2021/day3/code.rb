require 'csv'
counts = Array.new(12, 0)
total_count = 0
CSV.foreach('day3/input.csv') do |str|
  str[0].split('').each_with_index do |letter, idx|
    counts[idx] += 1 if letter == "1"
  end
  total_count += 1
end

gamma = ""
epsilon = ""
counts.each do |num|
  if num > total_count / 2
    gamma += "1"
    epsilon += "0"
  else
    gamma += "0"
    epsilon += "1"
  end
end

gamma.to_i(2) * epsilon.to_i(2)

input = CSV.read('day3/input.csv').to_a.flatten
counts = Array.new(12, 0)
o2 = []
co2 = []
input.each do |str|
  str.split('').each_with_index do |letter, idx|
    counts[idx] += 1 if letter == "1"
  end
end

o2 = input.clone
idx = 0
until o2.length == 1
  count_1 = 0
  count_0 = 0
  o2.each do |el|
    el[idx] == '1' ? count_1 += 1 : count_0 += 1
  end
  bit = count_1 >= count_0 ? '1' : '0'
  o2.select! { |el| el[idx] == bit}
  idx += 1
end

co2 = input.clone
idx = 0
until co2.length == 1
  count_1 = 0
  count_0 = 0
  co2.each do |el|
    el[idx] == '1' ? count_1 += 1 : count_0 += 1
  end
  bit = count_1 < count_0 ? '1' : '0'
  co2.select! { |el| el[idx] == bit}
  idx += 1
end

o2[0].to_i(2) * co2[0].to_i(2)