import random
import requests

u = "https://www.mit.edu/~ecprice/wordlist.10000"
a, b, c = (
    0,
    random.choice(requests.get(u).content.decode().split("\n")),
    lambda s: "".join(
        [b[i] if b[i] == s[i] else "*" for i in range(min(len(s), len(b)))]
    ).ljust(len(b), "*")[: len(b)],
)

print(f"Word length: {len(b)}. Hope you win.")
while (a := a + 1) and (s := input(f"[{a}]: ")):
    s == b and (print(f"YOU ARE GENIOUS. {b}") or exit())
    print(f"Matches: {c(s)}")
