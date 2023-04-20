import os
import base64

# KIVY
try:
    from kivy.config import Config
    # Tamanho da tela da aplicação
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '600')
    # impedir que o usuário ajuste o tamanho da tela
    Config.set('graphics', 'resizable', False)

    from kivy.app import App
    from kivy.uix.image import Image
    from kivy.uix.screenmanager import Screen
    from kivy.properties import StringProperty
    # ====================== END OF KIVY

except ModuleNotFoundError:
    os.system('python.exe -m pip install --upgrade pip')
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')

try:
    import qrcode

except ModuleNotFoundError:
    os.system('pip install qrcode')

# ====================== END OF KIVY

finally:
    from tkinter import messagebox
    # IMPORT [message.py]
    from msg import message
    # ====================== IMPORT
    class MainPanel(Screen):
        """
            Classe principal dos widgets.

            ...

            VARIABLES
            ----------

                pass
        """
        msg_subtitle = StringProperty("---")
        link_set = StringProperty("Esperando...")
        image_source = StringProperty("assets/code/url_qrcode.png")

        def qrcode_generator(self, msg_ctx:str, color:str):
            """
                Gerar um QR Code e salvar em uma pasta.

                ...

                VARIABLES
                ----------
                ├── msg_input : string
                │     └── link escolhido pelo usuário.
                │
                └── color : string
                      └── cor de escolha do usuário.
            """

            # https://kivy.org/ [teste link]

            qr_code = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=15,
                border=4
            )

            qr_code.add_data(msg_ctx)
            qr_code.make(fit=True)

            if color == "":
                img = qr_code.make_image(
                    fill_color="#111111",
                    back_color="white"
                )

            else:
                img = qr_code.make_image(
                    fill_color=color,
                    back_color="white"
                )

            img.save('assets/code/url_qrcode.png')

            messagebox.showinfo(
                title="QR Code",
                message="O QR Code foi gerado com sucesso!"
            )

            link_encode = base64.b64encode((msg_ctx).encode('ascii'))

            self.link_set = "LINK DA CONVERSÃO"
            self.msg_subtitle = str(link_encode)[2:-1]
            self.image_source = 'assets/code/url_qrcode.png'

            image_dir = Image(
                source=self.image_source
            )

            image_dir.reload()
        
        def selected_link(self, msg:str):
            """
                Pegar o link que o usuário escolheu para a conversão.
                
                ...

                ARGS
                ----------
                └── msg : string
                      └── link do usuário.

            """

            if msg == "":
                messagebox.showerror(
                    title="Nenhum link inserido",
                    message="Você precisa colocar um link para realizar a conversão."
                )
            
            else:
                color = "#111111"
                self.qrcode_generator(msg, color)

    class QrCodeGenerator(App):
        """
            Classe principal dos widgets.

            ...

            Functions
            ----------
            └── build : any
                    ├── title : Um novo título ao programa
                    └── icon : ícone da aplicação
                    
                    return super().build()

        """

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