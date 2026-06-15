# BlossomLM

<p align="center">
    <img src="https://www.rainng.com/wp-content/uploads/2024/04/logo-blossom.jpg" width="200"/>
<p>


<p align="center">
    🖥️<a
        href="https://blossom-chat.com/">Demo</a>&nbsp|&nbsp🤗<a
        href="https://huggingface.co/Azure99">Hugging Face</a>&nbsp|&nbsp📑<a href="https://www.rainng.com/blossom-llm/">Blog</a>
</p>


Blossom是一个开源的对话式大型语言模型，提供可复现的后训练数据，致力于为每个人提供开放、强大且高效的本地通用模型。

Blossom模型的所有训练数据均由[BlossomData](https://github.com/Azure99/BlossomData)处理及合成，这是一个专为大模型设计的灵活且高效的数据处理框架。

**Hint**: BlossomLM是个人非商业化项目。

## 模型权重

Blossom-V6.4基本沿用了V6.3版本的训练方案和数据，将基座模型替换为Qwen3.5系列，并加入少量多模态样本，以维持基础模型的多模态能力。

| 模型                                                         | 相关资源                                                     | 预训练模型           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- |
| [Blossom-V6.4-27B](https://huggingface.co/Azure99/Blossom-V6.4-27B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.4-27B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V6.4-27B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.4:27b) | Qwen3.5-27B          |
| [Blossom-V6.4-35B-A3B](https://huggingface.co/Azure99/Blossom-V6.4-35B-A3B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.4-35B-A3B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V6.4-35B-A3B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.4:35b) | Qwen3.5-35B-A3B-Base |
| [Blossom-V6.4-9B](https://huggingface.co/Azure99/Blossom-V6.4-9B) | [Demo](https://huggingface.co/spaces/Azure99/Blossom-V6.4-9B-Demo) [GGUF](https://huggingface.co/Azure99/Blossom-V6.4-9B-GGUF) [Ollama](https://ollama.com/azure99/blossom-v6.4:9b) | Qwen3.5-9B-Base      |

## 模型部署

### Ollama

安装[Ollama](https://ollama.com/)后即可一键启动，你可以打开[模型列表](https://ollama.com/azure99/blossom-v6.4)查看全部可用模型。

> ollama run azure99/blossom-v6.4

#### Android端使用Ollama

首先需要安装[Termux](https://termux.dev/en/)，打开Termux后，先通过自带包管理器安装Ollama。

```bash
pkg install ollama
```

安装完毕后，在后台运行Ollama服务，并运行模型。

```bash
nohup ollama serve &
ollama run azure99/blossom-v6.4:9b
```

此外，推荐使用[PocketPal](https://github.com/a-ghorbani/pocketpal-ai)来在移动端体验Blossom模型，安装后，在Models页面选择Add from Hugging Face，并搜索Blossom-V6.4即可，建议选择9b-q4_k_m来平衡速度与质量。

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
| [blossom-v6.3-sft-stage1](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage1) | 150K   |
| [blossom-v6.3-sft-stage2](https://huggingface.co/datasets/Azure99/blossom-v6.3-sft-stage2) | 50K    |

## 模型评测

任何评估都具有局限性，不能完整反映模型的真实能力，许多模型在预训练及后训练阶段中，加入大量与评估集相似的合成样本甚至直接加入评估集进行训练，进而在测试中取得极高的成绩，因此，结果仅供参考。

### Arena-Hard-v2.0-Preview

Hard Prompt, Style Control, and GPT-4.1 as Judge.

Blossom-V6.3系列模型在同尺寸，甚至更大尺寸的非推理模型中，表现出极强的竞争力，特别适合本地部署场景。

```
                                Model  Scores (%)        CI (%)
0       Qwen3-235B-A22B-Instruct-2507        64.2  (-2.3 / +2.4)
1                GLM-4.6-Non-Thinking        60.5  (-1.5 / +1.6)
2                    Blossom-V6.3-36B        60.1  (-1.6 / +1.5)
3         Qwen3-30B-A3B-Instruct-2507        57.3  (-1.8 / +1.8)
4                        Kimi-K2-0905        55.6  (-1.6 / +1.6)
5      DeepSeek-V3.2-Exp-Non-Thinking        53.8  (-1.7 / +1.9)
6                  o3-mini-2025-01-31        50.0  (-0.0 / +0.0)
7                    Blossom-V6.3-14B        47.8  (-1.9 / +1.6)
8            GLM-4.5-Air-Non-Thinking        41.4  (-1.7 / +1.6)
9                 ERNIE-4.5-300B-A47B        33.7  (-1.7 / +1.9)
10                    Blossom-V6.3-8B        33.4  (-1.7 / +1.6)
11 Seed-OSS-36B-Instruct-Non-Thinking        28.0  (-1.6 / +2.0)
12             Qwen3-32B-Non-Thinking        26.5  (-1.8 / +1.6)
13             Qwen3-14B-Non-Thinking        19.1  (-1.3 / +1.5)
14              Qwen3-8B-Non-Thinking        12.4  (-1.1 / +1.1)
15                     gemma-3-27b-it         9.7  (-0.9 / +1.1)
16 Llama-3.1-Nemotron-70B-Instruct-HF         6.8  (-0.6 / +0.8)
```
