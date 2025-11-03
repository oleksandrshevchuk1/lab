import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import pygame
from bs4 import BeautifulSoup
from PIL import Image
from tqdm import tqdm
import pyjokes

def test_requests():
    try:
        response = requests.get("https://httpbin.org/get")
        print("Requests працює, статус:", response.status_code)
    except Exception as e:
        print("Помилка в requests:", e)

def test_numpy():
    try:
        arr = np.array([1, 2, 3])
        print("NumPy працює:", arr * 2)
    except Exception as e:
        print("Помилка в numpy:", e)

def test_pandas():
    try:
        df = pd.DataFrame({"Name": ["Anna", "Oleh"], "Age": [22, 25]})
        print("Pandas працює:\n", df)
    except Exception as e:
        print("Помилка в pandas:", e)

def test_faker():
    try:
        fake = Faker()
        print("Faker працює. Випадкове ім'я:", fake.name())
    except Exception as e:
        print("Помилка в Faker:", e)

def test_pyjokes():
    try:
        print("Pyjokes працює:", pyjokes.get_joke())
    except Exception as e:
        print("Помилка в pyjokes:", e)


if __name__ == "__main__":
    print("Тест бібліотек")
    test_requests()
    test_numpy()
    test_pandas()
    test_faker()
    test_pyjokes()
