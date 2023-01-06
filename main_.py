import gradio as gr
import numpy as np

text_sum = gr.Blocks.load(name="huggingface/csebuetnlp/mT5_multilingual_XLSum")
picture_gen = gr.Blocks.load(name="huggingface/CompVis/stable-diffusion-v1-4")

# Если юзер не ввел текст, то суммаризация происходит по дефолтному тексту
def predict_text(text):
    if len(text) > 0:
        return text_sum(text)
    else:
        return text_sum(
            'Pink elephant likes eating a lot of fruits and vegetable, but it likes eating bananas more then others')

# Если юзер не ввел текст, то создание изображения происходит по дефолтному тексту
def generate_image(text):
    if len(text) > 0:
        return picture_gen(text)
    else:
        return picture_gen('Pink elephant')

