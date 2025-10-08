import flet as ft
import flet_pages
import flet_pages.i18n
from pages import about,start
from locals import zh,en

def get_pages():
    pages = [
        start.page,about.page
    ]
    return pages
def main(page: ft.Page):
    flet_pages.i18n.I18n({
        "zh": zh.content,
        "en": en.content
    }, "en","./.config",True)
    page.title = "Video-Music-Lyrics-App"
    pages = get_pages()
    ui = flet_pages.pages(pages,page,True)


ft.app(main)