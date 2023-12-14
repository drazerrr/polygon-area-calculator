class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      return "\n".join(["*" * self.width] * self.height) + "\n"

  def get_amount_inside(self, shape):
    return int(self.width / shape.width) * int(self.height / shape.height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)
    self.length = length

  def set_side(self, length):
    self.length = length
    self.width = length
    self.height = length

  def set_width(self, width):
    self.width = width
    self.length = width

  def set_height(self, height):
    self.height = height
    self.length = height

  def __str__(self):
    return f"Square(side={self.length})"
    



