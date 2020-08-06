#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import torch


def hello():
    return torch.cuda.is_available()
