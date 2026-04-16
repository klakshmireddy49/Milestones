import ollama

MODEL = "tinyllama"


# ================= LLM =================


def ask_llm(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"num_ctx": 1024, "num_predict": 120},
    )

    return response["message"]["content"]


# ================= MEMORY =================


class AgentMemory:

    def __init__(self, name):

        self.name = name

        self.history = []

    def add(self, data):

        self.history.append(data)

    def get(self):

        return self.history


class SharedMemory:

    def __init__(self):

        self.data = []

    def store(self, data):

        self.data.append(data)

    def get(self):

        return self.data


# ================= AGENTS =================


class ResearchAgent:

    def __init__(self):

        self.memory = AgentMemory("Research")

    def work(self, query):

        prompt = f"""

You are a research agent.

Explain this topic clearly:

{query}

Give simple explanation.

"""

        result = ask_llm(prompt)

        self.memory.add(result)

        return result


class SummarizerAgent:

    def __init__(self):

        self.memory = AgentMemory("Summarizer")

    def work(self, text):

        prompt = f"""

You are a summarizer agent.

Summarize this into 3 bullet points:

{text}

"""

        result = ask_llm(prompt)

        self.memory.add(result)

        return result


class DecisionAgent:

    def __init__(self):

        self.memory = AgentMemory("Decision")

    def work(self, summary):

        prompt = f"""

You are a decision agent.

Check this summary:

{summary}

Decide:

Is this enough information?
Answer YES or NO and why.

"""

        result = ask_llm(prompt)

        self.memory.add(result)

        return result


# ================= COORDINATOR =================


class MultiAgentSystem:

    def __init__(self):

        self.research = ResearchAgent()

        self.summarizer = SummarizerAgent()

        self.decision = DecisionAgent()

        self.shared = SharedMemory()

    def run(self, query):

        print("\nCoordinator started task\n")

        # MEMORY INFLUENCE

        past = self.shared.get()

        if past:

            query = query + " Use this previous knowledge:" + str(past)

        # RESEARCH

        print("Research Agent working...\n")

        research = self.research.work(query)

        print(research)

        self.shared.store(research)

        # SUMMARY

        print("\nSummarizer Agent working...\n")

        summary = self.summarizer.work(research)

        print(summary)

        self.shared.store(summary)

        # DECISION

        print("\nDecision Agent working...\n")

        decision = self.decision.work(summary)

        print(decision)

        self.shared.store(decision)

        return summary


# ================= EXECUTION =================

system = MultiAgentSystem()


while True:

    question = input("\nAsk topic (type exit to stop): ")

    if question == "exit":

        break

    answer = system.run(question)

    print("\nFinal Output:\n")

    print(answer)
