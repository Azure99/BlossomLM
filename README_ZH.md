# BlossomLM

<p align="center">
    <a href="./README.md">English</a> | 简体中文
</p>

<p align="center">
    <img src="https://www.rainng.com/wp-content/uploads/2024/04/logo-blossom.jpg" width="200"/>
</p>

<p align="center">
    <a href="https://blossom-chat.com/">在线体验</a> |
    <a href="https://huggingface.co/Azure99">Hugging Face</a> |
    <a href="https://www.rainng.com/blossom-llm/">博客</a>
</p>

Blossom-V7.1 是一系列面向本地部署的开放权重通用多模态模型。它提供 `medium` 和 `max` 两种高效思考模式，具备支持交错思考的工具调用和图像理解能力，覆盖日常对话、世界知识、数学与推理、编程、Web 开发和数据可视化等任务，并可通过工具调用支持智能体工作流。

## 主要特性

- **高效的双模式思考：** 思考始终开启，支持 `medium` 和 `max` 两种模式，默认使用 `max` 以进行更充分的推理。`medium` 模式根据任务难度调整推理深度，在提供高质量结果的同时，推理轨迹长度约为 Qwen3.5 的四分之一、Qwen3.6 的五分之一。
- **支持交错思考的工具调用：** 每次调用工具前都会进行推理和决策，在智能体任务中表现出色。
- **图像理解：** 可结合文本理解图像输入。
- **长上下文：** 最长支持 262,144 个 token（256K）；建议使用 131,072 个 token（128K）以获得最佳效果。
- **使用 MTP 加速推理：** 在 vLLM 和 llama.cpp 中均支持通过多 Token 预测（Multi-Token Prediction，MTP）进行推测解码。

> **重要：** Blossom-V7.1 使用的自定义对话模板与其 Qwen 基座模型的原生模板不同。请始终使用模型附带的 `chat_template`；不要将其替换为原生 Qwen 对话模板，也不要混用两种模板。

## 模型规格

