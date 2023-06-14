import gradio as gr


text_sum = gr.Blocks.load(name="huggingface/csebuetnlp/mT5_multilingual_XLSum")
picture_gen = gr.Blocks.load(name="huggingface/CompVis/stable-diffusion-v1-4")


def predict_text(text):
    """ Если юзер не ввел текст, то суммаризация происходит по дефолтному тексту """
    if len(text) > 0:
        return text_sum(text)
    else:
        return text_sum(
            'Pink elephant likes eating a lot of fruits and vegetable, but it likes eating bananas more then others')   

def generate_image(text):
    """ Если юзер не ввел текст, то создание изображения происходит по дефолтному тексту """
    if len(text) > 0:
        return picture_gen(text)
    else:
        return picture_gen('Pink elephant')
    
    
if __name__=='__main__':
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=2):
                pass
            with gr.Column(scale=3, elem_id='main_col'):
                with gr.Row():
                    gr.Markdown(
                        """### The meaning in one picture!""")
                with gr.Row():
                    text_input=gr.Text(label='Enter your text here:', elem_id='text_input')
                    text_output=gr.Text(label='Text summary here', elem_id='text_output', interactive=False)
                with gr.Row():
                    get_text=gr.Button("Get summary", elem_id='button2')
                    image_button=gr.Button("Generate picture", elem_id='button2')
                with gr.Row():
                    image_output=gr.Image(label='Result', show_label=True, elem_id='image')
            with gr.Column(scale=2):
                pass

            
        get_text.click(predict_text, inputs=text_input, outputs=text_output)
        image_button.click(generate_image, inputs=text_output, outputs=image_output)
    demo.launch(server_name='0.0.0.0', server_port = 7000, share = True)
