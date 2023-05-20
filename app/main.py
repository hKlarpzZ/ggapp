from flet import *
from client_backend import SmallPost
# import logging
# logging.basicConfig(level=logging.DEBUG)



def main(page: Page):
    page.title = "GGworlds"
    page.fonts = {
        'main': './assets/minecraft.ttf'
    }
    page.window_min_height = 720
    page.window_min_width = 1280

    background = Container(
        image_src="assets/BG.png",
        image_fit=ImageFit.COVER,
        width=2000*page.width,
        expand=True,
        margin=-10,
        content=Stack(
            controls=[]
        )
    )

    post_list = Container(
        image_src="assets/BG_empty.png",
        image_fit=ImageFit.COVER,
        width=2000*page.width,
        expand=True,
        content=Column(
            controls=[],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll='auto',
            spacing=40,
        )
    )

    info_box = Container(
        image_src="boxes/empty.png",
        margin=margin.only(
            top=0,
            bottom=0,
            left=0,
            right=0,
        ),
        visible=False,
    )

    pages = {
        '/': View(
            "/",
            [
                background
            ],
        )
    }

    

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
        if page.route == '/':
            for i in range(1, 9):
                post_list.content.controls.append(SmallPost(i).post)
            background.content.controls.append(post_list)
            background.content.controls.append(info_box)
        
        # page.add(reload_btn)
        
    # page.add(background)

    page.on_route_change = route_change
    page.go(page.route)

    # page.add(reload_btn)

app(target=main, assets_dir="assets", view=WEB_BROWSER)
