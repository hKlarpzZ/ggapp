from flet import *

def info_box_empty(e: TapEvent):
    pass

info_box = GestureDetector(
    disabled=True,
    visible=False,
    on_tap=info_box_empty,
    left=0,
    top=0,
    content=Image(src=f"http://127.0.0.1:8000/generate_tab/author/1")
)