from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    max_new_tokens=100,
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)