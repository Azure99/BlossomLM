from threading import Thread

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer, BitsAndBytesConfig

MAX_INPUT_LIMIT = 2048
MODEL_NAME = "Azure99/blossom-v5-4b"
GENERATE_CONFIG = dict(
    max_new_tokens=512,
    temperature=0.5,
    top_p=0.85,
    top_k=50,
    repetition_penalty=1.05
)

quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                         bnb_4bit_compute_dtype=torch.float16)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto",
                                             quantization_config=quantization_config, low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def get_input_ids(inst, history):
    prefix = ("A chat between a human and an artificial intelligence bot. "
              "The bot gives helpful, detailed, and polite answers to the human's questions.")
    patterns = []
    for conv in history:
        patterns.append(f'\n|Human|: {conv[0]}\n|Bot|: ')
        patterns.append(f'{conv[1]}')
    patterns.append(f'\n|Human|: {inst}\n|Bot|: ')
    patterns[0] = prefix + patterns[0]

    input_ids = []
    for i, pattern in enumerate(patterns):
        input_ids += tokenizer.encode(pattern, add_special_tokens=(i == 0))
        if i % 2 == 1:
            input_ids += [tokenizer.eos_token_id]
    return input_ids


def chat(inst, history):
    with torch.no_grad():
        streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
        input_ids = get_input_ids(inst, history)
        if len(input_ids) > MAX_INPUT_LIMIT:
            yield "The input is too long, please clear the history."
            return
        generation_kwargs = dict(input_ids=torch.tensor([input_ids]).to(model.device), do_sample=True,
                                 streamer=streamer, **GENERATE_CONFIG)
        Thread(target=model.generate, kwargs=generation_kwargs).start()

        outputs = ""
        for new_text in streamer:
            outputs += new_text
            yield outputs


gr.ChatInterface(chat,
                 chatbot=gr.Chatbot(show_label=False, height=500, show_copy_button=True, render_markdown=True),
                 textbox=gr.Textbox(placeholder="", container=False, scale=7),
                 title="Blossom Web Demo",
                 description='Hello, I am Blossom, an open source conversational large language model.🌠'
                             '<a href="https://github.com/Azure99/BlossomLM">GitHub</a>',
                 theme="soft",
                 examples=["Hello", "What is MBTI", "用Python实现二分查找", "为switch写一篇小红书种草文案，带上emoji"],
                 clear_btn="🗑️Clear",
                 undo_btn="↩️Undo",
                 retry_btn="🔄Retry",
                 submit_btn="➡️Submit",
                 ).queue().launch()
