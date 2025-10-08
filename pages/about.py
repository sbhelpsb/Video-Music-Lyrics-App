import flet as ft
import flet_pages
import time
from flet_pages.router import PageMeta
from flet_pages.i18n import t


def get_about_content(ui: flet_pages.pages):
    co = ft.Column(
        [
            ft.Text("Video-Music-Lyrics-App", size=30),
            ft.Text(
                "✨A APP that allows CC subtitles from mainstream video websites on the market to be displayed outside the browser window✨",
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return ft.Container(
        content=co,
        alignment=ft.alignment.center,
        expand=True,
    )


page = PageMeta(
    label="about",
    func=get_about_content,
    title=lambda: t("about"),
)
