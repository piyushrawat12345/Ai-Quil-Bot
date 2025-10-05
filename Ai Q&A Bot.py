from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "difference between user and ai\n"
      },
      {
        "role": "assistant",
        "content": "### User vs. AI – A Quick Comparison\n\n| Feature | **User (Human)** | **AI (Artificial Intelligence)** |\n|---------|------------------|---------------------------------|\n| **Consciousness** | Self‑aware, experiences emotions, subjective feelings. | No consciousness or emotions; processes data based on programming. |\n| **Learning** | *Incremental, experiential, contextual.* Learns from personal experience, social cues, and introspection. | *Data‑driven, pattern‑based.* Trained on large datasets; updates only when retrained or fine‑tuned. |\n| **Creativity** | Generates novel ideas from personal insights, imagination, and emotional depth. | Generates “creative” outputs by recombining patterns seen in training data; can mimic creativity but lacks genuine intent. |\n| **Decision‑making** | Influenced by values, ethics, long‑term goals, and social context. | Follows objective functions (e.g., maximize accuracy, revenue) defined by developers; no personal values. |\n| **Adaptability** | Rapidly shifts between tasks, cultures, languages, and environments. | Adaptable only within the bounds of its training; may struggle with out‑of‑domain inputs. |\n| **Memory** | Unlimited contextual memory within a conversation or interaction. | Short‑term memory limited to context window; long‑term memory only if explicitly stored and retrieved. |\n| **Bias & Fairness** | Can be reflective, self‑critical, and change biases over time. | Biases are inherited from training data; must be actively mitigated. |\n| **Error Handling** | Can ask clarifying questions, admit uncertainty, and correct mistakes on the fly. | Errors often silent; may produce confident but incorrect outputs. |\n| **Speed & Scale** | Limited by human cognitive speed and capacity. | Processes millions of operations per second; scales to massive datasets. |\n| **Ethics & Responsibility** | Holds moral agency; can be held accountable for actions. | No moral agency; responsibility lies with creators, deployers, and users. |\n\n#### Bottom Line\n- **Users** bring intentionality, emotion, and ethical judgment to interactions.  \n- **AIs** bring speed, consistency, and pattern recognition but lack subjective experience and moral autonomy.  \n\nUnderstanding these differences helps set realistic expectations and design better human‑AI collaborations."
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
