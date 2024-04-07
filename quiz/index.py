from blessings import Terminal
from openai import OpenAI 
import json


client = OpenAI(
    api_key='CHATGPT_KEY' 
)


def question_generate(topic):
    chatgpt_response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            "role": "system",
            "content": """
                Você é um desenvolvedor muito experiente com conhecimento em diferentes
                stacks e conceitos teóricos sobre programação e engenharia de software.
                Você está trabalhando em um processo de contratação e seu trabalho agora é escrever perguntas
                para uma entrevista. Cada pergunta deve ter quatro respostas possíveis e uma delas
                deve ser correta. Escreva essas perguntas no seguinte formato:
                '{"pergunta": "Pergunta", "opcoes": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"], "certa": "Opção 1"}'
            """
        }, {
            "role": "user",
            "content": f"Gere uma pergunta sobre {topic}"
        }]
    )
    content = chatgpt_response.choices[0].message.content
    return json.loads(content)

pontos = 0
term = Terminal()
topic = input(term.green + "Digite o tópico que você quer responder: ")

while topic:
    print("Carregando...")
    question = question_generate(topic)
    print(term.clear)
    print(term.bold_underline(question['pergunta']))

    for i, option in enumerate(question['opcoes'], start=1):
        print(f"{i}. {option}")
    

    user_response_index = int(input(term.blue + "Digite a sua opção[1-4]: ")) -1;

    selected = question['opcoes'][user_response_index].lower()

    right_answer = question['certa'].lower()

    if selected == right_answer:
        pontos += 1
        print(term.green(f'Você acertou! Agora você tem {pontos} pontos\n'))
    else:
        print(
            term.red(f'Você errou! A resposta correta era: "{right_answer}"\n'))
        
    continuar = input("Quer continuar? (S/n) ")
    
    if continuar.lower() == 'n':
        break

print('Fim do programa')



