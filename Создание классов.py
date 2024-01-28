import doctest


class Car:
    def __init__(self, maximum_speed: float, current_speed: float):
        """
        Конструктор класса Car.

        :param maximum_speed: Максимальная скорость машины.
        :param current_speed: Текущая скорость машины.
        :raises TypeError: Если maximum_speed или current_speed не являются числами (int или float).
        :raises ValueError: Если current_speed больше maximum_speed или current_speed отрицательная.
        """
        if not isinstance(maximum_speed, (int, float)):
            raise TypeError ("Максимальная скокрость должна быть типа int или float")
        if not isinstance(current_speed, (int, float)):
            raise TypeError ("Текущая скокрость должна быть типа int или float")
        if  current_speed > maximum_speed:
            raise ValueError ("Текущая скорсть не может быть больше максимальной")
        if current_speed < 0:
            raise ValueError ("Текущая скорсть не может быть отрицательной")

        self.maximum_speed = maximum_speed #максимальная скорость
        self.current_speed = current_speed # текущая скоркость

    def car_standing(self) -> bool:
        """
        Проверяет, стоит ли машина.

        :return: True, если машина стоит, иначе False.
        """

    def new_speed(self, increased_speed: float):
        """
        Увеличивает скорость машины на указанное значение.

        :param increased_speed: Дополнительная скорость, которую нужно добавить.
        :raises TypeError: Если increased_speed не является числом (int или float).
        :raises ValueError: Если новая скорость превышает максимальную или отрицательная.
        """
        if not isinstance(increased_speed, (int, float)):
            raise TypeError # добавленная скорость быть типа int или float
        if increased_speed < 0:
            raise ValueError # добавленная скокрость не может быть отрицательной
        if self.current_speed + increased_speed > self.maximum_speed:
            raise ValueError #новая текущая скорсть не может превыщать максимальную

        self.current_speed += increased_speed


class Сomputer:
    def __init__(self, manufacturer: str, ram: int):
        """
        Конструктор класса Computer.

        :param manufacturer: Производитель компьютера.
        :param ram: Объем оперативной памяти.
        :raises TypeError: Если manufacturer не является строкой или ram не является числом (int).
        :raises ValueError: Если ram отрицательная.
        """
        if not isinstance(manufacturer, (str)):
            raise TypeError ("Произвожитель комьютера должн быть типа str")
        if not isinstance(ram, (int)):
            raise TypeError ("оперативня память должна быть типа int")

        self.manufacturer = manufacturer
        if ram < 0:
            raise ValueError("RAM не может быть отрицательнйо")
        self.ram = ram

    def power_on(self) -> None:
        """
        Включить компьютер.
        """

    def power_off(self) -> None:
        """
        Выключить компьютер.
        """


class Timer:
    def __init__(self, initial_minutes: int):
        """
        Конструктор класса Timer.

        :param initial_minutes: Начальное количество минут.
        :raises TypeError: Если initial_minutes не является числом (int).
        :raises ValueError: Если initial_minutes отрицательное.
        """
        if not isinstance(initial_minutes, int):
            raise TypeError("Начальное количество минут должно быть целым числом")
        if initial_minutes < 0:
            raise ValueError("Начальное количество минут не может быть отрицательным")

        self.remaining_minutes = initial_minutes  # оставшееся количество минут

    def is_time_up(self) -> bool:
        """
        Проверяет, закончилось ли отведенное время.

        :return: True, если время закончилось, иначе False.
        """

    def add_minutes(self, additional_minutes: int) -> None:
        """
        Добавляет дополнительные минуты к таймеру.

        :param additional_minutes: Дополнительное количество минут.
        :raises TypeError: Если additional_minutes не является числом (int).
        :raises ValueError: Если additional_minutes отрицательное.
        """
        if not isinstance(additional_minutes, int):
            raise TypeError("Дополнительное кол-во минут должно быть целым числом")
        if additional_minutes < 0:
            raise ValueError("Дополнительное кол-во минут не может быть отрицательным")

        self.remaining_minutes += additional_minutes

    def reset_timer(self, new_minutes: int) -> None:
        """
        Сбрасывает таймер на новое количество минут.

        :param new_minutes: Новое количество минут.
        :raises TypeError: Если new_minutes не является числом (int).
        :raises ValueError: Если new_minutes отрицательное.
        """
        if not isinstance(new_minutes, int):
            raise TypeError("Новое количество минут должно быть целым числом")
        if new_minutes < 0:
            raise ValueError("Новое количество минут не может быть отрицательным")

        self.remaining_minutes = new_minutes


# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить
