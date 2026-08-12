#!/usr/bin/env python3
# latency benchmark — 2026-08-12
import time, statistics

def bench(fn, n=50):
    t = []
    for _ in range(n):
        s = time.perf_counter()
        fn()
        t.append(time.perf_counter()-s)
    print(f'p50={statistics.median(t)*1000:.1f}ms  p95={sorted(t)[int(n*.95)]*1000:.1f}ms')
