import os

# KIVY
try:
    from kivy.app import App

except ModuleNotFoundError:
    os.system('python.exe -m pip install --upgrade pip')

    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

finally:
    # IMPORT [message.py]
    from msg import message

    # KIVY
    from kivy.config import Config
    # Tamanho da tela da aplicação
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '600')

    from kivy.app import App
    from kivy.uix.widget import Widget
    # ====================== END OF KIVY

    class QrCodeGenerator(App):
        def build(self):
            self.title = "QR CODE GENERATOR"
            self.icon = 'assets/img/qr_code_icon.png'
            return super().build()

    if __name__ == '__main__':
        try:
            os.system('cls')
            message.message()
            message.success()

            # ====================== KIVY
            QrCodeGenerator().run()

        except (AttributeError) as error:
            message.error(error)

        except KeyboardInterrupt:
            message.Interrupt()