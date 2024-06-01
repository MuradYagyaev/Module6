# Дополнительное практическое задание по модулю: "Наследование классов."

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, *param):
        self.__sides = []
        self.__color = [0, 0, 0]
        for i in range(self.sides_count):
            self.__sides.append(1)
        self.set_color(*param[0])
        self.set_sides(*param[1:])

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = color

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            if isinstance(self, (Circle, Triangle)):
                self.__sides = list(sides)
            elif isinstance(self, Cube):
                for i in range(self.sides_count):
                    self.__sides[i] = sides[0]

    def __is_valid_color(self, *color):
        for i in range(3):
            if color[i] < 0 or color[i] > 255:
                return False
        return True

    def __is_valid_sides(self, *sides):
        if isinstance(self, (Circle, Triangle)):
            return len(*sides) == self.sides_count
        if isinstance(self, Cube):
            return len(*sides) == 1

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter += side
        return perimeter


class Circle(Figure):
    sides_count = 1

    def __init__(self, *param):
        super().__init__(*param)
        self.__sides = super().get_sides()
        self.__set_radius()

    def __set_radius(self):
        self.__radius = self.__sides[0] / 2 / 3.14

    def get_square(self):
        return self.__sides[0] ** 2 / 4 / 3.14

    def get_radius(self):
        return self.__radius

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__sides = super().get_sides()
        self.__set_radius()


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *param):
        super().__init__(*param)
        self.__sides = super().get_sides()
        self.__set_height()

    def __set_height(self):
        self.__height = 2 * self.get_square() / self.__sides[2]

    def get_square(self):
        sp = 0
        for side in self.__sides:
            sp += side
        sp = sp / 2
        return (sp * (sp - self.__sides[0]) * (sp - self.__sides[1]) * (sp - self.__sides[2])) ** 0.5

    def get_height(self):
        return self.__height
    
    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__sides = super().get_sides()
        self.__set_height()


class Cube(Figure):
    sides_count = 12

    def __init__(self, *param):
        super().__init__(*param)

    def __set_volume(self):
        self.__volume = self.__sides[0] ** 3

    def get_volume(self):
        self.__sides = super().get_sides()
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)   # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)   # Изменится
cube1.set_color(300, 70, 15)    # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)     # Не изменится
circle1.set_sides(15)   # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Мои проверки

# Попытка создать фигуры с неверно введенными сторонами и цветами
print('----------- Мои проверки создания объектов! -----------')
circle2 = Circle((315, 15, 15), 6, 7)
triangle2 = Triangle((17, 17, 317), 5, 3, 4, 2)
cube2 = Cube((19, 419, 19), 10, 11, 12)
print('Круг, цвет:', circle2.get_color())
print('Круг, стороны:', circle2.get_sides())
print('Треугольник, цвет:', triangle2.get_color())
print('Треугольник, стороны:', triangle2.get_sides())
print('Куб, цвет:', cube2.get_color())
print('Куб, стороны:', cube2.get_sides())

print('----------- Мои проверки методов! -----------')
circle2.set_sides(10)
circle2.set_color(15, 15, 15)
triangle2.set_sides(5, 3, 4)
triangle2.set_color(17, 17, 17)
cube2.set_sides(10)
cube2.set_color(19, 19, 19)
print("Периметр круга:", len(circle2))
print('circle2 - get_color:', circle2.get_color(), ', get_sides:', circle2.get_sides())
print('triangle2 - get_color:', triangle2.get_color(), ', get_sides:', triangle2.get_sides())
print('cube2 - get_color:', cube2.get_color(), ', get_sides', cube2.get_sides())

print('----------- Мои проверки других методов! -----------')
print("Периметр круга, длина окружности:", len(circle2))
print('Радиус круга', circle2.get_radius())
print('Площадь круга:', circle2.get_square())
print("Периметр треугольника:", len(triangle2))
print('Площадь треугольника:', triangle2.get_square())
print('Высота треугольника:', triangle2.get_height())
print("Периметр куба:", len(cube2))
print('Объем куба:', cube2.get_volume())
