from .models import Produto
from django import forms
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def envio_email(self):
        dotenv.load_dotenv()
        smtp_server = os.environ['EMAIL_HOST']
        smtp_porta = os.environ['EMAIL_PORT']
        email_remetente = os.environ['EMAIL_HOST_USER']
        senha = os.environ['EMAIL_HOST_PASSWORD']

        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = 'marciopereira@pifpaf.com.br'
        msg['Subject'] = 'Email enviado pelo app Django'
        
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        msg.attach(MIMEText(conteudo, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_porta)
        server.starttls() 

        server.login(email_remetente, senha)

        server.sendmail(email_remetente, msg['To'], msg.as_string())

        server.quit()

class ProdutoModelForm(forms.ModelForm):
    class Meta: # Classe para mandar os metadados
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
    