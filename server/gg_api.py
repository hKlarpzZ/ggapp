import fastapi
import io
from info_box_generator import generate_tab
import db_config as db_config
# import psycopg2
import data_types

app = fastapi.FastAPI()

# class Tab(BaseModel):
#     text: str | None = "test"
#     post_id: int | None = 1
#     img_type: str | None = "left"

# @app.post("/generate_tab")
# def show_pic(tab: Tab):
#     img_byte_arr = io.BytesIO()
#     img = generate_tab(tab.text, tab.post_id, tab.img_type)
#     roi_img = img.crop(box=None)
#     roi_img.save(img_byte_arr, format='PNG')
#     img_byte_arr = img_byte_arr.getvalue()

#     return fastapi.responses.StreamingResponse(io.BytesIO(img_byte_arr), media_type="image/png")

@app.get("/generate_tab/{img_type}/{id}")
def show_pic(img_type: str, id: int):
    if img_type == "author":
        author = data_types.Author(id)
        img_text = f"Никнейм: {author.nickname}\nРоль: {author.role}\n\nНажмите [ЛКМ], чтобы показать\nвсе посты этого пользователя."
    if img_type == "category":
        category = data_types.Category(id)
        img_text = f"{category.icon} - {category.description}.\n\n[ЛКМ], чтобы показать все посты в ней."
    if img_type == "item":
        pass #### Дописать, когда понадобится обработка предметов
    img_byte_arr = io.BytesIO()
    img = generate_tab(img_text)
    roi_img = img.crop(box=None)
    roi_img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return fastapi.responses.StreamingResponse(io.BytesIO(img_byte_arr), media_type="image/png")