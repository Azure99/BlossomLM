# BlossomLM

Blossom是一系列开源的对话式大型语言模型。

本项目旨在提供一套高质量的中英双语通用SFT数据，让微调变得触手可及，同时提供训练后的模型权重。

**Hint**: BlossomLM是个人非商业化项目。

## 在线体验

[BlossomChat🚀](https://blossom-chat.com/)

Demo模型为blossom-v5-34b，出于资源限制，使用了4bit量化部署，效果会有一定下降。

## 模型权重

| 模型                                                         | 参数量 | 预训练模型                |
| ------------------------------------------------------------ | ------ | ------------------------- |
| [blossom-v5-34b](https://huggingface.co/Azure99/blossom-v5-34b) [GGUF](https://huggingface.co/Azure99/blossom-v5-34b-gguf/tree/main) [🌼演示](https://blossom-chat.com/) | 340亿  | 01-ai/Yi-34B              |
| [blossom-v5-14b](https://huggingface.co/Azure99/blossom-v5-14b) [GGUF](https://huggingface.co/Azure99/blossom-v5-14b-gguf/tree/main) [🤗演示](https://azure99-blossom-14b-demo.hf.space/) | 140亿  | Qwen/Qwen1.5-14B          |
| [blossom-v5-9b](https://huggingface.co/Azure99/blossom-v5-9b) [GGUF](https://huggingface.co/Azure99/blossom-v5-9b-gguf/tree/main) [🤗演示](https://azure99-blossom-9b-demo.hf.space/) | 90亿   | 01-ai/Yi-9B               |
| [blossom-v5-4b](https://huggingface.co/Azure99/blossom-v5-4b) [GGUF](https://huggingface.co/Azure99/blossom-v5-4b-gguf/tree/main) [🤗演示](https://azure99-blossom-4b-demo.hf.space/) | 40亿   | Qwen/Qwen1.5-4B           |
| [blossom-v5-mistral-7b](https://huggingface.co/Azure99/blossom-v5-mistral-7b) [GGUF](https://huggingface.co/Azure99/blossom-v5-mistral-7b-gguf/tree/main) [🤗演示](https://azure99-blossom-mistral-7b-demo.hf.space/) | 70亿   | mistralai/Mistral-7B-v0.1 |

## 模型部署

### Ollama

安装[Ollama](https://ollama.com/)后即可一键启动，你可以打开[模型列表](https://ollama.com/azure99/blossom-v5)查看全部可用模型(4b~34b)。

> ollama run azure99/blossom-v5

如果希望将模型权重完全放置到GPU上，可以使用带有**gpu**后缀的tag。

> ollama run azure99/blossom-v5:gpu

### Transformers

使用下面的命令进行安装，通过`python web_demo.py`启动网页Demo。

注意：在安装pytorch时，请**务必**参考[官方文档](https://pytorch.org/get-started/locally/)。

对于个人本地化部署场景，推荐使用[Ollama](https://ollama.com/)；对于高并发场景，推荐使用[vLLM](https://docs.vllm.ai/en/latest/)。

```bash
git clone https://github.com/Azure99/BlossomLM.git
cd BlossomLM/inference/transformers
pip install -r requirements.txt
python web_demo.py
```

## 数据集

| 数据集                                                       | 类型                   | 数据量 |
| ------------------------------------------------------------ | ---------------------- | ------ |
| [blossom-chat-v3](https://huggingface.co/datasets/Azure99/blossom-chat-v3) | 多轮通用对话           | 5K     |
| [blossom-math-v4](https://huggingface.co/datasets/Azure99/blossom-math-v4) | 包含推理过程的数学题目 | 10K    |
| [blossom-orca-v3](https://huggingface.co/datasets/Azure99/blossom-orca-v3) | 解释型指令             | 40K    |
| [blossom-wizard-v3](https://huggingface.co/datasets/Azure99/blossom-wizard-v3) | 更复杂的指令           | 20K    |

## 模型评测

任何评估都具有局限性，不能完整反映模型的真实能力，许多模型使用评估集进行训练，进而在测试中取得极高的成绩，结果仅供参考。

### AlignBench

| 模型                      | 专业 | 中文 | 任务 | 数学 | 写作 | 问答 | 扮演 | 逻辑 | 推理 | 语言 | 总分 |
| ------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| gpt-4-0613                | 7.56 | 6.76 | 7.16 | 6.49 | 7.31 | 7.26 | 7.48 | 6.33 | 6.41 | 7.25 | 6.83 |
| **blossom-v5-34b**        | 8.35 | 7.20 | 7.02 | 5.47 | 7.85 | 8.44 | 7.76 | 6.09 | 5.78 | 7.77 | 6.78 |
| **blossom-v5-14b**        | 7.70 | 6.98 | 6.88 | 5.42 | 7.46 | 8.34 | 7.43 | 5.83 | 5.63 | 7.47 | 6.55 |
| **blossom-v5-9b**         | 7.41 | 7.06 | 7.08 | 4.93 | 7.56 | 8.78 | 7.56 | 5.42 | 5.18 | 7.57 | 6.38 |
| yi-34b-chat-0205          | 7.63 | 7.55 | 6.95 | 4.40 | 7.66 | 7.94 | 7.43 | 5.76 | 5.08 | 7.53 | 6.30 |
| gpt-3.5-turbo-0613        | 6.29 | 5.60 | 6.01 | 4.90 | 7.27 | 6.97 | 6.98 | 4.79 | 4.85 | 6.52 | 5.68 |
| spark_desk_v2（讯飞星火） | 5.96 | 6.29 | 5.76 | 4.53 | 7.25 | 6.37 | 7.03 | 4.62 | 4.58 | 6.44 | 5.51 |
| qwen-14b-chat             | 5.98 | 5.84 | 6.46 | 4.54 | 6.47 | 6.71 | 6.38 | 4.50 | 4.52 | 6.31 | 5.41 |
| qwen-7b-chat              | 5.12 | 5.52 | 6.01 | 3.51 | 6.28 | 5.89 | 6.16 | 3.80 | 3.65 | 5.83 | 4.74 |
| chatglm2-6b               | 5.15 | 5.12 | 5.24 | 3.28 | 6.83 | 6.68 | 5.95 | 3.35 | 3.31 | 5.83 | 4.57 |

### MTBench

| 模型                      | 第一轮 | 第二轮 | 总分 |
| ------------------------- | ------ | ------ | ---- |
| gpt-4                     | 8.96   | 9.02   | 8.99 |
| **blossom-v5-14b**        | 8.73   | 7.61   | 8.17 |
| **blossom-v5-34b**        | 8.38   | 7.66   | 8.02 |
| gpt-3.5-turbo             | 8.08   | 7.81   | 7.94 |
| **blossom-v5-9b**         | 8.26   | 7.33   | 7.80 |
| **blossom-v5-mistral-7b** | 7.81   | 7.40   | 7.60 |
| zephyr-7b-beta            | -      | -      | 7.34 |
| vicuna-33b-v1.3           | 7.46   | 6.78   | 7.12 |
| qwen-14b-chat             | -      | -      | 6.96 |
| Mistral-7B-Instruct-v0.1  | -      | -      | 6.84 |
