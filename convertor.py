from PIL import ImageTk, Image, ImageFilter


class Convertor:

    def __init__(self, path):
        self.path = path
        self.pilImg = Image.open(self.path)
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def saveAs(self, path):
        if path:
            self.pilImg = self.pilImg.convert('RGB')
            self.pilImg.save(path)

    def save(self):
        self.pilImg.save(self.path)

    def resize(self, x, y):
        self.pilImg = self.pilImg.resize((x, y), Image.ANTIALIAS)
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def blur(self, radius):
        self.pilImg = self.pilImg.filter(ImageFilter.GaussianBlur(radius=radius))
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))
