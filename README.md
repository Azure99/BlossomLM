# BlossomLM

<p align="center">
    English | <a href="./README_ZH.md">简体中文</a>
</p>

<p align="center">
    <img src="https://www.rainng.com/wp-content/uploads/2024/04/logo-blossom.jpg" width="200"/>
</p>

<p align="center">
    <a href="https://blossom-chat.com/">Chat</a> |
    <a href="https://huggingface.co/Azure99">Hugging Face</a> |
    <a href="https://www.rainng.com/blossom-llm/">Blog</a>
</p>

Blossom-V7 is a family of open-weight, general-purpose multimodal models designed for local deployment. It combines efficient adaptive thinking, tool use with interleaved thinking, and image understanding. It covers everyday conversation, world knowledge, mathematics and reasoning, coding, web development, and data visualization, and supports agentic workflows through tool use.

## Key Features

- **Efficient Adaptive Thinking:** Uses always-on adaptive thinking to scale reasoning depth to task difficulty, delivering high-quality results with reasoning traces about one-quarter as long as those of Qwen3.5 and one-fifth as long as those of Qwen3.6.
- **Tool Use with Interleaved Thinking:** Reasons and makes decisions before every tool call, enabling strong performance in agentic tasks.
- **Image Understanding:** Understands image inputs alongside text.
- **Long Context:** Handles up to 262,144 tokens (256K); use 131,072 tokens (128K) for best results.
- **Faster Inference with MTP:** Supports speculative decoding via Multi-Token Prediction (MTP) in both vLLM and llama.cpp.

> **Important:** Blossom-V7 uses a custom chat template that differs from Qwen3.5's native template. Always use the bundled `chat_template`; do not replace it with a Qwen3.5 chat template or combine the two templates.

## Model Variants

| Model | Resources | Base Model |
| --- | --- | --- |
| [Blossom-V7-27B](https://huggingface.co/Azure99/Blossom-V7-27B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-27B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7-27B-GGUF) | [Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) |
| [Blossom-V7-35B-A3B](https://huggingface.co/Azure99/Blossom-V7-35B-A3B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-35B-A3B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7-35B-A3B-GGUF) | [Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) |
| [Blossom-V7-9B](https://huggingface.co/Azure99/Blossom-V7-9B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-9B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7-9B-GGUF) | [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) |

Select a variant based on your quality target, inference hardware, and memory budget:

- **27B:** The most capable dense option, intended for GPU deployments where the model's weights fit entirely in GPU memory.
- **35B-A3B:** The throughput-oriented option for CPU or hybrid CPU/GPU inference, offering a practical balance of quality and speed even with partial CPU offload.
- **9B:** The lowest-resource option for memory-constrained GPUs, mobile devices, and lighter workloads.

## Post-Training

Blossom-V7 is post-trained for general assistant use across everyday conversation, world knowledge, mathematics and reasoning, coding, web development, and data visualization.

The data pipeline uses [BlossomData](https://github.com/Azure99/BlossomData), our open-source framework for flexible, scalable data processing and synthesis. Data is filtered with LLM-as-Judge review and, when applicable, Agent-as-Judge verification. Agent-as-Judge runs in [AgentBox](https://github.com/Azure99/agentbox), our open-source work environment for AI agents, and uses search, browser interaction, screenshot capture, and code execution as needed. Samples involving web development and data visualization receive additional screening for functionality, usability, and visual quality.

The training data will be released as open source in a future update.

## Multi-turn & Reasoning Replay

For multi-turn conversations, always replay the assistant's reasoning together with its answer. Omitting prior reasoning can significantly degrade model performance in subsequent turns.

After initializing the OpenAI-compatible `client` shown in either server example below, append the complete assistant message rather than rebuilding it from `role` and `content`:

```python
messages = [{"role": "user", "content": "Explain why the sky is blue."}]

response = client.chat.completions.create(model="blossom-v7", messages=messages)
messages.append(response.choices[0].message.model_dump(exclude_none=True))
messages.append({"role": "user", "content": "Now explain it with an analogy."})

response = client.chat.completions.create(model="blossom-v7", messages=messages)
```

This preserves vLLM's `reasoning` field, llama.cpp's `reasoning_content` field, and any tool calls. Configure agent frameworks to retain the complete assistant message in history.

## Usage

The examples below use Blossom-V7-27B. To switch variants, set `MODEL_ID` to the corresponding Safetensors repository for Transformers or vLLM, or to the GGUF repository for llama.cpp.

### Recommended Sampling

The recommended settings are `temperature=1.0`, `top_p=0.95`, `top_k=50`, and `repetition_penalty=1.0`. The first three are included in `generation_config.json` and the GGUF metadata, while all three runtimes default to `repetition_penalty=1.0`. In most cases, leave them unset.

### Transformers

Install PyTorch for your hardware, then install:

```bash
pip install -U "transformers>=5.12.1" accelerate
```

This text-only path skips the vision encoder:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Azure99/Blossom-V7-27B"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Explain why the sky is blue in simple terms."}
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

with torch.inference_mode():
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=2048,
    )

generated_ids = generated_ids[:, inputs["input_ids"].shape[1]:]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

### vLLM

Install vLLM and the OpenAI client:

```bash
pip install -U "vllm>=0.26.0" openai
```

Start an OpenAI-compatible server:

```bash
MODEL_ID=Azure99/Blossom-V7-27B

vllm serve "$MODEL_ID" \
  --served-model-name blossom-v7 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.95 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --enable-prefix-caching \
  --speculative-config '{"method":"mtp","num_speculative_tokens":1}'
```

The tokenizer includes the full chat template for multimodal input, reasoning, and tool calls, and vLLM loads `generation_config.json` by default. Add `--tensor-parallel-size N` for multi-GPU serving. Set `--max-model-len 262144` if memory allows. MTP is optional; remove `--speculative-config` to disable it.

Call the server with an image URL using the OpenAI client. vLLM returns parsed reasoning in `message.reasoning`:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
IMAGE_URL = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"

response = client.chat.completions.create(
    model="blossom-v7",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": IMAGE_URL},
                },
                {"type": "text", "text": "Describe this image briefly."},
            ],
        }
    ],
    max_completion_tokens=512,
)

