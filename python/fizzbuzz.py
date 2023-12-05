# Aquí programa una función que resuelva el problema 1 FizzBuzz


def FizzBuzz():
    # Itera sobre los números del 1 al 100 (ambos inclusive)
    for i in range(1, 101):
        # Comprueba si el número es divisible por 3 y 5 al mismo tiempo
        if i % 3 == 0 and i % 5 == 0:
            # Imprime "FizzBuzz" seguido del número
            print(f"FizzBuzz: {i}")
        # Comprueba si el número es divisible por 3 solamente
        elif i % 3 == 0:
            # Imprime "Fizz" seguido del número
            print(f"Fizz: {i}")
        # Comprueba si el número es divisible por 5 solamente
        elif i % 5 == 0:
            # Imprime "Buzz" seguido del número
            print(f"Buzz: {i}")


# Llama a la función FizzBuzz para ejecutarla
FizzBuzz()
