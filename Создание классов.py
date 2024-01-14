import doctest


class Car:
    def __init__(self, maximum_speed: float, current_speed: float): #maximum_speed - максимальная скорость, current_speed - текущая скорсть

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

    def car_standing(self) -> bool: #проверяет,стоит ли машина
        """
            Примеры:
                car = Car(150, 0)
                car.car_standing()
        """

    def new_speed(self, increased_speed: float): # увеличение скорости

        if not isinstance(increased_speed, (int, float)):
            raise TypeError # добавленная скорость быть типа int или float
        if increased_speed < 0:
            raise ValueError # добавленная скокрость не может быть отрицательной
        if self.current_speed + increased_speed > self.maximum_speed:
            raise ValueError #новая текущая скорсть не может превыщать максимальную
        """
        Примеры: 
            car = Car(150, 0)
            car.new_speed(125)
        """
        self.current_speed += increased_speed


class Сomputer:
    def __init__(self, manufacturer: str, ram: int):
        """
        manufacturer: Производитель компьютера.
        ram : Объем оперативной памяти .
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
    def __init__(self, initial_minutes: int):  # initial_minutes - начальное количество минут

        if not isinstance(initial_minutes, int):
            raise TypeError("Начальное количество минут должно быть целым числом")
        if initial_minutes < 0:
            raise ValueError("Начальное количество минут не может быть отрицательным")

        self.remaining_minutes = initial_minutes  # оставшееся количество минут

    def is_time_up(self) -> bool:  # проверяет, закончилось ли отведенное время
        """
        Примеры:
            timer = Timer(0)
            timer.is_time_up()
        """


    def add_minutes(self, additional_minutes: int) -> None:  # добавляет дополнительные минуты к таймеру
        """
        Примеры:
            timer = Timer(5)
            timer.add_minutes(10)
        """
        if not isinstance(additional_minutes, int):
            raise TypeError("Дополнительное кол-во минут должно быть целым числом")
        if additional_minutes < 0:
            raise ValueError("Дополнительное кол-во минут не может быть отрицательным")

        self.remaining_minutes += additional_minutes

    def reset_timer(self, new_minutes: int) -> None:  # сбрасывает таймер на новое кол-во минут
        """
        Примеры:
            timer = Timer(10)
            timer.reset_timer(15)
        """
        if not isinstance(new_minutes, int):
            raise TypeError("Новое количество минут должно быть целым числом")
        if new_minutes < 0:
            raise ValueError("Новое количество минут не может быть отрицательным")

        self.remaining_minutes = new_minutes


# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
