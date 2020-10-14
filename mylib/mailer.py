import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        # Digite seu email abaixo. Este e-mail será usado para enviar alertas.
        # Por exemplo, "email@gmail.com"
        self.EMAIL = ""
        # Digite a senha do email abaixo. Observe que a senha varia se você tiver
        # Verificação em 2 etapas ativada. Você pode consultar os links abaixo e criar uma senha específica para o aplicativo.
        # Google Mail tem um guia aqui: https://myaccount.google.com/lesssecureapps
        # Para contas verificadas em 2 etapas: https://support.google.com/accounts/answer/185833
        self.PASS = ""
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)

        # mensagem a ser enviada
        SUBJECT = 'ALERT!'
        TEXT = f'People limit exceeded in your building!'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # enviando o e-mail
        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
