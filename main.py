import math

def trivia_fetch(num):
    """
    Función que genera un diccionario con curiosidades sobre un número.
    """
    trivia = {
        "Número original": num,
        "Es par": num % 2 == 0,
        "Es primo": es_primo(num),
        "Raíz cuadrada": round(math.sqrt(num), 2),
        "Factorial (si es pequeño)": factorial_pequeño(num),
        "Es divisible por 3": num % 3 == 0,
    }
    return trivia

def es_primo(num):
    """
    Determina si un número es primo.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def factorial_pequeño(num):
    """
    Calcula el factorial de un número solo si es pequeño para evitar sobrecarga.
    """
    if num >= 0 and num <= 20:  # Factorial de números mayores puede ser muy grande
        return math.factorial(num)
    return "Demasiado grande para calcular"

def main():
    """
    Función principal del programa.
    """
    print("Hola alumnos y alumnas!👩‍🏫☺️")
    print("¡Bienvenidos al cuestionario interactivo!📝")
    print("Hoy aprenderemos curiosidades sobre números.👀🙌")
    
    while True:
        try:
            num = int(input("\nIntroduce un número (o escribe -1 para salir): "))
            if num == -1:
                print("¡Gracias por participar! Hasta luego.✨")
                break
            # Llamamos a trivia_fetch para obtener las curiosidades
            curiosidades = trivia_fetch(num)
            print("\nCuriosidades sobre el número:")
            for key, value in curiosidades.items():
                print(f"- {key}: {value}")
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
