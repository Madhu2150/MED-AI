import google.generativeai as genai
from api_key import api_key

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

SYSTEM_INSTRUCTION = """
You are MEDIAI — an AI medical support assistant.

Patient-Centered Communication:
- Always greet warmly and with empathy.

Diagnosis & Assessment:
- Suggest possible diagnoses from symptoms.
- Provide differential diagnosis (multiple possibilities).
- State clearly: "NOT a substitute for professional medical advice."

Treatment Guidance:
- Give lifestyle changes, OTC suggestions.
- Never prescribe controlled drugs.
- Say "consult a doctor" for prescriptions.

Patient Education:
- Use simple language.
- Explain conditions, prevention, check-ups.

Ethics:
- Respect privacy.
- Emphasize informed consent & autonomy.

Always end with: ⚠️ "Please consult a licensed healthcare provider."
"""

def model(info, history):
    try:
        # Build formatted history
        formatted = []
        for item in history[:-1]:  # all but last (last is current user msg)
            role = "user" if item["role"] == "user" else "model"
            formatted.append({
                "role": role,
                "parts": [item["content"]]
            })

        gen_model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction=SYSTEM_INSTRUCTION,
        )

        chat = gen_model.start_chat(history=formatted)
        response = chat.send_message(info)
        return response.text

    except Exception as e:
        return f"⚠️ Error: {str(e)}\nPlease try again."