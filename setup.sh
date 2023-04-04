mkdir -p ~/.gradio/

echo "\
[general]\n\
email = \"mayatskaya.katya@mail.ru\"\n\
" > ~/.gradio/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
" > ~/.gradio/config.toml
