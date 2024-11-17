from openai import OpenAI
import os

client = OpenAI(
    api_key=open('token.txt').readline(),  # This is the default and can be omitted
)
def idea_to_vec(POMYSL):
    chat_completion = client.chat.completions.create(
        messages=[{
            "role":'system',
            'content':'''Choose which article should help the most in solving given problem:
                    1. Biology in AI;Understanding Biology in the Age of Artificial Intelligence;
                    2. Fine-tunning modeli;QLoRA: Efficient Finetuning of Quantized LLMs;
                    3. Modele Audio;MusicLM: Generating Music From Text;
                    4. Reinforcment Learning;Mastering Diverse Domains through World Models;
                    5. Video Generation;VideoPoet: A Large Language Model for Zero-Shot Video Generation;
                    6. Generowanie bardzo dobrych obrazów; Synthetic Data from Diffusion Models Improves ImageNet Classification;
                    7. 3D generation;3D Gaussian Splatting for Real-Time Radiance Field Rendering;
                    8. Solving problems desgriben in natural language;Tree of Thoughts: Deliberate Problem Solving with Large Language Models;
                    9. Generacja obrazkow w oparciu o tekst;PaLM 2 Technical Report;
                    10. Using Human Feedback;RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback. 
                    ALWAYS respond only one number;'''
        },
            {
                "role": "user",
                "content": POMYSL,
            }
        ],
        model="gpt-4o",
    )
    ans=chat_completion.choices[0].message.content
    return ans
def fill_gaps_from_info(pomysl):
    chat_completion = client.chat.completions.create(
        messages=[{
            "role":'system',
            'content':'''answer questions below, using given info:
            1: What is good title for that project?
            2: How much money project need?; answer only in number, 0 if not specified!!!.
            3: Explain project in a few words. 
            4: Startup or working project? answer s for startup.
            Answer in the same order, divide answers by ";"'''

        },
            {
                "role": "user",
                "content": pomysl,
            }
        ],
        model="gpt-4o",
    )
    ans=chat_completion.choices[0].message.content
    return ans
def Respond(Project_description,answer):
    chat_completion = client.chat.completions.create(
        messages=[{
            "role":'system',
            'content':f'''Zadawaj losowe standardowe pytanie do opisu projektu: {Project_description}.Odnieś się lekko do wiadomości użytkownika. Na początku mów: "Dodałem do formularza."'''
        },
            {
                "role": "user",
                "content": answer,
            }
        ],
        model="gpt-4o",
    )
    ans=chat_completion.choices[0].message.content
    return ans