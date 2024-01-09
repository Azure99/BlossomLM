# BlossomLM

Blossom是一系列开源的对话式大型语言模型

本项目旨在提供一套高质量的中英双语通用SFT数据，让微调变得触手可及，同时提供训练后的模型权重

更多信息待补充

## 在线体验

[BlossomChat🚀](https://blossom-chat.com/)

Demo模型为blossom-v4-yi-34b，出于资源限制，使用了4bit量化部署，效果会有一定下降

## 模型权重

| 模型                                                         | 参数量 | 预训练模型                     |
| ------------------------------------------------------------ | ------ | ------------------------------ |
| [blossom-v4-yi-34b](https://huggingface.co/Azure99/blossom-v4-yi-34b) | 340亿  | 01-ai/Yi-34B                   |
| [blossom-v4-qwen-14b](https://huggingface.co/Azure99/blossom-v4-qwen-14b) | 140亿  | Qwen/Qwen-14B                  |
| [blossom-v4-baichuan2-7b](https://huggingface.co/Azure99/blossom-v4-baichuan2-7b) | 70亿   | baichuan-inc/Baichuan2-7B-Base |
| [blossom-v4-mistral-7b](https://huggingface.co/Azure99/blossom-v4-mistral-7b) | 70亿   | mistralai/Mistral-7B-v0.1      |

## 数据集

| 数据集                                                       | 类型                   | 数据量 |
| ------------------------------------------------------------ | ---------------------- | ------ |
| [blossom-chat-v2](https://huggingface.co/datasets/Azure99/blossom-chat-v2) | 多轮通用对话           | 30K    |
| [blossom-math-v3](https://huggingface.co/datasets/Azure99/blossom-math-v3) | 包含推理过程的数学题目 | 10K    |
| [blossom-orca-v2](https://huggingface.co/datasets/Azure99/blossom-orca-v2) | 解释型指令             | 200K   |
| [blossom-wizard-v2](https://huggingface.co/datasets/Azure99/blossom-wizard-v2) | 更复杂的指令           | 100K   |
