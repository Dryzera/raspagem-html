from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from fazendo_raspagem import realizar_raspagem
from datetime import datetime
import os
import smtplib

load_dotenv()

CAMINHO_HTML = Path(__file__).parent / 'html_noticia.html'
horario_atual = datetime.now()
cria_horario = datetime.strftime(horario_atual, '%d/%m/%Y - %H:%M')

class CriaCorpoEmail:
    def __init__(self) -> None:
        self._my_email = os.getenv('smtp_username')
        self._password = os.getenv('smtp_password')
        self._server = os.getenv('smtp_server')
        self._port = os.getenv('smtp_port')
    
        self._from_addr = os.getenv('smtp_username')
        self._to_addr = 'CHANGE-ME' #<--------------------------------------- Defina
        self._subject = f'Noticias do Dia - {cria_horario}' 

    def cria_e_converte_html(self):
        with open(CAMINHO_HTML, 'w', encoding='utf-8') as file:
            str_html = str(realizar_raspagem())
            file.write(str_html)

    def criando_mensagem(self):
        with open(CAMINHO_HTML, 'r', encoding='utf-8') as file:
            body = file.read()

        msg = MIMEMultipart()
        msg['From'] = self._from_addr #type: ignore
        msg['To'] = self._to_addr
        msg['Subject'] = self._subject
        msg.attach(MIMEText(body, 'html', 'utf-8'))
        return msg



class EnviaEmail(CriaCorpoEmail):
    def __init__(self) -> None:
        super().__init__()
    
    def envia_email(self, msg):
        with smtplib.SMTP(host=self._server, port=self._port) as server: #type: ignore
            server.ehlo()
            server.starttls()
            server.login(self._my_email, self._password) #type: ignore
            server.send_message(msg)
            print('email enviado!')
        

if __name__ == '__main__':
    corpo = CriaCorpoEmail()
    corpo.cria_e_converte_html()
    msg = corpo.criando_mensagem()

    envia_email = EnviaEmail()
    envia_email.envia_email(msg)