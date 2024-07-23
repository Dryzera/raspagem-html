import enviando_email

corpo_email = enviando_email.CriaCorpoEmail()
corpo_email.cria_e_converte_html()
msg = corpo_email.criando_mensagem()

enviando_noticias = enviando_email.EnviaEmail()
enviando_noticias.envia_email(msg)