---
layout: interview
title: Bert
date: 2021-05-28 11:34:56
tags:
---

# Introduction

本文旨在，整理一部分Bert相关的面试QA

# Main

## Q1 - Bert, ELMO与GPT的比较？

**Answer:**

        ELMO是RNN-Based的Embedding模型。ELMO包含双层BiLSTM结构，ELMO的Embeddings是left-to-right和right-to-left的concatenation

        GPT同样是使用了Transformers的结构，但只使用了decoder部分

        Bert使用Transformers的encoder部分

## Q1 - bert的具体网络结构，以及训练过程，bert为什么火，它在什么的基础上改进了些什么？

        Bert采用MLM (Masked Language Model) 和 NSP (Next Sentence Prediction)结构。

        MLM:
        与之前的Embedding模型不同，Bert中的MLM并不去预测下一个词，而是预测整句话。Input Sequence中的15%的Tokens将会被masked。
        1. 不会所有的masked words都用[MASK]替换，而且根据token的位置，随机的抽取15%来预测
        2. 如果$i_{th}$的token被选中，则可能存在三种情况:
            *. 80%的情况会被用[MASK]替换
            *. 10%的情况会用其他token替换(randomly)
            *. 10%的情况不作改变
        3. 使用Cross Entropy Loss来预测masked tokens.

        这里涉及到三个问题，
