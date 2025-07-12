# BlossomLM

<p align="center">
    <img src="https://www.rainng.com/wp-content/uploads/2024/04/logo-blossom.jpg" width="200"/>
<p>


<p align="center">
    📑<a href="https://www.rainng.com/blossom-llm/">Blog</a>&nbsp|&nbsp🖥️<a
        href="https://blossom-chat.com/">Demo</a>&nbsp|&nbsp🤗<a
        href="https://huggingface.co/Azure99">Hugging Face</a>
</p>


Blossom是一个开源的对话式大型语言模型，提供可复现的后训练数据，致力于为每个人提供开放、强大且高效的本地通用模型。

**Hint**: BlossomLM是个人非商业化项目。

## 模型权重

|                             模型                             |                           相关资源                           |     预训练模型      |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :-----------------: |
| [Blossom-V6.1-32B](https://huggingface.co/Azure99/Blossom-V6.1-32B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.1-32B-AWQ-Demo) [AWQ](https://huggingface.co/Azure99/Blossom-V6.1-32B-AWQ) [GGUF](https://huggingface.co/Azure99/Blossom-V6.1-32B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.1:32b) |     Qwen2.5-32B     |
| [Blossom-V6.1-GLM-32B](https://huggingface.co/Azure99/Blossom-V6.1-GLM-32B) | [GGUF](https://huggingface.co/Azure99/Blossom-V6.1-GLM-32B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.1:glm-32b) | GLM-4-32B-Base-0414 |
| [Blossom-V6.1-14B](https://huggingface.co/Azure99/Blossom-V6.1-14B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.1-14B-Demo) [AWQ](https://huggingface.co/Azure99/Blossom-V6.1-14B-AWQ) [GGUF](https://huggingface.co/Azure99/Blossom-V6.1-14B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.1:14b) |   Qwen3-14B-Base    |
| [Blossom-V6.1-8B](https://huggingface.co/Azure99/Blossom-V6.1-8B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.1-8B-Demo) [AWQ](https://huggingface.co/Azure99/Blossom-V6.1-8B-AWQ) [GGUF](https://huggingface.co/Azure99/Blossom-V6.1-8B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.1:7b) |    Qwen3-8B-Base    |

注：Blossom-V6.1-GLM-32B在日常任务上效果比Blossom-V6.1-32B更优。

## 模型部署

### Ollama

安装[Ollama](https://ollama.com/)后即可一键启动，你可以打开[模型列表](https://ollama.com/azure99/blossom-v6.1)查看全部可用模型(8b~32b)。

> ollama run azure99/blossom-v6.1

#### Android编译Ollama

首先需要安装[Termux](https://termux.dev/en/)，然后执行下面的脚本，它会自动编译Ollama并启动服务，每次重启后，需要重新执行脚本。

```bash
curl -s https://raw.githubusercontent.com/Azure99/BlossomLM/main/inference/ollama/termux.sh | bash
```

执行完毕后，使用ollama启动。

> ollama run azure99/blossom-v6.1

此外，推荐使用[PocketPal](https://github.com/a-ghorbani/pocketpal-ai)来在移动端体验Blossom模型，安装后，在Models页面选择Add from Hugging Face，并搜索Blossom-V6.1即可，建议选择8b-q4_k_m来平衡速度与质量。

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

| 数据集                                                       | 数据量 |
| ------------------------------------------------------------ | ------ |
| [blossom-v6.1-sft-stage1](https://huggingface.co/datasets/Azure99/blossom-v6.1-sft-stage1) | 150K   |
| [blossom-v6.1-sft-stage2](https://huggingface.co/datasets/Azure99/blossom-v6.1-sft-stage2) | 50K    |

## 模型评测

任何评估都具有局限性，不能完整反映模型的真实能力，许多模型在预训练及后训练阶段中，加入大量与评估集相似的合成样本甚至直接加入评估集进行训练，进而在测试中取得极高的成绩，因此，结果仅供参考。

### Arena-Hard-v2.0-Preview

Hard Prompt, Style Control, and GPT-4.1 as Judge.

Blossom-V6.1系列模型在30B及以下的非推理模型中，表现出极强的竞争力，特别适合本地部署场景。

```
                                Model  Scores (%)        CI (%)
0                  o3-mini-2025-01-31        50.0  (-0.0 / +0.0)
1              Qwen3-32B-Non-Thinking        26.5  (-1.8 / +1.6)
2                    Blossom-V6.1-32B        22.6  (-1.5 / +1.8)
3                Blossom-V6.1-GLM-32B        21.2  (-1.6 / +1.3)
4                    Blossom-V6.1-14B        19.3  (-1.2 / +1.2)
5              Qwen3-14B-Non-Thinking        19.1  (-1.3 / +1.5)
6                        gpt-4.1-nano        15.4  (-1.1 / +1.2)
7                      GLM-4-32B-0414        14.8  (-1.1 / +1.2)
8                     Blossom-V6.1-8B        12.8  (-1.0 / +1.0)
9                      Athene-V2-Chat        12.6  (-1.2 / +1.3)
10              Qwen3-8B-Non-Thinking        12.4  (-1.1 / +1.1)
11                     gemma-3-27b-it         9.7  (-0.9 / +1.1)
12                  ERNIE-4.5-21B-A3B         8.5  (-0.9 / +0.9)
13               Qwen2.5-72B-Instruct         8.0  (-0.7 / +0.9)
14 Llama-3.1-Nemotron-70B-Instruct-HF         6.8  (-0.6 / +0.8)
15 Doubao-Seed-1.6-Flash-Non-Thinking         6.4  (-0.8 / +0.8)
```
