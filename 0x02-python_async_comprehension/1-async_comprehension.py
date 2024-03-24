#!/usr/bin/env python3
"""Coroutine called async_comprehension"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of 10 random numbers"""
    return [i async for i in async_generator()]
