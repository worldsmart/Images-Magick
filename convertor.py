from PIL import ImageTk, Image, ImageFilter
import cv2
import os


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

    def detection(self):
        cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(cascade_path)
        image = cv2.imread(self.path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(10, 10)
        )
        faces_detected = "Лиц обнаружено: " + format(len(faces))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
        b,g,r = cv2.split(image)
        image = cv2.merge((r,g,b))
        self.pilImg = Image.fromarray(image)
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def contour(self):
        self.pilImg = self.pilImg.filter(ImageFilter.CONTOUR)
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def brightness(self, brightness):
        result = Image.new('RGB', self.pilImg.size)
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))

                red = int(r * brightness)
                red = min(255, max(0, red))

                green = int(g * brightness)
                green = min(255, max(0, green))

                blue = int(b * brightness)
                blue = min(255, max(0, blue))

                result.putpixel((x, y), (red, green, blue))

        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def negative(self):
        result = Image.new('RGB', self.pilImg.size)
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def white_black(self, brightness):
        result = Image.new('RGB', self.pilImg.size)
        separator = 255 / brightness / 2 * 3
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                total = r + g + b
                if total > separator:
                    result.putpixel((x, y), (255, 255, 255))
                else:
                    result.putpixel((x, y), (0, 0, 0))
        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def grayscale(self):
        result = Image.new('RGB', self.pilImg.size)
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                result.putpixel((x, y), (gray, gray, gray))
        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def sepia(self):
        result = Image.new('RGB', self.pilImg.size)
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                red = int(r * 0.393 + g * 0.769 + b * 0.189)
                green = int(r * 0.349 + g * 0.686 + b * 0.168)
                blue = int(r * 0.272 + g * 0.534 + b * 0.131)
                result.putpixel((x, y), (red, green, blue))
        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def contrast(self, coefficient):
        result = Image.new('RGB', self.pilImg.size)

        avg = 0
        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= self.pilImg.size[0] * self.pilImg.size[1]

        palette = []
        for i in range(256):
            temp = int(avg + coefficient * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for x in range(self.pilImg.size[0]):
            for y in range(self.pilImg.size[1]):
                r, g, b = self.pilImg.getpixel((x, y))
                result.putpixel((x, y), (palette[r], palette[g], palette[b]))
        self.pilImg = result
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))

    def original(self):
        self.pilImg = Image.open(self.path)
        if self.pilImg.size[0] >= self.pilImg.size[1]:
            size = (700, int(self.pilImg.size[1] / (self.pilImg.size[0] / 700)))
        else:
            size = (int(self.pilImg.size[0] / (self.pilImg.size[1] / 400)), 400)
        self.tkImg = ImageTk.PhotoImage(self.pilImg.resize(size, Image.ANTIALIAS))