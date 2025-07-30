from stream_chat import StreamChat
from transformers import pipeline

client = StreamChat(api_key="up4p7w9q397a", api_secret="pprgdy2jpqqx34yvufsb8rz3ybh73usqyzcabqdtgkp9kqfyg2bqtyfgbau63d6n")
channel = client.channel("messaging", "6868280218b8aa0772ab72d7-686964d7777f0fc3b4cc1004")
response = channel.query(options={"messages": {"limit": 20}})
# print(response["messages"])

# messages=response["messages"]
messages = [
    {"text": "Hey everyone, are we still on for the project meeting today?", "user": {"name": "Alice"}, "created_at": "2025-07-06T10:05:00Z"},
    {"text": "Yes, I think we planned it for 2 PM. Does that still work for everyone?", "user": {"name": "Bob"}, "created_at": "2025-07-06T10:07:00Z"},
    {"text": "2 PM works for me! I’ve prepared the slides for my part.", "user": {"name": "Charlie"}, "created_at": "2025-07-06T10:08:00Z"},
    {"text": "Nice! I’ll talk about the architecture and deployment pipeline.", "user": {"name": "Alice"}, "created_at": "2025-07-06T10:10:00Z"},
    {"text": "Great, I’ll handle the UI demo and summary at the end.", "user": {"name": "Bob"}, "created_at": "2025-07-06T10:11:00Z"},
    {"text": "Should we also talk about next sprint planning in the meeting?", "user": {"name": "Charlie"}, "created_at": "2025-07-06T10:13:00Z"},
    {"text": "Yes, let’s cover that briefly at the end if we have time.", "user": {"name": "Alice"}, "created_at": "2025-07-06T10:14:00Z"},
    {"text": "Perfect, I’ll add it to the agenda. See you at 2!", "user": {"name": "Bob"}, "created_at": "2025-07-06T10:15:00Z"}
]

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

chat_text = " ".join([m["text"] for m in messages])
summary = summarizer(chat_text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]

for message in messages:
    print(f"User: {message['user']['name']} - Message: {message['text']}")
    print("---")
    
print("Summary:", summary)