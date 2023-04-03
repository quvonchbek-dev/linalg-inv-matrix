import numpy as np


S = " !@#$%^&*()_+,.-/0123456789:;<=>?\"'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]`~Nabcdefghijklmnopqrstuvwxyz{|\n"

def filter_text(text: str) -> str:
    return str(text).replace(",", " ").replace("[", "").replace("]", "").strip()

def decode(A: list, k: list) -> str:
    A = np.array(A).reshape(2, len(A) // 2)
    inv_k = np.linalg.inv(k)
    decoded_arr = np.dot(inv_k, A)
    res = []
    for i in range(len(decoded_arr[0])):
        res.append(decoded_arr[0][i])
        res.append(decoded_arr[1][i])
    decoded_str = ""
    for i in range(len(A[0])):
        for j in [0, 1]:
            decoded_str += S[round(decoded_arr[j][i])]
    return decoded_str


def encode(s: str, k: list) -> np.ndarray:
    A = [[], []]
    s += " " * (len(s) % 2)
    n = len(s)
    for i in range(n):
        A[i % 2].append(S.index(s[i]))
    A = np.array(A)
    res = np.dot(np.array(k), A)
    return res.reshape(1, 2 * len(res[0]))[0]

def main():
    pass

if __name__ == "__main__":
    main()
