from app import create_app, db
from app.models import Service

# Crie a aplicação e configure o contexto
app = create_app()

with app.app_context():
    # Adicione serviços de exemplo
    services = [
        Service(
            name="Sistema de Agendamento",
            description="Permite agendar compromissos e reuniões com facilidade.",
            image_url="/static/img/service1.jpg"
        ),
        Service(
            name="Sistema de Gerenciamento Financeiro",
            description="Controle seu fluxo de caixa e mantenha as finanças organizadas.",
            image_url="/static/img/service2.jpg"
        ),
        Service(
            name="Sistema de Controle de Estoque",
            description="Gerencie seu inventário e estoque de maneira eficiente.",
            image_url="/static/img/service3.jpg"
        ),
        Service(
            name="Sistema de Atendimento ao Cliente",
            description="Facilite o suporte ao cliente com um sistema de tickets.",
            image_url="/static/img/service4.jpg"
        )
    ]

    # Adiciona os serviços ao banco de dados e faz o commit
    for service in services:
        db.session.add(service)

    db.session.commit()
    print("Serviços adicionados com sucesso!")
