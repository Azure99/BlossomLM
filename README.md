# BlossomLM

Blossom是一系列开源的对话式大型语言模型

本项目旨在提供一套高质量的中英双语通用SFT数据，让微调变得触手可及，同时提供训练后的模型权重

更多信息待补充

## 在线体验

[BlossomChat🚀](https://blossom-chat.com/)

Demo模型为blossom-v4-yi-34b，出于资源限制，使用了4bit量化部署，效果会有一定下降

## 模型权重

| 模型                                                         | 参数量 | 预训练模型                |
| ------------------------------------------------------------ | ------ | ------------------------- |
| [blossom-v4-yi-34b](https://huggingface.co/Azure99/blossom-v4-yi-34b) | 340亿  | 01-ai/Yi-34B              |
| [blossom-v4-qwen1_5-14b](https://huggingface.co/Azure99/blossom-v4-qwen1_5-14b) | 140亿  | Qwen/Qwen1.5-14B          |
| [blossom-v4-qwen1_5-7b](https://huggingface.co/Azure99/blossom-v4-qwen1_5-7b) | 70亿   | Qwen/Qwen1.5-7B           |
| [blossom-v4-mistral-7b](https://huggingface.co/Azure99/blossom-v4-mistral-7b) | 70亿   | mistralai/Mistral-7B-v0.1 |
| [blossom-v4-qwen1_5-4b](https://huggingface.co/Azure99/blossom-v4-qwen1_5-4b) | 40亿   | Qwen/Qwen1.5-4B           |

## 数据集

| 数据集                                                       | 类型                   | 数据量 |
| ------------------------------------------------------------ | ---------------------- | ------ |
| [blossom-chat-v2](https://huggingface.co/datasets/Azure99/blossom-chat-v2) | 多轮通用对话           | 30K    |
| [blossom-math-v3](https://huggingface.co/datasets/Azure99/blossom-math-v3) | 包含推理过程的数学题目 | 10K    |
| [blossom-orca-v2](https://huggingface.co/datasets/Azure99/blossom-orca-v2) | 解释型指令             | 200K   |
| [blossom-wizard-v2](https://huggingface.co/datasets/Azure99/blossom-wizard-v2) | 更复杂的指令           | 100K   |

## 模型评测

任何评估都具有局限性，不能完整反映模型的真实能力，许多模型使用评估集进行训练，进而在测试中取得极高的成绩，结果仅供参考。

### AlignBench

| 模型                        | 专业  | 中文  | 任务  | 数学  | 写作  | 问答  | 扮演  | 逻辑  | 推理  | 语言  | 总分  |
| --------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| gpt-4-0613                  | 7\.56 | 6\.76 | 7\.16 | 6\.49 | 7\.31 | 7\.26 | 7\.48 | 6\.33 | 6\.41 | 7\.25 | 6\.83 |
| **blossom-v4-yi-34b**       | 7\.04 | 6\.62 | 6\.25 | 4\.66 | 7\.29 | 7\.47 | 7\.40 | 5\.05 | 4\.85 | 7\.01 | 5\.93 |
| gpt-3.5-turbo-0613          | 6\.29 | 5\.60 | 6\.01 | 4\.90 | 7\.27 | 6\.97 | 6\.98 | 4\.79 | 4\.85 | 6\.52 | 5\.68 |
| **blossom-v4-qwen-14b**     | 6\.41 | 6\.15 | 6\.23 | 4\.45 | 7\.32 | 7\.36 | 7\.37 | 4\.58 | 4\.52 | 6\.81 | 5\.66 |
| spark_desk_v2（讯飞星火）   | 5\.96 | 6\.29 | 5\.76 | 4\.53 | 7\.25 | 6\.37 | 7\.03 | 4\.62 | 4\.58 | 6\.44 | 5\.51 |
| qwen-14b-chat               | 5\.98 | 5\.84 | 6\.46 | 4\.54 | 6\.47 | 6\.71 | 6\.38 | 4\.50 | 4\.52 | 6\.31 | 5\.41 |
| **blossom-v4-baichuan2-7b** | 6\.12 | 5\.48 | 5\.29 | 3\.07 | 7\.20 | 7\.57 | 6\.70 | 3\.78 | 3\.42 | 6\.39 | 4\.91 |
| qwen-7b-chat                | 5\.12 | 5\.52 | 6\.01 | 3\.51 | 6\.28 | 5\.89 | 6\.16 | 3\.80 | 3\.65 | 5\.83 | 4\.74 |
| chatglm2-6b                 | 5\.15 | 5\.12 | 5\.24 | 3\.28 | 6\.83 | 6\.68 | 5\.95 | 3\.35 | 3\.31 | 5\.83 | 4\.57 |

### MTBench

| 模型                      | 第一轮 | 第二轮 | 总分  |
| ------------------------- | ------ | ------ | ----- |
| gpt-4                     | 8\.96  | 9\.02  | 8\.99 |
| gpt-3.5-turbo             | 8\.08  | 7\.81  | 7\.94 |
| **blossom-v4-qwen-14b**   | 7\.81  | 7\.06  | 7\.43 |
| zephyr-7b-beta            | \-     | \-     | 7\.34 |
| **blossom-v4-yi-34b**     | 7\.66  | 6\.94  | 7\.30 |
| **blossom-v4-mistral-7b** | 7\.77  | 6\.71  | 7\.23 |
| vicuna-33b-v1.3           | 7\.46  | 6\.78  | 7\.12 |
| qwen-14b-chat             | \-     | \-     | 6\.96 |
| Mistral-7B-Instruct-v0.1  | \-     | \-     | 6\.84 |