| 模型 | 相关资源 | 基座模型 |
| --- | --- | --- |
| [Blossom-V7.1-27B](https://huggingface.co/Azure99/Blossom-V7.1-27B) | [演示](https://huggingface.co/spaces/Azure99/Blossom-27B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7.1-27B-GGUF) | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) |
| [Blossom-V7.1-35B-A3B](https://huggingface.co/Azure99/Blossom-V7.1-35B-A3B) | [演示](https://huggingface.co/spaces/Azure99/Blossom-35B-A3B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7.1-35B-A3B-GGUF) | [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) |
| [Blossom-V7.1-9B](https://huggingface.co/Azure99/Blossom-V7.1-9B) | [演示](https://huggingface.co/spaces/Azure99/Blossom-9B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V7.1-9B-GGUF) | [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) |

请根据效果需求、推理硬件和内存预算选择合适的规格：

- **27B：** 能力最强的稠密模型，适合模型权重能够完全载入显存的 GPU 部署场景。
- **35B-A3B：** 侧重吞吐量，适合 CPU 或 CPU/GPU 混合推理；即使将部分权重卸载到 CPU，也能兼顾质量与速度。
- **9B：** 资源需求最低，适合显存受限的 GPU、移动设备和较轻量的工作负载。

## 后训练

Blossom-V7.1 经过面向通用助手场景的后训练，覆盖日常对话、世界知识、数学与推理、编程、Web 开发和数据可视化等任务。

数据流水线采用 [BlossomData](https://github.com/Azure99/BlossomData)，这是我们开源的灵活且可扩展的数据处理与合成框架。数据经 LLM-as-Judge 审核筛选，并在适用时通过 Agent-as-Judge 验证。Agent-as-Judge 运行在我们开源的 AI 智能体工作环境 [AgentBox](https://github.com/Azure99/agentbox) 中，可按需使用搜索、浏览器交互、截图和代码执行。涉及 Web 开发和数据可视化的样本还会接受额外筛选，以评估其功能性、易用性和视觉质量。

训练数据将在后续更新中开源。

## 多轮对话与推理回放

进行多轮对话时，务必在上下文中将助手的推理过程与回答一并回放。省略此前的推理过程可能会显著降低模型在后续轮次中的表现。

按照下方任一服务端示例初始化兼容 OpenAI API 的 `client` 后，请将完整的 `assistant` 消息追加到历史记录中，不要仅使用 `role` 和 `content` 重新构造消息：

```python
messages = [{"role": "user", "content": "Explain why the sky is blue."}]

response = client.chat.completions.create(model="blossom-v7.1", messages=messages)
messages.append(response.choices[0].message.model_dump(exclude_none=True))
messages.append({"role": "user", "content": "Now explain it with an analogy."})

response = client.chat.completions.create(model="blossom-v7.1", messages=messages)
```

这样可以保留 vLLM 的 `reasoning` 字段、llama.cpp 的 `reasoning_content` 字段以及所有工具调用信息。使用智能体框架时，请进行相应配置，使其在对话历史中保留完整的 `assistant` 消息。

## 使用方法

以下示例均使用 Blossom-V7.1-27B。若要切换模型规格，请将 `MODEL_ID` 指向相应的 Safetensors 仓库（用于 Transformers 或 vLLM）或 GGUF 仓库（用于 llama.cpp）。

### 思考模式

思考始终开启，提供 `medium` 和 `max` 两种模式，默认为 `max`。模型附带的对话模板按以下规则将 `reasoning_effort` 的值映射到对应模式：

| `reasoning_effort` | 思考模式 |
| --- | --- |
| 未指定（默认） | `max` |
| `low`、`medium`、`adaptive`（模板别名） | `medium` |
| 其他所有值 | `max` |

### 推荐采样参数

推荐设置为 `temperature=1.0`、`top_p=0.95`、`top_k=50` 和 `repetition_penalty=1.0`。前三项已写入 `generation_config.json` 和 GGUF 元数据，而三种运行方式均默认使用 `repetition_penalty=1.0`。多数情况下，无需显式设置这些参数。

### Transformers

请先根据硬件环境安装 PyTorch，再安装：

```bash
pip install -U "transformers>=5.12.1" accelerate
```

以下纯文本推理方式会跳过视觉编码器：

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Azure99/Blossom-V7.1-27B"

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

安装 vLLM 和 OpenAI 客户端：

```bash
pip install -U "vllm>=0.26.0" openai
```

启动 OpenAI 兼容服务：

```bash
MODEL_ID=Azure99/Blossom-V7.1-27B

vllm serve "$MODEL_ID" \
  --served-model-name blossom-v7.1 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.95 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --enable-prefix-caching \
  --speculative-config '{"method":"mtp","num_speculative_tokens":1}'
```

分词器包含支持多模态输入、推理和工具调用的完整对话模板，vLLM 默认会加载 `generation_config.json`。使用多张 GPU 提供服务时，请添加 `--tensor-parallel-size N`。内存充足时，可将上下文长度设为 262144（`--max-model-len 262144`）。MTP 为可选功能；移除 `--speculative-config` 即可禁用。

使用 OpenAI 客户端向服务发送包含图像 URL 的请求。vLLM 会在 `message.reasoning` 中返回解析后的推理内容：

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
IMAGE_URL = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"

response = client.chat.completions.create(
    model="blossom-v7.1",
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

在 vLLM 中选择 `medium` 模式时，请在上述 `client.chat.completions.create(...)` 调用中添加 `reasoning_effort="medium"`。

### llama.cpp（GGUF）

进行 GGUF 推理时，请使用对应的 GGUF 仓库和较新版本的 `llama.cpp`。请使用模型内嵌的对话模板，不要传入 `--chat-template` 或 `--chat-template-file`。同时，请按下方示例启用 `--reasoning on` 和 `--reasoning-format deepseek`。

目前不推荐使用 Ollama，因为其当前的对话实现无法正确保留 Blossom 对话模板所定义的行为。

```bash
MODEL_ID=Azure99/Blossom-V7.1-27B-GGUF

llama-server \
  -hf "${MODEL_ID}:Q4_K_M" \
  --alias blossom-v7.1 \
  --ctx-size 131072 \
  --parallel 1 \
  --flash-attn on \
  --spec-type draft-mtp \
  --spec-draft-n-max 1 \
  --reasoning on \
  --reasoning-format deepseek \
  --min-p 0
```

`-hf` 会加载 `Q4_K_M` 模型及其内嵌对话模板，并自动从同一仓库下载多模态投影器。`--min-p 0` 会禁用 llama.cpp 默认的 min-p 采样器。内存充足时，可将上下文大小设为 262144（`--ctx-size 262144`）。MTP 为可选功能；移除 `--spec-type` 和 `--spec-draft-n-max` 即可禁用。

启用上述解析参数后，llama.cpp 会在 `message.reasoning_content` 中返回推理内容，并在 `message.tool_calls` 中返回工具调用。

使用 OpenAI 客户端调用服务：

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="no-key")
response = client.chat.completions.create(
    model="blossom-v7.1",
    messages=[{"role": "user", "content": "Find an elegant proof that there are infinitely many primes."}],
    max_tokens=2048,
)

message = response.choices[0].message
print("Reasoning:", getattr(message, "reasoning_content", None))
print("Answer:", message.content)
```

## 公开数据集

目前公开的最新 Blossom 后训练数据集来自 V6.3：

| 数据集 | 样本数 |
| --- | ---: |
| [blossom-v6.3-sft-stage1](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage1) | 150K |
| [blossom-v6.3-sft-stage2](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage2) | 50K |

## 许可证

Blossom-V7.1 依据 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 发布。
