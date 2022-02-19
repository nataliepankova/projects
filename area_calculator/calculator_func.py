class Rectangle:
  def __init__(self, w, h):
    self.width = int(w)
    self.height = int(h)
  
  def __str__(self):
    output = f'Rectangle(width={self.width}, height={self.height})'
    return output

  def set_width(self, w):
    self.width = int(w)
  
  def set_height(self, h):
    self.height = int(h)

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return  2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    i = 1
    fig = ""
    while i <= self.height:
      fig += '*' * self.width + '\n'
      i += 1
    return fig
  
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())
    

class Square(Rectangle):
  def __init__(self, side):
    self.width = int(side)
    self.height = int(side)
  def __str__(self):
    output = f'Square(side={self.width})'
    return output
  
  def set_side(self, side):
    self.width = int(side)
    self.height = int(side)
