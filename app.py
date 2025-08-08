import streamlit as st
from core.crew_setup import run_crew

st.set_page_config(page_title="Mental Health Support Bot", layout="centered")
st.title("🧠 Mental Health Support Bot")
st.write("Get quick emotional support, empathy, and self-care tips.")

user_input = st.text_input("How are you feeling today?")

# Mood-specific jokes/notes
mood_responses = {
    {
    "overwhelmed": {
        "emoji": "🌊",
        "note": "Like waves, everything feels big right now — but you’re the shore, steady and strong. One thing at a time 🌱"
    },
    "unmotivated": {
        "emoji": "🛋️",
        "note": "Even rockets stay still before launch. Rest is part of the journey — your spark isn’t gone, just recharging 🔋"
    },
    "hopeful": {
        "emoji": "🌈",
        "note": "That little light inside you? It’s peeking through — just like sun after rain. Keep going 🌤️"
    },
    "frustrated": {
        "emoji": "😤",
        "note": "Ugh moments are real — scream into the void (or a snack), then try again with a side of patience 🍪"
    },
    "drained": {
        "emoji": "🥱",
        "note": "Running on low? Plug into silence, music, or a cozy blanket. You’re not a machine, you're magic 🪄"
    },
    "default": {
        "emoji": "🌟",
        "note": "Feelings come and go like seasons — but you're consistently enough. Breathe, you’re doing okay 💫"
    }
}

}

def detect_mood(text):
    
   text = text.lower()
   if "overwhelmed" in text or "too much" in text or "drowning" in text:
    return "overwhelmed"
   elif "tired" in text or "lazy" in text or "unmotivated" in text or "can't do it" in text:
    return "unmotivated"
   elif "hopeful" in text or "optimistic" in text or "looking forward" in text:
    return "hopeful"
   elif "frustrated" in text or "stuck" in text or "annoyed" in text:
    return "frustrated"
   elif "drained" in text or "exhausted" in text or "burnt out" in text:
    return "drained"
   return "default"


if st.button("Get Support"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = run_crew(user_input)

            outputs = []
            if hasattr(result, "tasks_output"):
                for task_output in result.tasks_output:
                    raw_text = getattr(task_output, "raw", "").strip()
                    if raw_text:
                        outputs.append(raw_text)

            if outputs:
                mood = detect_mood(user_input)
                mood_data = mood_responses.get(mood, mood_responses["default"])

                st.success("Here's your support:")
                st.write(f"- {mood_data['emoji']} Mood Insight: {outputs[0]}")  # Mood Analyzer
                st.write(f"- ❤️ Support: {outputs[1]}")  # Companion
                st.write(f"- 🌱 Self-Care Tip: {outputs[2]}")  # Self-care
                st.write(f"- 🌈 Bonus Thought: {mood_data['note']}")
            else:
                st.warning("Couldn't generate support. Please try again.")
    else:
        st.warning("Please enter something about how you're feeling.")


