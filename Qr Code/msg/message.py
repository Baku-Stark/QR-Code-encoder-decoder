"""
    Código para envio de situação APLICAÇÃO PRINCIPAL (message.py)

    ...

    FUNCTIONS
    ----------
    message  : str
            Title App

    success  : str
            It is working correctly

    error    : function (message:str)
            It will send the message with the code error
"""

import os

try:
    from rich import print as rprint

except ModuleNotFoundError:
    os.system('pip install rich')

finally:
    from rich import print as rprint

    def title_set_color(msg: str):
        return f'[blue]{msg}[/blue]'
    
    def message():
        message = """
             ___          _     _                 
            | _ \  _  _  | |_  | |_    ___   _ _  
            |  _/ | || | |  _| | ' \  / _ \ | ' \  
            |_|    \_, |  \__| |_||_| \___/ |_||_|
                    |__/          

             _  __  _  
            | |/ / (_) __ __  _  _ 
            | ' <  | | \ V / | || |
            |_|\_\ |_|  \_/   \_, |
                              |__/
            """
        
        rprint(title_set_color(message))
        

    def success():
        """
            Aplicação funcionando com sucesso!
        """

        status_title = "[ON-MODE]"
        status_message = "[bold green]KIVY[/bold green] application successfully created!"
        
        rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')

    def error(message: str):
        """
            Mensagem com o erro do código.
        """

        status_title = "[ERROR]"
        status_message = f"[bold green]KIVY[/bold green] {message}"

        rprint(f'[on white] [black] {status_title} [/black] [/on white][on purple] [bold]{status_message}[/bold] [/on purple]')


    def Interrupt():
        """
            Mensagem com interrupção do código pelo teclado.
        """

        message = "B Y E ! ! !"

        status_title = "[KeyboardInterrupt]"
        status_message = f"[bold green]KIVY[/bold green] {message}"

        rprint(f'[on white] [black] {status_title} [/black] [/on white][on cyan] [bold]{status_message}[/bold] [/on cyan]')