message = response.choices[0].message
print("Reasoning:", getattr(message, "reasoning", None))
print("Answer:", message.content)
```

### llama.cpp (GGUF)

For GGUF inference, use the matching GGUF repository with a current `llama.cpp` build. Use the embedded chat template; do not pass `--chat-template` or `--chat-template-file`. Keep `--reasoning on` and `--reasoning-format deepseek` enabled as shown below.

Ollama is not recommended because its current chat implementation does not correctly preserve Blossom's template behavior.

```bash
MODEL_ID=Azure99/Blossom-V7-27B-GGUF

llama-server \
  -hf "${MODEL_ID}:Q4_K_M" \
  --alias blossom-v7 \
  --ctx-size 131072 \
  --parallel 1 \
  --n-gpu-layers all \
  --flash-attn on \
  --spec-type draft-mtp \
  --spec-draft-n-max 1 \
  --reasoning on \
  --reasoning-format deepseek \
  --min-p 0
```

`-hf` loads the `Q4_K_M` model and its embedded chat template, and automatically downloads a multimodal projector from the same repository. `--min-p 0` disables llama.cpp's default min-p sampler. Set `--ctx-size 262144` if memory allows. MTP is optional; remove `--spec-type` and `--spec-draft-n-max` to disable it.

With the parsing flags above, llama.cpp returns reasoning in `message.reasoning_content` and tool calls in `message.tool_calls`.

Call the server with the OpenAI client:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="no-key")
response = client.chat.completions.create(
    model="blossom-v7",
    messages=[{"role": "user", "content": "Find an elegant proof that there are infinitely many primes."}],
    max_tokens=2048,
)

message = response.choices[0].message
print("Reasoning:", getattr(message, "reasoning_content", None))
print("Answer:", message.content)
```

## Public Datasets

The latest currently available Blossom post-training datasets are from V6.3:

| Dataset | Samples |
| --- | ---: |
| [blossom-v6.3-sft-stage1](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage1) | 150K |
| [blossom-v6.3-sft-stage2](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage2) | 50K |

## License

Blossom-V7 is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
