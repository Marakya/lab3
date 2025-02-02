## Jenkins
![Снимок экрана от 2023-04-08 11-23-33](https://user-images.githubusercontent.com/113238801/230707148-51349698-7446-4e7d-b46f-e8435f68b661.png)


## Вывод консоли
![Снимок экрана от 2023-04-08 11-17-14](https://user-images.githubusercontent.com/113238801/230707152-7e5cb3a9-241e-4eca-9ba9-ec33139461ca.png)

![Снимок экрана от 2023-04-08 11-17-59](https://user-images.githubusercontent.com/113238801/230707154-8930b6fa-d209-463f-80f7-a10d29c550b2.png)

![Снимок экрана от 2023-04-08 11-18-18](https://user-images.githubusercontent.com/113238801/230707162-f2f87e71-f568-44a6-bac3-1769785ecb9c.png)

## Результат работы

![Снимок экрана от 2023-04-08 11-19-39](https://user-images.githubusercontent.com/113238801/230707190-1d4e3c6b-97be-4ac4-a753-0e719dbb6693.png)


## Загрузка на DockerHub

![Снимок экрана от 2023-04-08 11-18-43](https://user-images.githubusercontent.com/113238801/230707181-68750fbd-2b0c-48db-bf32-dc374366b594.png)

## Работа приложения

![Снимок экрана от 2023-04-08 11-22-45](https://user-images.githubusercontent.com/113238801/230707220-990b18be-2ed5-47b8-8db3-2226f5172abc.png)


## Описание работы приложения

Цель данного приложения - суммаризация текста и последующая генерация изображания

#### Алгоритм работы приложения:
 1. Ввод текста, по которому пользователь хочет сделать суммаризацию;
 2. Генерация основной информации текста с помощью модели [mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum?text=Москва́+%28произношение+%28инф.%29%29+—+столица+России%2C+город+федерального+значения%2C+административный+центр+Центрального+федерального+округа+и+центр+Московской+области%2C+в+состав+которой+не+входит%5B6%5D.+Крупнейший+по+численности+населения+город+России+и+её+субъект+—+13+010+112%5B3%5D+человек+%282021%29%2C+самый+населённый+из+городов%2C+полностью+расположенных+в+Европе%2C+занимает+22-е+место+среди+городов+мира+по+численности+населения%5B7%5D%2C+крупнейший+русскоязычный+город+в+мире.+Центр+Московской+городской+агломерации.+Самый+крупный+город+Европы+по+площади%5B8%5D.);
 3.  Генерация изображения второй моделью [stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4?text=cyberpunk+avatar), где входными данными является суммаризированный первой моделью текст;
 4.  В случае, если на первом шаге пользователь не ввел текст, модель суммаризации будет работать с дефольтным текстом (прописанном в приложении), а вторая модель генерировать изображение в соответствии с резульатом работы первой модели;
