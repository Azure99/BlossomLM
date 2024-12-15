# BlossomLM

<p align="center">
    <img src="https://www.rainng.com/wp-content/uploads/2024/04/logo-blossom.jpg" width="200"/>
<p>




<p align="center">
    📑<a href="https://www.rainng.com/blossom-llm/">Blog</a>&nbsp|&nbsp🖥️<a
        href="https://blossom-chat.com/">Demo</a>&nbsp|&nbsp🤗<a
        href="https://huggingface.co/Azure99">Hugging Face</a>
</p>




Blossom是一系列开源的对话式大型语言模型。

本项目旨在提供一套高质量的中英双语通用SFT数据，让微调变得触手可及，同时提供训练后的模型权重。

**Hint**: BlossomLM是个人非商业化项目。

- 2024.12.07: 很高兴推出Blossom V6预览版（可前往[https://blossom-chat.com/](https://blossom-chat.com/)体验），当最终版本训练完成后，会一并开源模型权重和训练数据。

## 模型权重

| 模型                                                         | 参数量 | 预训练模型       |
| ------------------------------------------------------------ | ------ | ---------------- |
| [blossom-v5.1-34b](https://huggingface.co/Azure99/blossom-v5.1-34b) [GGUF](https://huggingface.co/Azure99/blossom-v5.1-34b-gguf/tree/main) [🤗演示](https://azure99-blossom-34b-demo.hf.space/) | 340亿  | 01-ai/Yi-1.5-34B |
| [blossom-v5.1-9b](https://huggingface.co/Azure99/blossom-v5.1-9b) [GGUF](https://huggingface.co/Azure99/blossom-v5.1-9b-gguf/tree/main) [🤗演示](https://azure99-blossom-9b-demo.hf.space/) | 90亿   | 01-ai/Yi-1.5-9B  |
| [blossom-v5.1-4b](https://huggingface.co/Azure99/blossom-v5-4b) [GGUF](https://huggingface.co/Azure99/blossom-v5-4b-gguf/tree/main) | 40亿   | Qwen/Qwen1.5-4B  |

## 模型部署

### Ollama

安装[Ollama](https://ollama.com/)后即可一键启动，你可以打开[模型列表](https://ollama.com/azure99/blossom-v5)查看全部可用模型(4b~34b)。

> ollama run azure99/blossom

#### Android编译Ollama

首先需要安装[Termux](https://termux.dev/en/)，然后执行下面的脚本，它会自动编译Ollama并启动服务，每次重启后，需要重新执行脚本。

```bash
curl -s https://raw.githubusercontent.com/Azure99/BlossomLM/main/inference/ollama/termux.sh | bash
```

执行完毕后，使用ollama启动。对于中文场景，你可能需要添加`--nowordwrap`来避免换行异常。

> ollama run azure99/blossom --nowordwrap

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
| **blossom-v5.1-34b**      | 8.07 | 7.79 | 7.69 | 6.47 | 7.76 | 8.71 | 7.86 | 6.00 | 6.23 | 7.98 | 7.10 |
| gpt-4-0613                | 7.56 | 6.76 | 7.16 | 6.49 | 7.31 | 7.26 | 7.48 | 6.33 | 6.41 | 7.25 | 6.83 |
| **blossom-v5.1-9b**       | 7.62 | 7.31 | 7.16 | 5.59 | 7.76 | 8.50 | 7.56 | 6.08 | 5.84 | 7.65 | 6.74 |
| yi-34b-chat-0205          | 7.63 | 7.55 | 6.95 | 4.40 | 7.66 | 7.94 | 7.43 | 5.76 | 5.08 | 7.53 | 6.30 |
| gpt-3.5-turbo-0613        | 6.29 | 5.60 | 6.01 | 4.90 | 7.27 | 6.97 | 6.98 | 4.79 | 4.85 | 6.52 | 5.68 |
| spark_desk_v2（讯飞星火） | 5.96 | 6.29 | 5.76 | 4.53 | 7.25 | 6.37 | 7.03 | 4.62 | 4.58 | 6.44 | 5.51 |
| qwen-14b-chat             | 5.98 | 5.84 | 6.46 | 4.54 | 6.47 | 6.71 | 6.38 | 4.50 | 4.52 | 6.31 | 5.41 |
| qwen-7b-chat              | 5.12 | 5.52 | 6.01 | 3.51 | 6.28 | 5.89 | 6.16 | 3.80 | 3.65 | 5.83 | 4.74 |
| chatglm2-6b               | 5.15 | 5.12 | 5.24 | 3.28 | 6.83 | 6.68 | 5.95 | 3.35 | 3.31 | 5.83 | 4.57 |

### MTBench

| 模型                 | 第一轮 | 第二轮 | 总分 |
| -------------------- | ------ | ------ | ---- |
| gpt-4-0613           | -      | -      | 9.18 |
| llama-3-70b-instruct | -      | -      | 8.95 |
| **blossom-v5-34b**   | 8.91   | 8.46   | 8.69 |
| qwen1.5-72b-chat     | -      | -      | 8.61 |
| **blossom-v5.1-9b**  | 8.87   | 7.95   | 8.41 |
| gpt-3.5-turbo-0613   | -      | -      | 8.39 |
| glm-4-9b-chat        | -      | -      | 8.35 |
| qwen1.5-32b-chat     | -      | -      | 8.30 |
| llama-3-8b-instruct  | -      | -      | 8.05 |
