# Prompt Compression

## Introduction

Prompt compression is an idea that the text ${x_h}$ used to condition a language model (LM) can be approximately represented by a much smaller set of carefully chosen weights, using the framkwork ofo soft prompts, where ${x_h} = x_1,...,x_{t-1}$ is a set of tokens, called prompt, that guide a LM

Recently, a tweet from @VictorTaelin suggests that GPT can be prompted to generate more tokens by compressing the original prompt. @VictorTaelin initially discovered the GPT’s ability to compress and decompress tokens, as seen on the Github. 




## Notification
### Compression Rate



## LLM Lingua


## Experiment

1. Evaluation

* Dataset

|Dataset|Size|Description|Partition|
|:-|:-:|:-|:-|
|ARC|y|A new dataset of 7,787 genuine grade-school level, multiple-choice science questions, assembled to encourage research in advanced question-answering. The dataset is partitioned into a Challenge Set and an Easy Set, where the former contains only questions answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm. We are also including a corpus of over 14 million science sentences relevant to the task, and an implementation of three neural baseline models for this dataset. We pose ARC as a challenge to the community.|['ai2_arc', 'ARC-Challenge']|
|HellaSwag|.|A new dataset for commonsense NLI.(ACL2021)|
|MMLU||This is a massive multitask test consisting of multiple-choice questions from various branches of knowledge. The test spans subjects in the humanities, social sciences, hard sciences, and other areas that are important for some people to learn. This covers 57 tasks including elementary mathematics, US history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem solving ability.||
|TruthfulQA||A benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. Questions are crafted so that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts.|


```bash
python main.py \
    --model=hf-causal \
    --model_args="pretrained=/ossfs/workspace/nas/mntnlp/common_base_model/llama2-7b" \
    --tasks="arc_challenge" \
    --num_fewshot=25 \
    --batch_size=2 \
    --output_path="arc_challenge_eval"
```

2. Training