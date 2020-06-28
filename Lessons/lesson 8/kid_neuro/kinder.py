import random
import math

inches = 40
centemetre = 101.6

def kid_neuro(epoch, lr, accur):
    """

    :param epoch: сколько раз попробует вычислить правильное значение
    :param lr: с каким шагом наша нейросеть у нас будет обучаться
    :param accur: на сколько точный нас устроит результат
    :return:
    """
    W_coef = random.uniform(1, 3) #мы знаем, что правильный ответ это около 2.54 возьмем
    print(f"Наш первоначальный вес равен {W_coef}") #Чтобы понимать, что нам выкинул рандом

    for i in range(epoch):
        Error = centemetre - (inches * W_coef) # на сколько нейросеть ошиблась
        print(f"Наша ошибка составляет {Error}")

        if abs(Error) < accur:
            print(f"Наш итоговый результат {W_coef}")
        if Error > 0:
            W_coef += lr
            #Если ошибка положительная, нам надо наращивать вес
        elif Error < 0:
            W_coef -= lr