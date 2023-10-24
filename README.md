# BlossomLM

BlossomLM是一系列面向实用场景的对话式大型语言模型

更多信息待补充

## 在线体验

[BlossomChat🚀](https://chat.rainng.com/)

注意：Demo模型为blossom-v2-baichuan-13b，出于成本考虑使用4bit量化部署，12G显存的消费级显卡即可推理，但效果会有一定下降。

## 模型权重

| 模型                                                         | 参数量 | 预训练模型                     |
| ------------------------------------------------------------ | ------ | ------------------------------ |
| [blossom-v2-baichuan-13b](https://huggingface.co/Azure99/blossom-v2-baichuan-13b)👍 | 130亿  | baichuan-inc/Baichuan-13B-Base |
| [blossom-v2-baichuan-7b](https://huggingface.co/Azure99/blossom-v2-baichuan-7b)👍 | 70亿   | baichuan-inc/Baichuan-7B       |
| [blossom-v2-llama2-7b](https://huggingface.co/Azure99/blossom-v2-llama2-7b) | 70亿   | meta-llama/Llama-2-7b-hf       |
| [blossom-v2-3b](https://huggingface.co/Azure99/blossom-v2-3b) | 30亿   | bigscience/bloom-3b            |

## 数据集

| 数据集                                                       | 类型                   | 数据量 |
| ------------------------------------------------------------ | ---------------------- | ------ |
| [blossom-chat-v1](https://huggingface.co/datasets/Azure99/blossom-chat-v1) | 多轮通用对话           | 30K    |
| [blossom-math-v2](https://huggingface.co/datasets/Azure99/blossom-math-v2) | 数学题COT              | 10K    |
| [blossom-orca-v1](https://huggingface.co/datasets/Azure99/blossom-orca-v1) | 带有System的解释性指令 | 200K   |
| [blossom-wizard-v1](https://huggingface.co/datasets/Azure99/blossom-wizard-v1) | 更复杂的单轮指令       | 100K   |
