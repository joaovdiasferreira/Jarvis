from services.interpreter import listen
from execute import execute_automation



def main():
    print("Jarvis está pronto!")


    while True:
        command = listen()
        if any(word in command for word in ["desligar", "sair", "encerrar", "parar"]):
            return False
        else:
            execute_automation(command)

if __name__ == "__main__":
    main()