from utils import ask_llama, load_histories, save_histories
from settings import SYSTEM_PROMPT


histories = load_histories()
def ask_llm(question: str, user_Id: str):
    if user_Id not in histories:
        histories[user_Id] = [SYSTEM_PROMPT]
    
    histories[user_Id].append({"role": "user", "content": question})
    try:
        response = ask_llama(histories[user_Id])
        histories[user_Id].append({"role": "assistant", "content": response})

        # Gérer historique (limite max 400 échanges)
        if len(histories[user_Id]) > 400:
            histories[user_Id] = [histories[user_Id][0]] + histories[user_Id][-40:]

        save_histories(histories)
        return response
    except Exception as e:
        return "Une erreur s'est produite."