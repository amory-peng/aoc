class Tile
  attr_accessor :selected, :value

  def initialize(value)
    @value = value
    @selected = false
  end
end

class Board
  attr_accessor :board
  def initialize
    @board = []
  end

  def <<(row)
    @board << row
  end

  def [](idx)
    @board[idx]
  end

  def select_tile(value)
    @board.each do |row|
      row.each do |tile|
        if tile.value == value
          tile.selected = true
          break
        end
      end
    end
  end

  def won?
    # check rows
    (0..4).each do |idx|
      return true if @board[idx].select(&:selected).length == 5
    end
    # check columns
    (0..4).each do |i|
      col = []
      (0..4).each do |j|
        col << @board[j][i]
      end
      return true if col.select(&:selected).length == 5
    end
    return false
  end

  def calc_score(num)
    @board.flatten.reject(&:selected).map(&:value).reduce(&:+) * num
  end
end

file = File.open("day4/input.txt")
file = file.readlines.map(&:chomp)
numbers = file.shift.split(",")
count = 0
boards = []
board = Board.new
file.each do |row|
  # if count is 0, make a new board
  if count == 5
    boards << board
    board = Board.new
    count = 0
  end
  next if row == ""
  tiles = row.split(" ").map { |val| Tile.new(val.to_i) }
  board << tiles
  count += 1
end

winning_number = nil
won_boards = []
count = 0
until boards.empty?
  winning_number = numbers.shift.to_i
  p "#{boards.length} remaining..."
  boards.each do |board|
    board.select_tile(winning_number)
    if board.won?
      won_boards << board
      count += 1
      p "found won_board with #{winning_number}, count: #{count}"
    end
  end
  boards = boards - won_boards
end

winning_number
won_boards.first.calc_score(42)
won_boards.last.calc_score(39)
