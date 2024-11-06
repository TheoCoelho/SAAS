from app import create_app

app = create_app()

print("Aplicativo Flask iniciado com sucesso.")  # Verificação de inicialização

if __name__ == '__main__':
    app.run(debug=True)
